# Design principles and sources
These are practical applications of established guidance, not rigid aesthetic rules. Preserve the user's preferred information-rich TransplantID style. Diagnose specific communication problems; do not prescribe minimalism, remove essential content or redesign accepted figures just because a source uses another visual style.

## Composition before decoration
Choose an orientation and reading order that explain the relationships. Put sequential steps in aligned stages; give equivalent inputs equal weight; put exceptions beside the relevant step. Reserve space for branch/merge channels before placing boxes. Minimize unnecessary crossings, bends and reversals. Use clear junctions and arrowheads; proximity alone must not imply a relationship.

yWorks describes layered placement and crossing reduction: https://www.yworks.com/pages/layered-graph-layout.html
Its orthogonal router describes routing while preserving node positions: https://yed.yworks.com/support/manual/layout/router_orthogonal.html
These references do not require purchasing or using yFiles; apply the principles with tools suitable to the task. Automatic layout still needs inspection and can mishandle labels or constraints.

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
