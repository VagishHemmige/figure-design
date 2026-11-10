# Interactive Figure Design

A plugin for Claude and ChatGPT/Codex that helps an AI assistant make clear explanatory figures (workflow diagrams, study designs, system overviews), then faithful interactive versions of them.

Instead of drawing first and asking later, the assistant agrees the content of each view with you, draws one static SVG per view, inspects the rendered picture, and waits for your approval before adding any interactivity. The default look is an information-rich illustrated style: numbered pastel phases, strong headings, meaningful small illustrations and clearly labelled arrows.

It's built for explaining processes, not plotting data: a plot of real numbers is better made by the analysis code that produces it.

**Website:** https://vagishhemmige.github.io/figure-design (how it works, guides, and what has been tested)

## Install

This repository is its own plugin marketplace.

- **Claude Code** (2.1.292 or later): `claude plugin install figure-design --marketplace VagishHemmige/figure-design`
- **Codex:** `codex plugin marketplace add VagishHemmige/figure-design`, then `codex plugin add figure-design@figure-design`
- **Claude app** (web, desktop, Cowork): Settings → Customize → Plugins → Add → Add marketplace → `VagishHemmige/figure-design`
- **ChatGPT:** ask Plugin Creator to create a plugin from this repository

Full steps, and which routes have been tested, are on the [Install page](https://vagishhemmige.github.io/figure-design/install.html).

## What's in the repository

| Path | What it is |
|---|---|
| `skills/figure-to-interactive/` | The skill: `SKILL.md` (the workflow) and its `references/` |
| `plugin.json`, `.codex-plugin/`, `.claude-plugin/`, `.agents/` | Manifests and marketplace files for each app |
| `site/` | Source of the website (not part of the plugin's instructions) |
| `.github/` | Publishes the website and checks the manifests agree |

When the version changes, change it in all three `plugin.json` files; a check on every pull request fails if they differ.

## Before you rely on it

The plugin guides an assistant; it does not check your facts. Review what a figure says as you would a colleague's draft. Version 0.1.5 is early and has been used only by the maintainer.

## License

The original text and code are MIT licensed; see [LICENSE](LICENSE). That license does not cover `skills/figure-to-interactive/assets/transplantid-explainer.svg`, a reference figure that contains embedded artwork, logos and a font owned by others; see [`reference-assets.md`](skills/figure-to-interactive/references/reference-assets.md).
