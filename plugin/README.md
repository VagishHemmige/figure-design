# Interactive Figure Design (plugin)

This folder is the plugin itself: the part Claude and Codex copy when you install it. It holds one skill, `skills/figure-to-interactive/`, plus a manifest for each app.

The skill helps an AI assistant make clear explanatory figures (workflow diagrams, study designs, system overviews), then faithful interactive versions. It agrees the content of each view with you, draws one static SVG per view, inspects the rendered picture, and waits for your approval before adding any interactivity.

## Install

- Claude Code: `claude plugin install figure-design --marketplace VagishHemmige/figure-design`
- Codex: `codex plugin marketplace add VagishHemmige/figure-design`, then `codex plugin add figure-design@figure-design`

Other routes (the Claude app, ChatGPT) are on the [Install page](https://vagishhemmige.github.io/figure-design/install.html).

## More

- How it works, guides and what's been tested: https://vagishhemmige.github.io/figure-design
- Source and issues: https://github.com/VagishHemmige/figure-design

## License

The original text and code are MIT licensed; see [LICENSE](LICENSE). That license does not cover `skills/figure-to-interactive/assets/transplantid-explainer.svg`, a reference figure that contains embedded artwork, logos and a font owned by others; see [`reference-assets.md`](skills/figure-to-interactive/references/reference-assets.md).
