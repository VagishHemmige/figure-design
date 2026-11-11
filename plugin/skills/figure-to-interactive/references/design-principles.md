# Design principles and sources
These are practical applications of established guidance, not rigid aesthetic rules. Preserve the user's preferred information-rich TransplantID style. Diagnose specific communication problems; do not prescribe minimalism, remove essential content or redesign accepted figures just because a source uses another visual style.

## Composition before decoration
Choose an orientation and reading order that explain the relationships. Put sequential steps in aligned stages; give equivalent inputs equal weight; put exceptions beside the relevant step. Reserve space for branch/merge channels before placing boxes. Minimize unnecessary crossings, bends and reversals. Use clear junctions and arrowheads; proximity alone must not imply a relationship.

yWorks describes layered placement and crossing reduction: https://www.yworks.com/pages/layered-graph-layout.html
Its orthogonal router describes routing while preserving node positions: https://yed.yworks.com/support/manual/layout/router_orthogonal.html
These references do not require purchasing or using yFiles; apply the principles with tools suitable to the task. Automatic layout still needs inspection and can mishandle labels or constraints.

## Connectors and arrows
Apply these when drawing and again after every revision that moves a box or a line. Each rule has an ID so a check or review finding can cite it. [code] marks rules a script can check on the rendered SVG; [look] marks rules that need visual judgment. Distances are at final size and are this plugin's defaults, not sourced values; change them per figure when there's a reason.

- **A1 One arrow, one relationship.** Each arrow shows one real relationship (sequence, data flow or dependency) and points the way the thing moves. Do not add arrows only to lead the eye. [look]
- **A2 Label it on the arrow.** If the meaning isn't obvious from the two ends, put a short label beside a straight segment, near its middle, not in a legend. [look]
- **A3 Remove crossings by placement first.** Reorder boxes within their row or column before rerouting lines. Aim for zero crossings. [code: count crossings]
- **A4 Unavoidable crossings are clearly crossings.** Cross at a right angle, away from labels, junctions and arrowheads, so it can't be read as a junction: either leave a small gap in the line passing underneath, or give the two lines clearly different colours, as the TransplantID reference does. [code: angle; look: gap or colour]
- **A5 Never through a box or text.** A line passes no box, icon or text it doesn't connect to, and keeps at least 8 px from them. [code]
- **A6 No overlapping or hugging lines.** Parallel lines stay at least 8 px apart. Two arrows never share a path unless they deliberately merge into one trunk (A10). [code]
- **A7 Straight or orthogonal, with few bends.** Use straight lines, or horizontal and vertical segments with small rounded corners, and at most two bends per arrow; a route along an outer channel (A14) may take three. Needing more usually means a box is in the wrong place. [code: count bends]
- **A8 Consistent attachment.** Arrows meet a box at a side, perpendicular to it, normally at its midpoint. Incoming flow enters the side facing the previous step, and outgoing flow leaves the side facing the next. Several arrows on one side are spaced evenly. [code]
- **A9 Ends touch.** The arrowhead tip touches the target's edge, within 2 px, and the line starts at the source's edge. It neither stops short nor disappears inside the box. [code]
- **A10 Branches and merges are visible.** Fan out from one trunk and merge into one, with a clear junction (a dot or a T). A dot means "joined"; a plain crossing (A4) never has one. [code: junctions; look]
- **A11 One direction for the main flow.** Keep the main path left to right or top to bottom. Return or feedback arrows are few and routed around the outside, so they read as going back. [look]
- **A12 Two-way arrows only for two-way relationships,** such as a sync. Otherwise draw one arrow, or two one-way arrows. [look]
- **A13 A line style has one meaning.** One weight and arrowhead for ordinary flow. A different style (dashed, dotted or another colour) only for a different meaning, such as planned, optional or pending. Explain it once in a key, and use it the same way in every view. [code: styles used vs key]
- **A14 Long routes use open channels.** If an arrow must cross most of the figure, first try moving the target closer. If the long line stays, run it along an open channel between groups or around the outside, crossing as few lines as possible (A3, A4). If no clear channel exists, use a labelled connector at both ends ("to 6", "from 3") instead. [look]

## Layout, alignment and labels
- **L1 Align to a grid.** Boxes in the same row share a centre line, and boxes in the same column share a centre or an edge, within 2 px. [code]
- **L2 Consistent spacing.** Equal gaps between consecutive stages. Gaps between groups are clearly larger than gaps inside a group, so grouping reads before the arrows do. [code]
- **L3 Size boxes to their content.** Items at the same level get the same size where the content allows. Size the box to the text at final size; do not shrink the text to fit the box. [code: text fits]
- **L4 Margins.** Nothing sits within 12 px of the canvas edge, and nothing is clipped. [code]
- **L5 Balance.** No crowded region next to a large empty one. Redistribute before adding routing. [look]
- **L6 Reading order follows the flow.** Number the stages when order matters, as the house style does. [look]
- **T1 Horizontal text.** Avoid rotated or vertical labels. [code]
- **T2 No line through text.** Arrow labels sit beside the line or on a background that interrupts it. [code]
- **T3 Labels sit closest to what they name,** nearer to it than to anything else. [code]
- **T4 Readable at final size.** Text is at least the destination's minimum size (8 pt for print, about 11 px on screen), with the same terms and capitalisation throughout. [code]

When a revision moves anything, re-check every rule above for the boxes and lines it moved and the ones next to them, not only the problem being fixed.

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
This paper is broader scientific-figure guidance, not a workflow-diagram standard. The checks below are this plugin's operational synthesis rather than verbatim requirements from any single source.
The connector, layout and label rules (A, L and T) are this plugin's own synthesis: they restate the principles above and the lessons in design-lessons.md as checkable rules, add common diagramming conventions, and were adjusted after checking them against the TransplantID reference. They are not taken from a published standard, and the rule IDs and distances are this plugin's defaults.
Related reading, not yet checked against these rules: Bang Wong's *Points of View* columns in *Nature Methods*, especially "Points of view: arrows" (2011), https://doi.org/10.1038/nmeth.1676; "Layout" (2011), https://doi.org/10.1038/nmeth.1711; "Points of view: the overview figure" (2011), https://doi.org/10.1038/nmeth0511-365; and "Points of view: gestalt principles (part 1)" (2010), https://doi.org/10.1038/nmeth1110-863.
