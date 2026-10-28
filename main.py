"""Custom macros for mkdocs-macros (auto-loaded by the plugin).

Personal contact details are never stored in the repository. They are read
from environment variables at build time (set from GitHub Actions secrets in
CI) and rendered lightly obfuscated: the value is reversed and base64-encoded
into a data attribute, and docs/assets/contacts.js decodes it in the browser.
This keeps plain phone numbers and email addresses out of the page source,
which defeats naive scrapers, while remaining readable to any visitor.
For local builds, the same values can instead come from contacts.local.yml
at the repository root (git-ignored; see contacts.local.example.yml).
Environment variables take precedence over it. CI never has that file, so it
cannot put numbers on the live site. When a value is in neither place, a
"[withheld]" placeholder is rendered instead, and the event plan carries a
"Public version: contact details removed" notice (redaction_notice()) unless
every key in contacts.local.example.yml has a value.

The generic mailbox (regatta@linacre.ox.ac.uk) is intentionally NOT
obfuscated: it lives in event.yml and is rendered as a normal mailto: link.
"""

import base64
import html
import os
from datetime import date
from pathlib import Path

import yaml

# Local contact details for building with real numbers on your own machine.
# Git-ignored, never committed; see contacts.local.example.yml.
_LOCAL_CONTACTS = Path(__file__).parent / "contacts.local.yml"

# The example file is the canonical list of contact keys: a build counts as
# complete (no redaction notice) only when every key in it has a value, and
# pages may only use keys listed in it.
_CONTACT_KEYS = {
    kind: set(keys or {})
    for kind, keys in (yaml.safe_load(
        (Path(__file__).parent / "contacts.local.example.yml").read_text(encoding="utf-8")
    ) or {}).items()
}


def _load_local_contacts() -> dict:
    if not _LOCAL_CONTACTS.exists():
        return {}
    data = yaml.safe_load(_LOCAL_CONTACTS.read_text(encoding="utf-8")) or {}
    # Keys as in the macros: phone: {fergus_cooper: ...}, email: {...}
    return {kind: {k: str(v) for k, v in (data.get(kind) or {}).items() if v}
            for kind in ("phone", "email")}


_local_contacts = _load_local_contacts()


def _obfuscate(value: str) -> str:
    encoded = base64.b64encode(value[::-1].encode()).decode()
    return f'<span class="tr-contact" data-c="{encoded}">[enable JavaScript to view]</span>'


def _value(prefix: str, key: str) -> str:
    """A contact detail from the environment (CI secrets) or, failing that,
    contacts.local.yml; empty if neither has it."""
    value = os.environ.get(f"{prefix}_{key.upper()}", "").strip()
    if not value:
        value = _local_contacts.get(prefix.lower(), {}).get(key, "").strip()
    return value


def _contact(prefix: str, key: str, placeholder: str) -> str:
    if key not in _CONTACT_KEYS.get(prefix.lower(), set()):
        raise ValueError(f"{prefix.lower()}('{key}') is not listed in contacts.local.example.yml")
    value = _value(prefix, key)
    if not value:
        return f'<em class="tr-withheld">[{placeholder} withheld]</em>'
    return _obfuscate(value)


def _contacts_complete() -> bool:
    """True when every contact key has a value, i.e. nothing is withheld."""
    return all(_value(kind.upper(), key) for kind, keys in _CONTACT_KEYS.items() for key in keys)


def _ukdate(d: date) -> str:
    """Render a date compactly: 'Wed 25 Nov 2026'."""
    return f"{d:%a} {d.day} {d:%b} {d.year}"


_RISK_LEVEL_LABELS = {
    "low": "Low",
    "moderate": "Moderate",
    "substantial": "Substantial",
    "intolerable": "Intolerable",
}


def define_env(env):
    dates = env.variables["dates"]
    dates["year"] = dates["regatta_start"].year

    risk_matrix = env.variables["risk_matrix"]
    probabilities = sorted(risk_matrix["probability"])
    severities = sorted(risk_matrix["severity"])
    for s in severities:
        missing = [p for p in probabilities if p not in risk_matrix["levels"].get(s, {})]
        if missing:
            raise ValueError(f"risk_matrix.yml: severity {s} is missing probabilities {missing}")
        for p in probabilities:
            level = risk_matrix["levels"][s][p]
            if level not in _RISK_LEVEL_LABELS:
                raise ValueError(f"risk_matrix.yml: unknown level {level!r} at severity {s}, probability {p}")

    @env.filter
    def ukdate(d) -> str:
        return _ukdate(d)

    @env.filter
    def ukdatetime(d) -> str:
        """'Wed 11 Nov 2026, 04:00': always 24-hour clock."""
        return f"{_ukdate(d)}, {d:%H:%M}"

    @env.macro
    def daterange(start: date, end: date) -> str:
        """'Wed 25 – Sat 28 Nov 2026', eliding the month and year when
        shared."""
        if (start.year, start.month) == (end.year, end.month):
            return f"{start:%a} {start.day} – {end:%a} {end.day} {end:%b} {end.year}"
        return f"{_ukdate(start)} – {_ukdate(end)}"

    @env.macro
    def phone(key: str) -> str:
        """An organisation's public number from public_phones in event.yml,
        shown as it is; otherwise a person's number from the PHONE_<KEY>
        environment variable or contacts.local.yml, obfuscated."""
        public = env.variables.get("public_phones") or {}
        if key in public:
            return html.escape(str(public[key]))
        return _contact("PHONE", key, "number")

    @env.macro
    def redaction_notice() -> str:
        """A prominent notice that this is the public version without contact
        details. Empty when every contact detail is available (e.g. a local
        build with a complete contacts.local.yml), so full versions don't
        carry it."""
        if _contacts_complete():
            return ""
        return (
            '!!! warning "Public version: contact details removed"\n'
            "    This public version of the plan does not include contact details.\n"
            "    The full version, with all contact details, is sent directly to\n"
            "    event officials and others who need it.\n"
        )

    @env.macro
    def email(key: str) -> str:
        """A personal email address from the EMAIL_<KEY> environment variable."""
        return _contact("EMAIL", key, "email")

    @env.macro
    def risk(severity: int, probability: str) -> str:
        """A colour-coded 'Level of Risk' badge, derived from severity and
        probability via risk_matrix.yml; never pass a level in directly, so
        it can't disagree with the severity/probability that produced it."""
        probability = probability.upper()
        try:
            level = risk_matrix["levels"][severity][probability]
        except KeyError:
            raise ValueError(
                f"risk(): no matrix entry for severity={severity!r}, probability={probability!r}"
            )
        label = _RISK_LEVEL_LABELS[level]
        return (
            f'<span class="risk-badge risk-{level}">{label}</span>'
            f'<span class="risk-meta"> (severity {severity}, probability {probability})</span>'
        )

    @env.macro
    def risk_matrix_table() -> str:
        """The full severity x probability matrix, rendered from
        risk_matrix.yml so the legend can never drift from what risk()
        actually looks up."""
        rows = ['<tr><th></th>']
        for p in probabilities:
            rows.append(f"<th>{p}</th>")
        rows.append("</tr>")
        for s in reversed(severities):
            rows.append(f"<tr><th>{s}</th>")
            for p in probabilities:
                level = risk_matrix["levels"][s][p]
                rows.append(f'<td class="risk-{level}">{_RISK_LEVEL_LABELS[level]}</td>')
            rows.append("</tr>")
        return f'<table class="risk-matrix">{"".join(rows)}</table>'
