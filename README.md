# Vague Vision Match

This project implements a **coarse, ternary image abstraction** for fast and vague image matching.
It is designed to answer one question only:

> “Does this image roughly look like the other one?”

It is **not** intended for reconstruction, precise recognition, or invariance-heavy vision tasks.

---

## What it does

- Converts an image into a **3-state representation** (LOW / MID / HIGH)
- Uses global thresholds derived from the image data
- Compares two ternary maps to produce a **similarity score**
- Triggers a match when similarity exceeds a chosen threshold (≈81% in testing)

The output is a **rough perceptual match**, not a pixel-accurate comparison.

---

## Motivation

Inspired by how human vision performs **quick, low-effort recognition**:
- A brief glance
- No focus on fine detail
- Approximate confirmation is enough

This project explores that idea in software using extreme abstraction.

---

## How it works (high level)

1. Image → luminance (or RGB sum)
2. Values mapped into **three discrete states**
3. Image reduced to a ternary grid
4. Two grids compared using a simple similarity metric
5. Match triggered if similarity ≥ threshold

The abstraction is intentional and lossy.

---

## Results

- Empirically, a similarity threshold of **~81%** produced stable “vague match” behavior
- Works well for rough structure comparison
- Fails gracefully when images differ significantly

---

## Limitations (by design)

- Sensitive to rotation
- Sensitive to lighting changes
- Sensitive to scale and translation
- Not invariant
- Not suitable for fine-grained recognition

These are accepted constraints given the scope.

---

## Scope

This was a **6–8 hour experimental project**.
It is a finished experiment, not a production system.

---

## Possible extensions (not implemented)

- Rotation / scale normalization
- Local contrast instead of global thresholds
- Block-wise comparison
- Dithering or multi-level abstraction

---

## License

MIT
