# Pre-delivery inspection
The main skill defines when to review and seek approval. This checklist adds no approval gates.

## Content and topology
- Match each agreed view's actual explanation, including necessary decisions and exceptions.
- Distinguish planned/live/unverified behavior and actual source-to-output coverage.
- Trace each arrow end-to-end: correct source, target, direction and meaning; equivalent inputs must not look sequential.
- Shared objects use matching labels, visual identities and factual roles across views.
- Important prerequisites sit beside the affected step, not an unrelated footer.

## Geometry: automate where practical
- Measure rendered text/image bounds against containers and canvas; detect clipping and overlaps.
- Check text-to-icon, label-to-arrow and arrow-to-node collisions, excluding intentional endpoints and declared container-boundary crossings (design-principles.md A5, A6, T2).
- Inspect branch/merge junctions, arrowhead clearance, crossings, reversals and avoidable bends (A3, A4, A7, A9, A10, A11).
- Check aligned columns, padding and spacing consistency (L1, L2, L4).
- Apply the applicable rules in design-principles.md using their [measure], [review] and [look] methods; these tags do not claim implemented validators. Cite rule IDs, declared associations and justified exceptions. Mark unsupported or unavailable checks as not checked, never pass. Re-check moved elements, connected routes/labels and affected neighbours; re-check the whole view after scaling or global style changes.
- Parse SVG, verify referenced assets resolve, and ensure exports match current source.
Automated checks require explicit tolerances and semantic exceptions; a bounding-box pass is not proof of good design. Do not add a complex test harness for a trivial edit.

## Visual inspection
- Read the rendered figure at intended size: main action apparent, clear entry/exit, useful grouping and adequate contrast. Use the destination requirements and the scoped W3C contrast guidance in design-principles.md; a font-size floor is not proof of readability.
- No crowded Discovery/category boxes beside large unused regions; revise layout before adding more routing complexity.
- Consistent illustration family; meaningful teaching/career/document/browser graphics and legitimate logos.
- Inspect phone fit-to-width honestly. If illegible, provide usable enlarged viewing or agreed crops while preserving the approved illustration.
- Inspect every changed view and affected exports; never rely on stale screenshots.

## Independent design review for substantial work
Give an independent visual reviewer the current render, content brief, style reference, target size and current/planned distinctions. Ask for location, concrete problem, impact and smallest remedy; preserve content. Correct material findings and record deferrals. Keep factual/capability review distinct from visual design review. Do not automatically spawn a full review for minor edits.

## Interactive and delivery checks when applicable
Check exact-region highlight, complete hover, pointer entry, click pin, touch equivalent, keyboard/focus, Escape/close, zoom/pan, viewport-edge placement and scroll behavior. Check every view, not just the first. Keep accessible text equivalent and static outputs current.
Use a supported in-chat preview; local links are supplementary, not mobile attachments. Report actual browsers/devices tested, simulated tests and unavailable verification separately.
