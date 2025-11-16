# Marp Core Examples

This directory contains example Markdown files demonstrating various Marp features.

## Files

- **[math-typesetting.md](math-typesetting.md)** - Demonstrates inline and block math rendering with MathJax
- **[code-block-autoscaling.md](code-block-autoscaling.md)** - Shows how code blocks automatically scale to fit slides
- **[katex-autoscaling.md](katex-autoscaling.md)** - Demonstrates KaTeX math block auto-scaling

## Generating Screenshots

To generate screenshots for documentation:

1. Install [Marp CLI](https://github.com/marp-team/marp-cli):
   ```bash
   npm install -g @marp-team/marp-cli
   ```

2. Convert to HTML or PDF:
   ```bash
   marp examples/math-typesetting.md -o output.html
   # or
   marp examples/math-typesetting.md -o output.pdf
   ```

3. Take screenshots of the rendered slides for use in documentation

## Using These Examples

You can use these examples to:
- Test Marp features
- Create documentation screenshots
- Learn Marp syntax
- Verify theme compatibility
