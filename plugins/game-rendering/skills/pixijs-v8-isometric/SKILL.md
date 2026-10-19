---
name: pixijs-v8-isometric
description: "PixiJS v8 for isometric 2.5D pixel-art game views: Application init, tilemaps with @pixi/tilemap, hex or square grids projected to isometric, depth sorting, nearest-neighbour pixel scaling, camera zoom and pan, render on demand, pixel glow with pixi-filters, sprite atlases, React integration. Use when editing a PixiJS canvas, base/map view, tilemap or sprite code, or when pixels look blurry, sorting is wrong, or the canvas redraws constantly."
---

# PixiJS v8, isometric pixel art

Read the project's own rendering decisions first (grid type, tile size, zoom steps, what is cosmetic). Verify API details against the current PixiJS v8 docs; v8 differs from v7 (async init, new texture source API, `@pixi/tilemap` v5 for v8).

## Setup
```ts
const app = new Application()
await app.init({ canvas, resizeTo: host, background: 0x000000, antialias: false, roundPixels: true, resolution: 1, autoDensity: false })
```
- `await app.init(...)` is required in v8; do not use the v7 constructor options.
- No antialiasing, `roundPixels: true`, integer positions, so pixel art stays crisp.
- Load art with `Assets.load`; set `texture.source.scaleMode = 'nearest'` on every pixel texture (or load atlases once and set it there).

## Pixel-perfect scaling
- Zoom in integer steps only (for example 0.5x, 1x, 2x, 3x, 4x) as the project defines; scale a single world container, not each sprite.
- Keep camera positions on whole pixels after scaling.
- Never use blur, bloom or smooth filters on the pixel layers.

## Grid to isometric
- Keep game logic in grid coordinates (axial for hex, column/row for square). Project to screen in one function and back in another; never mix.
- Square grid, 2:1 pixel isometric: `x = (c - r) * tileW / 2`, `y = (c + r) * tileH / 2`, with `tileH = tileW / 2`.
- Hex grid: convert axial to flat pixel positions with the hex formulas, then apply the project's isometric squash/rotation in the same single function. Match the project's decision exactly; test the round trip `screen -> grid -> screen`.
- Hit testing: invert the projection from the pointer position, then check the grid cell; do not rely on sprite bounds for tall objects.

## Depth sorting
- Sort by the projected ground position (for square grids `c + r`, then height), not by sprite bottom. Use a `Container` with `sortableChildren = true` and set `zIndex`, or re-order explicitly when objects change cell.
- Tall blocks and walls: anchor sprites at the bottom-centre of their footprint so sorting and placement use one point.
- Cut-away roofs: render the roof as its own sprite per room and hide or fade it (alpha steps, no blur) when the room is selected.

## Tilemaps
- `CompositeTilemap` from `@pixi/tilemap`: call `clear()` then `tile(texture, x, y)` per tile when the map changes; do not rebuild every frame.
- Keep all tile art in one atlas; pad each frame by 1px and extrude edges to stop seams.
- One tilemap per layer (ground, floor decor); objects with depth live in the sorted container.

## Render on demand
For views that do not animate every frame (a base map), stop the ticker and render only after a change:
```ts
app.ticker.stop()
const redraw = () => app.render()
```
Call `redraw()` after a state change, zoom, pan or resize. Run the ticker only while something animates (day/night fade, selection pulse), then stop it again.

## Glow and effects
- Pixel glow: draw it into the sprite art or add a small additive sprite. If a filter is unavoidable, use a `pixi-filters` glow with low quality and small strength, keep it to a few objects, and check that edges stay hard.
- Hard pixel shadows: a darker copy of the silhouette, offset in whole pixels, no soft edge.

## With React
- Create the `Application` once in an effect, destroy it in the cleanup (`app.destroy(true)`), and guard against React strict-mode double mount (an unmounted flag checked after the awaited init).
- Keep game state outside the canvas; React sends view-model updates in, canvas events (pick, hover) come out as callbacks. Never put the canvas in React state.
- Resize with `resizeTo` the host element, then call the redraw.

## Pitfalls
- Blurry sprites: `scaleMode` not `nearest`, non-integer zoom, or a CSS-scaled canvas.
- Seams between tiles: no padding in the atlas, or fractional positions.
- Jitter on camera pan: positions not rounded after scale.
- Memory growth: textures and containers not destroyed on teardown; call `destroy({ children: true })` on removed containers.
- Using v7 examples (`new PIXI.Application({...})` synchronous, `PIXI.Loader`): wrong for v8.
