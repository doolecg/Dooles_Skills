---
name: isometric-pixel-art
description: "Isometric pixel art for games: 2:1 pixel lines, tile and block sizes, tall blocks with walls and cut-away roofs, hard pixel shadows, limited palettes, consistent light, outlines, dense pixel UI at 1x, sprite sheet and atlas export. Use when drawing, generating or reviewing isometric tiles, buildings, base art, program icons or UI pixel art, or checking that assets match the project's art decisions."
---

# Isometric pixel art

Follow the project's art decisions first (tile size, palette, UI pixel scale, fonts). These are defaults to fall back on when it says nothing.

## Geometry
- Use 2:1 pixel isometric: lines run 2 pixels across for every 1 down. Every edge on the grid then repeats cleanly with no jaggies.
- Pick one tile footprint and never mix: for example 32x16 or 64x32. A "tall block" is the footprint plus a wall height in whole multiples of the pixel unit.
- Vertical edges are exactly vertical. Do not rotate a finished drawing; draw on the grid.
- Anchor every sprite at its footprint's bottom-centre and record that offset in the atlas data, so placement and depth sorting use one point.

## Light and shading
- One fixed light direction for the whole game (for example top-left): top face lightest, left face mid, right face darkest.
- Hard pixel shadows: a solid darker silhouette offset by whole pixels. No soft edges, no transparency gradients, no blur.
- Anti-aliasing is off. Where an edge needs softening use a one-pixel dither or a mid colour, sparingly.

## Palette
- A small shared palette (16 to 32 colours) for all world art; ramps of 3 to 5 steps per material with a slight hue shift (shadows cooler, highlights warmer).
- Accent colours are reserved for meaning (for example a single orange for the main action). Do not spend them on decoration.
- Glow is drawn as lighter pixels around a light source, not a blur.

## Buildings and rooms
- Walls are tall blocks: two visible faces plus a top. Doors and windows are dark insets with a one-pixel highlight.
- Cut-away rooms: draw the back walls full height, the front walls dropped or removed, and the roof as a separate sprite so the game can hide it.
- Keep silhouettes readable at 1x: an object must be recognisable from its outline in 16 to 32 pixels.

## Dense pixel UI
- UI art pixel = 1 screen pixel at the default 1x scale; icons 24x24 or 32x32; frames carry detail but not noise.
- Pixel fonts only at their native sizes and integer multiples; check them at 1x before approving.
- Use the same palette ramps as the world so the interface and the game feel like one machine.

## Export
- One PNG atlas per theme with 1px transparent padding (extrude edge pixels by 1px for tilemaps) and a JSON data file of frames, anchors and animation names.
- Names: `thing_state_direction_frame` in snake case; one source file per object so a change touches one asset.
- Keep source files (Aseprite or similar) in the repo's art folder and export from them, never hand-edit the PNG atlas.

## Review checklist
1. All edges follow 2:1 lines; no stray half-steps.
2. Light direction identical across assets.
3. Palette only from the shared ramps; no new colours without reason.
4. Sprite anchor and footprint match the tile size.
5. Looks right at 1x and at the largest zoom; no sub-pixel scaling.
6. No blur, bloom or soft shadows anywhere.
