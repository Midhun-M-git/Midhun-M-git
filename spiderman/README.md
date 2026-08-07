# 🕸️ Marvel Spider-Man GitHub Activity SVG Animation

This directory contains the self-contained, high-detail Marvel Spider-Man vector animation swinging across a real-time GitHub contribution graph grid.

## 📁 Files Included:
- `spiderman-activity.svg`: The standalone, self-contained SVG animation file.
- `preview.html`: Local preview file to view the high-resolution animation in full size.
- `README.md`: Embedding documentation and instructions.

## 🚀 How to Embed in your GitHub Profile (`README.md`):

Add the following HTML snippet to your main GitHub repository `README.md`:

```html
<div align="center">
  <!-- Marvel Spider-Man Swinging Activity Graph -->
  <img src="spiderman/spiderman-activity.svg?v=20260807_PRO" alt="Spider-Man swinging contribution calendar" width="100%" style="max-width: 880px;" />
</div>
```

## ✨ Technical Highlights:
1. **10+ Modular Articulated SVG Groups**:
   - `#spiderman`, `#head`, `#left-eye`, `#right-eye`, `#torso`, `#chest-emblem`, `#web-shooting-arm`, `#left-hand`, `#right-arm`, `#left-leg`, `#right-leg`.
2. **True Pendulum Momentum Physics**:
   - Curved web line shooting from Spider-Man's wrist (`🤟` gesture) attaching to anchor points above the contribution grid.
   - Smooth `cubic-bezier(0.42, 0, 0.58, 1)` acceleration during kinetic drops and deceleration at swing apexes.
3. **100% Native SVG Paths**:
   - Built entirely with native `<path>`, `<g>`, `<defs>`, and `<linearGradient>` elements. Zero external dependencies or image formats (`.png`/`.jpg`).
