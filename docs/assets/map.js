// Course map (map.md). The SVG is fetched and inlined rather than shown as an
// <img>, so that the colour variables in extra.css (light and dark scheme)
// reach it, and so that later scripts can address its layers and markers.
//
// Pan and zoom use d3-zoom (vendor/d3/, loaded only on pages with a map):
// wheel or trackpad to zoom, drag to pan, pinch on touch, double-click to
// zoom in, plus +/-/home buttons and keys (+ - 0 and arrows) for keyboard use.
(function () {
  // data-map is relative to this script (docs/assets/), so the page's own
  // depth doesn't matter.
  var base = document.currentScript.src;

  var MAX_SCALE = 10;
  var STEP = 1.6; // zoom factor per button press or key
  var PAN_STEP = 0.15; // fraction of the visible width per arrow key
  var CLICK_DISTANCE = 4; // px a press may move and still count as a click
  // How near (screen px) a click or tap must be to an item to select it. Map
  // icons can be only a few px across when zoomed out, so a hit on the icon
  // itself is not required.
  var HIT_RADIUS = { mouse: 18, touch: 28 };
  // Fired on the frame whenever the view or the visible layers change.
  var CHANGED = "tamesis-map-changed";

  var ICONS = {
    // Material Design Icons: plus, minus, home, close.
    in: "M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z",
    out: "M19,13H5V11H19V13Z",
    home: "M10,20V14H14V20H19V12H22L12,2L2,12H5V20H10Z",
    close: "M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",
  };

  var d3Loaded;
  function loadD3() {
    if (!d3Loaded) {
      d3Loaded = new Promise(function (resolve, reject) {
        var s = document.createElement("script");
        s.src = new URL("vendor/d3/d3-zoom.min.js", base);
        s.onload = resolve;
        s.onerror = function () {
          reject(new Error("could not load " + s.src));
        };
        document.head.appendChild(s);
      });
    }
    return d3Loaded;
  }

  function loadSvg(frame) {
    var url = new URL(frame.dataset.map, base);
    return fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error(r.status + " " + url);
        return r.text();
      })
      .then(function (text) {
        var svg = new DOMParser().parseFromString(text, "image/svg+xml").documentElement;
        svg = document.importNode(svg, true);
        svg.setAttribute("role", "img");
        svg.setAttribute("aria-label", frame.dataset.label || "Map");
        // Everything but <defs> goes into one group that carries the zoom
        // transform, so markers and text-wrap shapes in <defs> are untouched.
        var viewport = document.createElementNS("http://www.w3.org/2000/svg", "g");
        viewport.setAttribute("class", "tamesis-map-viewport");
        Array.from(svg.childNodes).forEach(function (n) {
          if (n.nodeName !== "defs") viewport.appendChild(n);
        });
        svg.appendChild(viewport);
        frame.replaceChildren(svg);
        return svg;
      });
  }

  function button(kind, label) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "tamesis-map-button";
    b.title = label;
    b.setAttribute("aria-label", label);
    b.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="' + ICONS[kind] + '"/></svg>';
    return b;
  }

  function enableZoom(frame, svg) {
    var viewport = svg.querySelector(".tamesis-map-viewport");
    var vb = svg.viewBox.baseVal;
    var mapRect = [[vb.x, vb.y], [vb.x + vb.width, vb.y + vb.height]];
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    // The frame's shape rarely matches the map's, so the SVG letterboxes it
    // (preserveAspectRatio meet). This is the area actually on screen, in map
    // units, which d3-zoom needs as its extent so zoom centres correctly.
    function visibleRect() {
      var w = svg.clientWidth || 1;
      var h = svg.clientHeight || 1;
      var s = Math.min(w / vb.width, h / vb.height);
      var vw = w / s;
      var vh = h / s;
      var x = vb.x + (vb.width - vw) / 2;
      var y = vb.y + (vb.height - vh) / 2;
      return [[x, y], [x + vw, y + vh]];
    }

    var zoom = d3
      .zoom()
      .scaleExtent([1, MAX_SCALE])
      .extent(visibleRect)
      // d3's default constrain, but against the map's edges or the letterbox,
      // whichever is larger, since the letterbox changes with the window.
      .constrain(function (t, extent) {
        var v = visibleRect();
        var x0 = Math.min(mapRect[0][0], v[0][0]);
        var y0 = Math.min(mapRect[0][1], v[0][1]);
        var x1 = Math.max(mapRect[1][0], v[1][0]);
        var y1 = Math.max(mapRect[1][1], v[1][1]);
        var dx0 = t.invertX(extent[0][0]) - x0;
        var dx1 = t.invertX(extent[1][0]) - x1;
        var dy0 = t.invertY(extent[0][1]) - y0;
        var dy1 = t.invertY(extent[1][1]) - y1;
        return t.translate(
          dx1 > dx0 ? (dx0 + dx1) / 2 : Math.min(0, dx0) || Math.max(0, dx1),
          dy1 > dy0 ? (dy0 + dy1) / 2 : Math.min(0, dy0) || Math.max(0, dy1)
        );
      })
      .clickDistance(CLICK_DISTANCE)
      // d3's default allows only the primary button; also allow middle-drag.
      .filter(function (event) {
        return (!event.ctrlKey || event.type === "wheel") && (!event.button || event.button === 1);
      })
      .on("start", function (event) {
        if (event.sourceEvent && event.sourceEvent.type !== "wheel") frame.classList.add("is-panning");
      })
      .on("zoom", function (event) {
        viewport.setAttribute("transform", event.transform);
        frame.dispatchEvent(new Event(CHANGED));
      })
      .on("end", function () {
        frame.classList.remove("is-panning");
      });

    var sel = d3.select(svg).call(zoom);
    // Stop middle-click from starting the browser's autoscroll.
    svg.addEventListener("mousedown", function (e) {
      if (e.button === 1) e.preventDefault();
    });

    function animated() {
      return sel.transition().duration(reduceMotion.matches ? 0 : 250);
    }
    var actions = {
      in: function () {
        animated().call(zoom.scaleBy, STEP);
      },
      out: function () {
        animated().call(zoom.scaleBy, 1 / STEP);
      },
      home: function () {
        animated().call(zoom.transform, d3.zoomIdentity);
      },
      pan: function (dx, dy) {
        var v = visibleRect();
        var k = d3.zoomTransform(svg).k;
        var step = ((v[1][0] - v[0][0]) * PAN_STEP) / k;
        animated().call(zoom.translateBy, -dx * step, -dy * step);
      },
    };

    var controls = document.createElement("div");
    controls.className = "tamesis-map-controls";
    [["in", "Zoom in"], ["out", "Zoom out"], ["home", "Show whole map"]].forEach(function (c) {
      var b = button(c[0], c[1]);
      b.addEventListener("click", actions[c[0]]);
      controls.appendChild(b);
    });
    frame.appendChild(controls);

    frame.tabIndex = 0;
    frame.setAttribute("aria-label", "Course map. Use plus and minus to zoom, arrow keys to pan, 0 to reset.");
    frame.addEventListener("keydown", function (e) {
      if (e.target !== frame || e.altKey || e.ctrlKey || e.metaKey) return;
      var k = e.key;
      if (k === "+" || k === "=") actions.in();
      else if (k === "-" || k === "_") actions.out();
      else if (k === "0" || k === "Home") actions.home();
      else if (k === "ArrowLeft") actions.pan(-1, 0);
      else if (k === "ArrowRight") actions.pan(1, 0);
      else if (k === "ArrowUp") actions.pan(0, -1);
      else if (k === "ArrowDown") actions.pan(0, 1);
      else return;
      e.preventDefault();
    });

    // The visible area changes with the window; re-apply the limits.
    new ResizeObserver(function () {
      sel.call(zoom.translateBy, 0, 0);
    }).observe(svg);
  }

  // Layer controls, built from the SVG's own markup (see scripts/strip_map.py):
  // groups with data-course form a pick-one radio group plus "None", groups
  // with data-overlay are independent checkboxes, and data-title labels each.
  // The selection is kept in the URL (?course=none&aed=0), non-defaults only,
  // so a link can open a particular view.
  function layerControls(frame, svg) {
    var courses = Array.from(svg.querySelectorAll(".tamesis-map-viewport > [data-course]"));
    var overlays = Array.from(svg.querySelectorAll(".tamesis-map-viewport > [data-overlay]"));
    var defaultCourse = courses.filter(function (g) {
      return g.dataset.default === "true";
    })[0];
    var defaults = { course: defaultCourse ? defaultCourse.dataset.course : "none" };
    overlays.forEach(function (g) {
      defaults[g.dataset.overlay] = true;
    });

    var state = Object.assign({}, defaults);
    // Values in the URL that don't match anything on this map are ignored.
    var params = new URLSearchParams(location.search);
    var wanted = params.get("course");
    var known = courses.some(function (g) {
      return g.dataset.course === wanted;
    });
    if (known || wanted === "none") state.course = wanted;
    overlays.forEach(function (g) {
      var v = params.get(g.dataset.overlay);
      if (v === "0" || v === "1") state[g.dataset.overlay] = v === "1";
    });

    function apply() {
      courses.forEach(function (g) {
        g.classList.toggle("is-hidden", g.dataset.course !== state.course);
      });
      overlays.forEach(function (g) {
        g.classList.toggle("is-hidden", !state[g.dataset.overlay]);
      });
      var p = new URLSearchParams(location.search);
      Object.keys(defaults).forEach(function (k) {
        var v = state[k];
        if (v === defaults[k]) p.delete(k);
        else p.set(k, typeof v === "boolean" ? (v ? "1" : "0") : v);
      });
      var q = p.toString();
      history.replaceState(history.state, "", location.pathname + (q ? "?" + q : "") + location.hash);
      frame.dispatchEvent(new Event(CHANGED));
    }

    function control(type, name, value, label, checked, onChange) {
      var l = document.createElement("label");
      l.className = "tamesis-map-option";
      var i = document.createElement("input");
      i.type = type;
      if (name) i.name = name;
      i.value = value;
      i.checked = checked;
      i.addEventListener("change", onChange);
      l.append(i, " " + label);
      return l;
    }

    function group(legend, children) {
      var f = document.createElement("fieldset");
      f.className = "tamesis-map-group";
      var lg = document.createElement("legend");
      lg.textContent = legend;
      f.append(lg);
      children.forEach(function (c) {
        f.append(c);
      });
      return f;
    }

    var name = "tamesis-map-course-" + Math.random().toString(36).slice(2, 8);
    var bar = document.createElement("div");
    bar.className = "tamesis-map-layers";
    if (courses.length) {
      var opts = [{ id: "none", title: "None" }].concat(
        courses.map(function (g) {
          return { id: g.dataset.course, title: g.dataset.title || g.dataset.course };
        })
      );
      bar.append(
        group(
          "Course",
          opts.map(function (o) {
            return control("radio", name, o.id, o.title, state.course === o.id, function () {
              state.course = o.id;
              apply();
            });
          })
        )
      );
    }
    if (overlays.length) {
      bar.append(
        group(
          "Show",
          overlays.map(function (g) {
            var k = g.dataset.overlay;
            return control("checkbox", null, k, g.dataset.title || k, state[k], function (e) {
              state[k] = e.target.checked;
              apply();
            });
          })
        )
      );
    }
    frame.before(bar);
    apply();
  }

  // Clickable map items: elements with data-select (see scripts/strip_map.py).
  // A click or tap picks the nearest visible item within HIT_RADIUS and opens
  // a popup over the map. The popup is HTML, so its size does not change with
  // zoom; it follows the item as the map moves and closes when the item's
  // layer is hidden. Items are also focusable and open with Enter or Space.
  // Items sharing a data-id are one real thing drawn more than once (e.g. an
  // AED at both ends of the map): all of them get a ring, and the popup points
  // at the one that was chosen.
  function enableSelect(frame, svg) {
    var items = Array.from(svg.querySelectorAll("[data-select]"));
    if (!items.length) return;
    var selected = null; // the item the popup points at
    var group = []; // it and any items sharing its data-id

    var popup = document.createElement("div");
    popup.className = "tamesis-map-popup";
    popup.setAttribute("role", "dialog");
    popup.hidden = true;
    var markers = new Map();
    items.forEach(function (el) {
      var m = document.createElement("div");
      m.className = "tamesis-map-marker";
      m.hidden = true;
      markers.set(el, m);
      frame.append(m);
    });
    frame.append(popup);

    items.forEach(function (el) {
      el.setAttribute("tabindex", "0");
      el.setAttribute("role", "button");
      el.setAttribute("aria-label", el.dataset.name);
      el.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          open(el, true);
        }
      });
    });

    function visible(el) {
      var r = el.getBoundingClientRect();
      return r.width > 0 || r.height > 0;
    }

    function centre(el) {
      var r = el.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2, r: r };
    }

    function nearest(x, y, radius) {
      var best = null;
      var bestD = radius;
      items.forEach(function (el) {
        if (!visible(el)) return;
        var c = centre(el);
        // Distance to the item's box, so large items count from their edge.
        var dx = Math.max(c.r.left - x, 0, x - c.r.right);
        var dy = Math.max(c.r.top - y, 0, y - c.r.bottom);
        var d = Math.hypot(dx, dy);
        if (d <= bestD) {
          best = el;
          bestD = d;
        }
      });
      return best;
    }

    function content(el) {
      var title = document.createElement("strong");
      title.className = "tamesis-map-popup-title";
      title.textContent = el.dataset.name;
      var close = document.createElement("button");
      close.type = "button";
      close.className = "tamesis-map-popup-close";
      close.setAttribute("aria-label", "Close");
      close.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="' + ICONS.close + '"/></svg>';
      close.addEventListener("click", function () {
        closePopup(true);
      });
      var parts = [close, title];
      if (el.dataset.w3w) {
        var line = document.createElement("p");
        var a = document.createElement("a");
        a.href = "https://what3words.com/" + encodeURIComponent(el.dataset.w3w);
        a.target = "_blank";
        a.rel = "noopener";
        a.textContent = "///" + el.dataset.w3w;
        line.append("what3words: ", a);
        parts.push(line);
      }
      return parts;
    }

    function open(el, viaKeyboard) {
      hideMarkers();
      selected = el;
      group = el.dataset.id
        ? items.filter(function (i) {
            return i.dataset.id === el.dataset.id;
          })
        : [el];
      popup.replaceChildren.apply(popup, content(el));
      popup.setAttribute("aria-label", el.dataset.name);
      popup.hidden = false;
      group.forEach(function (i) {
        markers.get(i).hidden = false;
      });
      place();
      if (viaKeyboard) (popup.querySelector("a") || popup.querySelector("button")).focus();
    }

    function closePopup(returnFocus) {
      if (!selected) return;
      var el = selected;
      selected = null;
      popup.hidden = true;
      hideMarkers();
      if (returnFocus) el.focus({ preventScroll: true });
    }

    function hideMarkers() {
      group.forEach(function (i) {
        markers.get(i).hidden = true;
      });
      group = [];
    }

    // Ring an item; returns its centre in frame coordinates and whether that
    // is in view. Rings are hidden while their item is panned out of view.
    function ring(el) {
      var f = frame.getBoundingClientRect();
      var c = centre(el);
      var m = markers.get(el);
      // Absolute positions are measured from inside the frame's border.
      var x = c.x - f.left - frame.clientLeft;
      var y = c.y - f.top - frame.clientTop;
      var inView = visible(el) && x >= 0 && x <= frame.clientWidth && y >= 0 && y <= frame.clientHeight;
      m.style.visibility = inView ? "" : "hidden";
      var size = Math.max(c.r.width, c.r.height) + 12;
      m.style.width = m.style.height = size + "px";
      // Positioned by its centre (CSS translate), since a minimum size in
      // CSS can make it larger than size.
      m.style.left = x + "px";
      m.style.top = y + "px";
      return { x: x, y: y, inView: inView, radius: m.offsetWidth / 2 };
    }

    // Anchor the popup above the chosen item (below if there is no room),
    // keep it inside the frame, and hide it while that item is out of view.
    function place() {
      if (!selected) return;
      if (!visible(selected)) {
        closePopup(false);
        return;
      }
      group.forEach(function (i) {
        if (i !== selected) ring(i);
      });
      var r = ring(selected);
      var x = r.x;
      var y = r.y;
      popup.style.visibility = r.inView ? "" : "hidden";

      var gap = r.radius + 8;
      var pw = popup.offsetWidth;
      var ph = popup.offsetHeight;
      var below = y - gap - ph < 0;
      popup.classList.toggle("is-below", below);
      var left = Math.min(Math.max(x - pw / 2, 8), frame.clientWidth - pw - 8);
      popup.style.left = left + "px";
      popup.style.top = (below ? y + gap : y - gap - ph) + "px";
      popup.style.setProperty("--arrow-x", x - left + "px");
    }

    svg.addEventListener("click", function (e) {
      var touch = e.pointerType === "touch";
      var el = nearest(e.clientX, e.clientY, touch ? HIT_RADIUS.touch : HIT_RADIUS.mouse);
      if (el) open(el, false);
      else closePopup(false);
    });

    // Pointer cursor when an item is within reach.
    var pending = false;
    svg.addEventListener("mousemove", function (e) {
      if (pending) return;
      pending = true;
      requestAnimationFrame(function () {
        pending = false;
        frame.classList.toggle("is-over-item", !!nearest(e.clientX, e.clientY, HIT_RADIUS.mouse));
      });
    });

    frame.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && selected) {
        e.preventDefault();
        closePopup(true);
      }
    });
    frame.addEventListener(CHANGED, place);
    // Focusing an item can make the browser scroll the frame to it, even
    // with overflow hidden; the view is d3-zoom's job, so undo that.
    frame.addEventListener("scroll", function () {
      frame.scrollTop = 0;
      frame.scrollLeft = 0;
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".tamesis-map-frame[data-map]").forEach(function (frame) {
      // Static figures (e.g. the raft allocation) are inlined only for the
      // theme colours: no layer controls, no zoom, no d3.
      if (frame.classList.contains("tamesis-map-static")) {
        loadSvg(frame).catch(function (err) {
          console.error("Map figure failed to load:", err);
        });
        return;
      }
      Promise.all([loadSvg(frame), loadD3()])
        .then(function (r) {
          layerControls(frame, r[0]);
          enableZoom(frame, r[0]);
          enableSelect(frame, r[0]);
        })
        .catch(function (err) {
          console.error("Course map failed to load:", err);
        });
    });
  });
})();
