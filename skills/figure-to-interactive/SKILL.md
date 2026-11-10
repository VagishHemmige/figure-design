---
name: figure-to-interactive
description: Design and refine static explanatory figures, workflow diagrams, and interactive explainers using Vagish's preferences. Use for new diagrams, SVG refinement, interactive figure expansions, mobile presentation, or preparing an approved interactive for Quarto. Confirm content per view, approve static SVGs before interactivity, and review substantial designs independently.
---

# Static figures and interactive explainers

This is the authoritative workflow. Supporting references explain principles and checks; they do not create extra approval gates. Current user instructions take precedence. Reuse confirmed answers and approved work.

## References and style

- Before a new substantial design, inspect/render the bundled [TransplantID SVG](assets/transplantid-explainer.svg) and read [reference assets](references/reference-assets.md). Its companion website is the default base model for interactive presentation, adapted to the subject and agreed views.
- Read [design principles](references/design-principles.md) before layout and [inspection checklist](references/inspection-checklist.md) before delivery. Use the applicable host visualization, website, image, or document skill for implementation and delivery constraints.
- TransplantID is the preferred illustrated, information-rich style: numbered pastel phases, strong headings, meaningful illustrations, relevant logos and explicit arrows. General principles support that style, not automatic conversion into sparse cards or a different aesthetic. Explain concrete tradeoffs; do not restyle an accepted reference merely to satisfy a stylistic preference.

## 1. Agree on content for every view

For a new complex explanation, use [content intake](references/content-intake.md). Ask only consequential unanswered questions, at most three together: purpose/audience, scenarios, view count and what EACH view explains. If unsure, propose views and agree on them. Do not split related alternative routes merely to create tabs.

Present the actual plain-language content outline for each view: inputs, actors, meaningful actions, decisions, information read/saved, outputs, missing facts, waits and stop/resume paths where relevant. Distinguish implemented, planned and unverified behavior. Confirm each outline before drawing; agreement on tab names is not content approval. An exact user-supplied outline with an instruction to draw counts as confirmation. An explicit request to skip questions takes precedence; state consequential assumptions briefly.

Keep a compact authorized task brief: purpose, audience, views, content confirmations, unresolved facts, SVG versions and visual approvals. Do not claim persistent storage without saving it. Small edits do not restart intake; confirm only changed explanatory scope. Never invent facts to complete a layout.

## 2. Design the flow, then the static SVG

Choose the composition from the relationships before decorating it. Arrange the main flow, equivalent inputs, branches, merges and exceptions; reserve connector channels and label space. Difficult routes are a reason to reconsider placement, not keep adding bends. Arrows must represent real dependencies. Do not imply parallel inputs are sequential.

Create a static SVG for EACH view. Prefer editable text and geometry, with legitimate service logos and a consistent family of purposeful mini illustrations. Preserve known asset/license provenance. Do not imply embedded raster content is fully editable vector art. Keep factual detail needed to understand the overview; supporting detail can later expand without changing its meaning.

Use identical representations for shared records and outputs across views. Confirm actual source-to-output coverage rather than assuming every record feeds every output. Apply hierarchy, grouping, spacing and typography using the principles reference. Preserve a recoverable prior version before major redesign.

## 3. Inspect and independently review

Run the inspection checklist on rendered SVGs, not just source. Use automated geometry checks for bounds and collisions when practical, plus visual inspection for hierarchy, clarity, misleading paths and illustration quality. Report checks actually performed; do not equate a syntactically valid file with a visually successful figure.

For substantial new figures or major redesigns, obtain an independent visual-design review before presenting the approval draft when delegation is available and allowed. This instruction authorizes that review within the task. Supply the current renders, agreed content, style reference, target viewing context and current/planned distinctions. Ask for prioritized concrete problems and minimal fixes. The designer first examines the graphic; a separate functional reviewer may then compare it with the relevant implementation. Use audience perspectives to check comprehension as well. Do not claim independence for self-review; if delegation is unavailable, disclose that and apply the checklist yourself.

Correct material findings, re-render affected areas, and keep a compact record of resolved/deferred issues. Routine wording, logo or spacing edits require focused checks, not a fresh full independent review. Do not churn through speculative redesigns after the user accepts the composition.

## 4. Obtain visual approval per SVG

Show each static SVG through the host's supported in-chat visual viewer when available; retain the SVG source. A minimal static preview wrapper is delivery, not interactive implementation. A Windows-local link is not a phone-accessible uploaded attachment. If delivery fails, change the delivery method rather than repeatedly sending the same link or redesigning the figure.

Wait for explicit visual approval of EACH included view before building the combined interactive experience. Content approval, general project authorization and silence do not count as SVG approval. A user may explicitly waive a checkpoint; never infer that waiver. If only static output is requested, finish here.

## 5. Add faithful interactivity when requested

Preserve the approved composition, illustrations, colors, relationships and content. An expanded region should feel like a continuation of its original region. Use a brief interaction instruction. Desktop: delayed hover reveals the complete explanation, pointer can enter it, and click can pin it. Touch: the whole relevant region opens equivalent content. Keyboard: native focusable controls, visible focus and dismissal including Escape where applicable. Highlight only the exact selected region.

Prevent flicker, trigger-covering panels, accidental closure, label overlays and nested figure scrollbars. Provide usable enlarged/pannable viewing or agreed section crops when the whole figure is illegible at phone width. Do not silently replace the approved illustrated figure with a text accordion. Keep essential explanation available without hover and provide an equivalent accessible text account.

Maintain the approved view structure. For a new view, return to its content and SVG checkpoints. Routine interactive refinements do not reopen approved unrelated views. Keep downloads synchronized with visible figures.

## 6. Verify and deliver

Check explanation completeness as well as layout and interaction. Test applicable hover, pinning, dismissal, keyboard, touch, zoom, viewport edges, scrolling and links. Distinguish desktop emulation from physical-phone and other-browser testing. Report limitations honestly.

Keep source, assets and exports portable; avoid unnecessary servers or extensions. For Quarto integration when requested, supply files and a minimal integration example; choose direct embedding or an iframe deliberately and verify paths, copied assets, height and post-render behavior. Do not promise that an existing hotspot extension reproduces the design without checking. Publish only within user authorization. End with the actual result, material limits and any unresolved decision.
