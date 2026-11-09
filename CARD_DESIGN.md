# Flux Point: Zimu — Card Studio

Open [`design/card-studio.html`](design/card-studio.html) in a browser to edit
the basic card fields and see a live preview. The editor works offline and
requires no packages or external assets.

Choose any of the 100 registry cards to load its stats, ability, and an
editable, original appearance description. The italic description is a visual
prompt, not a gameplay effect. Vanilla cards leave the ability area blank.
Changes in the editor are temporary and do not modify the registry.

Appearance descriptions live in `design/appearances.json`. After changing
those descriptions or the engine registry, run `python design/build_catalog.py`
to regenerate `design/card-catalog.js` for the offline studio.

## Visual direction

The template uses a dark, technical frame with one bright rank accent, short
labels, a single artwork window, and separated rules text and stats. The
intersecting orbit mark gives Flux Point a distinct visual signature while
keeping the hierarchy quick to read. The accent changes by Zimu rank: Core
(emerald), Militia (amber), Mythic (crimson), and Apex (volcanic orange).

## Print geometry

The preview canvas is the full bleed at 816 × 1116 px (2.72" × 3.72" at
300 DPI). The cut line is inset 33 px on every side, producing 750 × 1050 px
(2.50" × 3.50"). The centered safe zone is 675 × 975 px (2.25" × 3.25");
all text and bottom-left ATK / HP stats sit inside it. The editor's amber
outline marks the cut line, and its mint outline marks the safe zone. Toggle
the guides off to inspect the clean card face.

Use the browser's print command from the Card Studio page for a single-card
output. Print CSS sets the page and card to the full 2.72" × 3.72" canvas and
hides the guides.

## First iteration limits

The art window currently contains an original abstract placeholder rather
than final character art; the appearance descriptions are not illustrations.
The studio is a single-card layout prototype, not a
48-card deck builder or print-sheet imposition tool. Confirm printer profile,
color workflow, and final imagery before commercial printing.
