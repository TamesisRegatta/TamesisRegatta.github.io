"""Custom macros for mkdocs-macros (auto-loaded by the plugin).

Personal contact details are never stored in the repository. They are read
from environment variables at build time (set from GitHub Actions secrets in
CI) and rendered lightly obfuscated: the value is reversed and base64-encoded
into a data attribute, and docs/assets/contacts.js decodes it in the browser.
This keeps plain phone numbers and email addresses out of the page source,
which defeats naive scrapers, while remaining readable to any visitor.
When a variable is unset (e.g. local builds), a "[withheld]" placeholder is
rendered instead.

The generic mailbox (regatta@linacre.ox.ac.uk) is intentionally NOT
obfuscated — it lives in event.yml and is rendered as a normal mailto: link.
"""

import base64
import os
from datetime import date


def _obfuscate(value: str) -> str:
    encoded = base64.b64encode(value[::-1].encode()).decode()
    return f'<span class="tr-contact" data-c="{encoded}">[enable JavaScript to view]</span>'


def _contact(prefix: str, key: str, placeholder: str) -> str:
    value = os.environ.get(f"{prefix}_{key.upper()}", "").strip()
    if not value:
        return f'<em class="tr-withheld">[{placeholder} withheld]</em>'
    return _obfuscate(value)


def _ukdate(d: date) -> str:
    """Render a date compactly: 'Wed 25 Nov 2026'."""
    return f"{d:%a} {d.day} {d:%b} {d.year}"


def define_env(env):
    dates = env.variables["dates"]
    dates["year"] = dates["regatta_start"].year

    @env.filter
    def ukdate(d) -> str:
        return _ukdate(d)

    @env.filter
    def ukdatetime(d) -> str:
        """'Wed 11 Nov 2026, 04:00' — always 24-hour clock."""
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
        """A phone number from the PHONE_<KEY> environment variable."""
        return _contact("PHONE", key, "number")

    @env.macro
    def email(key: str) -> str:
        """A personal email address from the EMAIL_<KEY> environment variable."""
        return _contact("EMAIL", key, "email")
