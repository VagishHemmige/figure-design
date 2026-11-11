"""Check that the plugin's manifests agree, and that the site is not ahead of them.

The plugin lives in plugin/; the marketplace files at the repository root
point at it, so installs copy only that folder.

Fails (exit 1) when:
  - the three plugin.json files differ in name or version, or
  - the two marketplace files don't list a plugin by that name, or
  - a marketplace entry's source folder isn't plugin/, or
  - plugin/LICENSE differs from the root LICENSE, or
  - a site page says it was written for a version newer than the plugin.
Warns (exit 0) when a site page was written for an older version, so pages
that haven't changed since an earlier release don't block a pull request.

Run from the repository root: python3 .github/scripts/check_versions.py
Standard library only.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PLUGIN_DIR = ROOT / "plugin"
MANIFESTS = ["plugin/plugin.json", "plugin/.codex-plugin/plugin.json", "plugin/.claude-plugin/plugin.json"]
MARKETPLACES = [".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"]
WRITTEN_FOR = re.compile(r"Written for version (\d+(?:\.\d+)*)")


def as_tuple(version):
    return tuple(int(part) for part in version.split("."))


def main():
    errors, warnings = [], []

    found = {}
    for rel in MANIFESTS:
        manifest = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        found[rel] = (manifest.get("name"), manifest.get("version"))
    if len(set(found.values())) != 1:
        listing = ", ".join(f"{rel} = {name} {version}" for rel, (name, version) in found.items())
        errors.append(f"plugin.json files disagree: {listing}")
    name, version = found[MANIFESTS[0]]

    for rel in MARKETPLACES:
        catalog = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        entries = catalog.get("plugins", [])
        listed = [entry.get("name") for entry in entries]
        if name not in listed:
            errors.append(f"{rel} does not list plugin '{name}' (lists {listed})")
        for entry in entries:
            if entry.get("name") != name:
                continue
            # Claude uses a plain relative path; Codex uses {"source": "local", "path": ...}.
            source = entry.get("source")
            source_path = source.get("path") if isinstance(source, dict) else source
            if not isinstance(source_path, str) or (ROOT / source_path).resolve() != PLUGIN_DIR:
                errors.append(f"{rel} points '{name}' at {source_path!r}, not ./plugin")

    if (ROOT / "LICENSE").read_bytes() != (PLUGIN_DIR / "LICENSE").read_bytes():
        errors.append("plugin/LICENSE differs from LICENSE; installs must carry the same license")

    for page in sorted((ROOT / "site").rglob("*.qmd")):
        match = WRITTEN_FOR.search(page.read_text(encoding="utf-8"))
        if not match:
            continue
        page_version = match.group(1)
        rel = page.relative_to(ROOT)
        if as_tuple(page_version) > as_tuple(version):
            errors.append(f"{rel} says version {page_version}, newer than the plugin's {version}")
        elif page_version != version:
            warnings.append(f"{rel} was written for {page_version}; the plugin is {version}. Check it still matches.")

    for line in warnings:
        print(f"::warning::{line}")
    for line in errors:
        print(f"::error::{line}")
    if not errors:
        print(f"OK: {name} {version} in all three plugin.json files and both marketplace files.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
