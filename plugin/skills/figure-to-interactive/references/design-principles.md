# Design principles and sources
These are practical applications of established guidance, not rigid aesthetic rules. Preserve the user's preferred information-rich TransplantID style. Diagnose specific communication problems; do not prescribe minimalism, remove essential content or redesign accepted figures just because a source uses another visual style.

## Composition before decoration
Choose an orientation and reading order that explain the relationships. Put sequential steps in aligned stages; give equivalent inputs equal weight; put exceptions beside the relevant step. Reserve space for branch/merge channels before placing boxes. Minimize unnecessary crossings, bends and reversals. Use clear junctions and arrowheads; proximity alone must not imply a relationship.

yWorks describes layered placement and crossing reduction: https://www.yworks.com/pages/layered-graph-layout.html
Its orthogonal router describes routing while preserving node positions: https://yed.yworks.com/support/manual/layout/router_orthogonal.html
These references do not require purchasing or using yFiles; apply the principles with tools suitable to the task. Automatic layout still needs inspection and can mishandle labels or constraints.

## Applying the rules

Preserve the agreed meaning first. Never alter a relationship merely to pass a geometry check. Apply the rules when drawing and after revisions; cite their IDs in findings. Treat layout thresholds as defaults. Record each justified exception with its rule ID, reason and affected elements. An exception cannot make an incorrect relationship correct or waive a claimed destination/accessibility requirement. An accepted reference is a style anchor, not proof that every detail meets these rules.

Check tags describe possible methods, not implemented validators:

- **[measure]**: a mechanical measurement, given supported geometry and declared associations.
- **[review]**: a measurement may flag a candidate problem, but a reviewer decides whether it is a defect.
- **[look]**: visual or semantic judgment against the agreed content.

Before mechanical checks, identify nodes, containing regions, connectors, labels and intentional junctions; associate labels with their owners and connectors with their endpoints. Declare comparable rows/columns/groups and any style key. Unsupported geometry or missing associations mean **not checked**, never pass. Do not infer semantics from proximity alone. A measurement pass does not establish readability or factual correctness.

Measure after SVG transforms and viewBox scaling at each declared destination size. Here px means final rendered CSS pixels (96 px per inch); print text uses points (72 pt per inch). Raster export DPI is not CSS display size. The 8 px clearances, 12 px margins, 2 px tolerances and bend targets below are plugin defaults, not published standards.

## Connectors and arrows

- **A1 One arrow, one relationship.** Show a real sequence, data flow or dependency with the correct direction. Do not add arrows only to lead the eye. [look]
- **A2 Label the relationship.** If meaning is unclear from the endpoints, put a short label beside an identifiable segment, preferably near its middle. Keep the relationship label local; a key may separately explain shared line styles. [look]
- **A3 Remove crossings by placement first.** Consider reordering comparable boxes before rerouting; preserve meaningful order and grouping. Aim for no unnecessary crossings. Counting crossings flags candidates, not proof that a layout is wrong. [review]
- **A4 Distinguish crossings from junctions.** At unavoidable non-junction crossings, aim for a right angle away from labels, junctions and arrowheads. Use a gap or bridge so connectivity does not depend on hue alone; colour may reinforce it without changing the style key. Record an exception for an accepted reference rather than silently restyling it. [review]
- **A5 Avoid unrelated objects.** Do not route through unrelated process nodes, icons or text; default to 8 px clearance. A connector may cross its containing region's boundary when linking an inside element to an outside element. Declare that boundary crossing and keep it clear of the region's label; it is not a connection to the region itself. Intentional endpoints are exempt from clearance. [review]
- **A6 Keep distinct paths distinct.** Default to 8 px between separate parallel routes. Do not share a segment unless A10 permits a meaningful shared trunk. Declare endpoint approaches and intended branch/merge junctions as exceptions to spacing. [review]
- **A7 Prefer simple routes.** Prefer straight or orthogonal routes with few bends and optional rounded corners. Two bends, or three in an outer channel, are review targets, not hard failures. Additional bends or a deliberate curve are acceptable when they better preserve meaning, clearance or an accepted composition; record why. [review]
- **A8 Use consistent attachment points.** For ordinary boxes, prefer perpendicular side connections, normally at the midpoint and facing the flow. Multiple connections on one side may use evenly spaced ports. Use declared ports or appropriate boundaries for other shapes and illustrations; do not force every connection onto a midpoint. [review]
- **A9 Connect visible endpoints.** For boundary-attached connectors, place the visible arrowhead tip on the declared target boundary within 2 px and start the visible line on the source boundary. Account for marker geometry and stroke width. Do not stop short or bury the tip. Record deliberate gaps or non-box attachment conventions. [review]
- **A10 Show real branches and merges.** Use a shared trunk only when the agreed relationship actually branches or merges. Mark its junction clearly with a dot or an unambiguous T; a non-junction crossing has neither. Keep independent flows separate, even when they enter the same process. Never invent a merge to simplify routing. [look]
- **A11 Keep the main flow readable.** Prefer left-to-right or top-to-bottom flow where sequence matters. Route feedback around the outside where practical; preserve all necessary feedback relationships. Other topologies may use a different declared reading order. [look]
- **A12 Reserve two-way arrows for two-way relationships.** Otherwise use one arrow or two separately identified one-way arrows. [look]
- **A13 Give styles consistent meanings.** Use a consistent ordinary-flow style. Explain meaningful variations once in a key and reuse them across views. Check against a declared style-to-meaning map; distinct SVG styles alone cannot establish semantic consistency. Do not invent meaning for purely presentational variation. [review]
- **A14 Give long routes open channels.** Consider placing related elements closer without changing meaningful order/grouping. Otherwise route between groups or around the outside. If no clear route exists, use uniquely matched continuation labels at both ends, preserving direction and traceability. [look]

## Layout, alignment and labels

- **L1 Align comparable items.** Within declared rows or columns of comparable boxes, align centres or edges within 2 px. Do not impose a global grid on unrelated groups, annotations or illustrations. [review]
- **L2 Space within groups consistently.** Prefer equal gaps between comparable consecutive stages within a group. Use larger separation between groups where grouping carries meaning. Preserve declared time/distance encodings and intentional unequal spacing. [review]
- **L3 Fit boxes to content.** Give comparable items equal size where content allows. Fit containers to text at the destination size; do not shrink labels below that destination's requirements to force a fit. Declared text bounds can be measured; equal sizing remains contextual. [review]
- **L4 Keep content inside the canvas.** Default to 12 px outer clearance for meaningful content and no unintended clipping. Background fills or deliberate bleeds may reach the edge; record exceptions. [measure]
- **L5 Balance density.** Avoid a crowded region beside unused space when redistribution would help comprehension. Preserve intentional whitespace and meaningful grouping. [look]
- **L6 Match reading order to meaning.** Number stages when sequence matters, without implying a sequence among parallel or unordered elements. [look]
- **T1 Prefer horizontal labels.** Flag rotation for review; retain justified destination-specific or accepted-layout exceptions. [review]
- **T2 Keep lines out of text.** Put connector labels beside the line or on a background that visibly interrupts it. Measure visible rendered overlap, accounting for masking/backgrounds, rather than treating a hidden path as a collision. [measure]
- **T3 Make label ownership unambiguous.** Place labels near what they name; when proximity is ambiguous, use placement, grouping or a leader line. Nearest-object distance can flag a problem only with declared label ownership; it is not an absolute acceptance rule. [review]
- **T4 Check text at the destination size.** Use the destination's actual type-size requirements where supplied. Without them, use the plugin fallback of 8 pt for print or 11 CSS px for screen as a floor, not a guarantee of readability. Record overrides and inspect at actual size, including phone presentation where applicable. Keep terminology and capitalisation consistent. [review]

After a revision, re-check moved elements, their connected routes and labels, and nearby elements affected by the change. If scaling, typography or global styles change, re-check the whole affected view and its exports.

## Hierarchy and grouping
Make the main explanation visually dominant through scale, position, contrast and whitespace. Group related elements by proximity and common region. Maintain alignment and consistent spacing. Important distinctions should not depend on color alone. Do not give setup, footnotes and the central action identical prominence by default.
NN/g's visual design principles: https://media.nngroup.com/media/articles/attachments/Principles_Visual_Design-A4.pdf
Proximity: https://www.nngroup.com/articles/gestalt-proximity/
Hierarchy: https://www.nngroup.com/articles/visual-hierarchy-ux-definition/

## Typography, illustrations and shared objects
Use a restrained type hierarchy, readable line lengths and enough clearance around labels. Measure rendered text; fit its container rather than shrinking until it fits. Keep the same role, color and illustration for the same object in different views. Use a coherent non-logo illustration family and recognizable subject-specific images; retain authentic logos and provenance. Decoration must not change factual meaning.

## Audience and medium
Select content and encodings for the audience and medium. An overview must work before interaction. A large figure scaled down may be technically unclipped but unreadable. Inspect at intended size, plan usable enlarged viewing or section crops, and distinguish file quality from delivery success.
Rougier, Droettboom and Bourne, “Ten Simple Rules for Better Figures” (2014): https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833
This paper gives general scientific-figure guidance, not a workflow-diagram standard.

## Sources and scope

The rule IDs and operational wording are this plugin's synthesis. The following sources were inspected on 11 November 2026; the mapping identifies adapted guidance, not certification that the plugin implements a standard. Keep the illustrated TransplantID style; do not import another source's aesthetic wholesale.

| Source | Rules informed | Scope and exceptions |
|---|---|---|
| [SBGN Process Description v1.3, Chapter 4, printed pp. 47–50](https://sbgn.github.io/sbgn/downloads/proposals/PD_L1V3.pdf) | A3–A6, T1–T3 | Sections 4.2.1–4.2.8 address overlaps and labels; 4.3.1 allows necessary container-boundary crossings; 4.3.2–4.3.3 recommend horizontal/nearby labels and fewer crossings; 4.4 suggests near-right-angle crossings. Historical version, not asserted to be current. Adapt geometry guidance, not biological glyph semantics or its aspect-ratio suggestion. |
| [Camunda BPMN modeling styles](https://camunda.com/bpmn/examples/) | A3, L3, L6; activity/decision labels | Avoid crossing flows; label activities consistently, phrase decisions as questions, and size comparable tasks consistently. Apply where a process diagram benefits; do not impose BPMN symbols on every explanatory figure. |
| [draw.io connector guidance](https://drawio-app.com/blog/connector-styles-and-animations-in-draw-io/) | A4 | Line jumps distinguish crossings from junctions. A drawing technique, not a requirement of every notation. |
| [W3C use of colour, SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) | A4, A13; hierarchy | Do not rely on hue alone for meaningful distinctions. The gap/bridge rule is this plugin's chosen way to clarify crossings. |
| [W3C text contrast, SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), and [non-text contrast, SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast) | Typography and meaningful graphical cues | For web figures claiming AA: ordinary text 4.5:1; large text (at least 18 pt, or 14 pt bold) 3:1; graphical parts needed for understanding generally 3:1 against adjacent colours. Apply the criteria's exceptions, including relevant decorative/essential content exceptions; not every pastel fill requires 3:1. Record what was measured and visually assess which components are essential. These checks alone do not establish full WCAG conformance. |
| [Nature figure specifications](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) | T4; editable exports | A destination-specific example: ordinary figure text 5–7 pt and editable vector artwork. Use the actual target publication's guidance; this is not a universal font-size or illustration-style rule. |

The yWorks, NN/g and Rougier references above remain background for composition and hierarchy. Wong's *Points of View* columns are related reading, not verified support for these rules: [Arrows](https://doi.org/10.1038/nmeth.1676), [Layout](https://doi.org/10.1038/nmeth.1711), [The overview figure](https://doi.org/10.1038/nmeth0511-365), and [Gestalt principles](https://doi.org/10.1038/nmeth1110-863).
