# CLAUDE.md - AI Assistant Guide for @marp-team/marp-core

This document provides comprehensive guidance for AI assistants working on the Marp Core codebase.

## Project Overview

**@marp-team/marp-core** (v4.2.0) is the core converter library for [Marp](https://marp.app), a Markdown presentation ecosystem. It extends the [Marpit](https://github.com/marp-team/marpit) framework to convert Markdown into presentation slides with advanced features.

- **Language:** TypeScript
- **License:** MIT
- **Node.js:** 18+ required
- **Package Manager:** npm
- **Test Coverage:** 95% minimum required

### Key Features

1. **Markdown Presentation Conversion** - Converts Markdown to HTML/CSS slides
2. **Math Typesetting** - MathJax and KaTeX support (`$...$`, `$$...$$`)
3. **Emoji Support** - Shortcodes (`:smile:`) and Unicode → Twemoji SVG
4. **Syntax Highlighting** - Code blocks via highlight.js
5. **Auto-scaling** - Fitting headers (`<!-- fit -->`) and auto-shrinking blocks
6. **Built-in Themes** - Default (GitHub-style), Gaia, Uncover
7. **Size Directives** - `<!-- size: 4:3 -->` for aspect ratio control
8. **HTML Sanitization** - XSS protection with configurable allowlists

## Repository Structure

```
/home/user/marp-core/
├── src/                        # TypeScript source (~1,453 lines)
│   ├── marp.ts                 # Main Marp class (extends Marpit)
│   ├── browser.ts              # Browser runtime utilities
│   ├── auto-scaling/           # Auto-scaling features
│   ├── custom-elements/        # Web Components for scaling
│   ├── emoji/                  # Emoji conversion
│   ├── html/                   # HTML sanitization & allowlist
│   ├── math/                   # MathJax & KaTeX support
│   ├── script/                 # Script injection
│   ├── size/                   # Size directive
│   └── slug/                   # Heading ID generation
│
├── themes/                     # SCSS themes (default, gaia, uncover)
├── test/                       # Jest tests (~1,485 lines)
├── scripts/                    # Build utilities
├── sandbox/                    # Local testing (gitignored)
│
├── lib/                        # Build output (gitignored)
├── types/                      # Type definitions output (gitignored)
│
└── [17 config files at root]
```

### Key Source Files

- `src/marp.ts:1-463` - Main Marp class with constructor options
- `src/html/allowlist.ts:1-184` - Default HTML element allowlist
- `src/math/math.ts:1-234` - Math typesetting coordinator
- `src/auto-scaling/fitting-header.ts:1-123` - Fitting header implementation
- `src/custom-elements/postcss-plugin.ts:1-89` - CSS selector transformation
- `src/emoji/emoji.ts:1-267` - Emoji shortcode & Unicode conversion

## Development Workflow

### Initial Setup

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Run tests
npm test

# Run tests with coverage
npm run test:coverage
```

### Development Commands

```bash
# Watch mode (auto-rebuild on changes)
npm run watch

# Sandbox mode (watch + live reload with marp-cli)
npm run sandbox

# Type checking (no emit)
npm run check:ts

# Generate type definitions
npm run types

# Linting
npm run lint:js          # ESLint
npm run lint:css         # Stylelint for SCSS

# Formatting
npm run check:format     # Check with Prettier
npm run format:write     # Auto-format with Prettier
```

### Sandbox Workflow

The sandbox provides live development with auto-reload:

```bash
npm run sandbox
```

This runs:
1. Rollup in watch mode (rebuilds on changes)
2. Nodemon monitoring `lib/` directory
3. `@marp-team/marp-cli` executing test Markdown

Place test `.md` files in the `sandbox/` directory to experiment.

## Build System

### Rollup Configuration

**File:** `rollup.config.mjs`

**Three Build Targets:**

1. **Browser Helper Script** (`lib/browser.js`)
   - Format: IIFE (inline execution)
   - Purpose: Polyfills for browser environment
   - Minified in production

2. **Browser CJS Bundle** (`lib/browser.cjs.js`)
   - Format: CommonJS
   - Entry: `src/browser.ts`
   - For bundlers (webpack, etc.)

3. **Main Package** (`lib/marp.js`)
   - Format: CommonJS
   - Entry: `src/marp.ts`
   - All dependencies externalized

### PostCSS Processing Pipeline

SCSS files are processed through:

1. **Sass** - Compilation with package importer
2. **Custom Optimizer** (`scripts/postcss-optimize-default-theme.mjs`) - Converts `@media (prefers-color-scheme)` to `light-dark()` for default theme
3. **postcss-url** - Inline SVG assets as base64
4. **Autoprefixer** - Vendor prefixes
5. **cssnano** - Minification (preserves whitespace)

### Important Build Notes

- TypeScript compilation happens via Rollup (`@rollup/plugin-typescript`)
- SCSS imported directly in TypeScript files (`import css from './style.scss'`)
- CSS exported as strings via `css()` function in plugins
- Browser scripts inlined into main bundle or served via CDN

## Testing Approach

### Jest Configuration

**File:** `jest.config.mjs`

- **Framework:** Jest v30.2.0
- **Environment:** Node.js (jsdom for browser tests)
- **Coverage:** 95% minimum line coverage required
- **Reporter:** JUnit XML for CI, text for local

### Test Organization

```
test/
├── marp.ts                     # Main class tests (1,485 lines)
├── browser.ts                  # Browser functionality
├── size/size.ts                # Size directive tests
├── math/katex.ts               # KaTeX tests
├── custom-elements/browser.ts  # Custom elements
├── __snapshots__/              # Jest snapshots
└── _transformers/
    └── sass.js                 # SCSS transformer
```

### Testing Patterns

```typescript
// Use cheerio for DOM assertions
import cheerio from 'cheerio'

const { html } = marp.render('# Hello')
const $ = cheerio.load(html)
expect($('h1').text()).toBe('Hello')

// Snapshot testing for complex outputs
expect(html).toMatchSnapshot()

// Context blocks for organization
import { context } from 'jest-plugin-context'

context('with option enabled', () => {
  // Tests here
})
```

### Custom Transformers

- **TypeScript:** `ts-jest` with `isolatedModules: true`
- **SCSS:** Custom transformer in `test/_transformers/sass.js`
  - Compiles SCSS to CSS
  - Returns as ES module default export

### Running Tests

```bash
npm test                    # Run all tests
npm run test:coverage       # With coverage report
npm test -- --watch        # Watch mode
npm test -- marp.ts        # Specific test file
```

## Plugin Architecture

### Core Pattern

All features are **markdown-it plugins** wrapped with Marpit's plugin helper:

```typescript
import marpitPlugin from '@marp-team/marpit/plugin'

export const markdown = marpitPlugin((md) => {
  // Add parsing rules
  md.core.ruler.push('feature_name', coreRule)

  // Add rendering rules
  md.renderer.rules.feature_token = renderRule

  // Or modify existing rules
  const originalRule = md.renderer.rules.heading_open
  md.renderer.rules.heading_open = (tokens, idx, options, env, self) => {
    // Custom logic
    return originalRule(tokens, idx, options, env, self)
  }
})

// Optional: Export CSS
export const css = () => import('./styles.scss')
```

### Plugin Registration

In `src/marp.ts:1-463`, plugins are registered:

```typescript
// Enable markdown-it plugins
this.markdown
  .use(markdownItEmoji)
  .use(htmlPlugin.markdown)
  .use(emojiPlugin.markdown)
  .use(mathPlugin.markdown)
  .use(autoScalingPlugin.markdown)
  // ... etc
```

### Available Plugins

1. **HTML Plugin** (`html/html.ts`)
   - XSS filtering with allowlist
   - Configurable via `html` option
   - Default allowlist in `html/allowlist.ts`

2. **Emoji Plugin** (`emoji/emoji.ts`)
   - Shortcode: `:smile:` → 😄 or Twemoji
   - Unicode: 😄 → Twemoji SVG
   - Configurable via `emoji` option

3. **Math Plugin** (`math/math.ts`)
   - Inline: `$E = mc^2$`
   - Block: `$$...$$`
   - Renderers: MathJax (default) or KaTeX
   - Per-doc selection: `<!-- math: katex -->`

4. **Auto-scaling Plugin** (`auto-scaling/`)
   - Fitting headers: `# <!-- fit --> Title`
   - Code block auto-shrink
   - KaTeX block auto-shrink

5. **Size Plugin** (`size/size.ts`)
   - Directive: `<!-- size: 4:3 -->`
   - Reads `@size` metadata from themes

6. **Slug Plugin** (`slug/slug.ts`)
   - Auto-generates heading IDs
   - GitHub-compatible slugification
   - Duplicate handling: `-N` suffix

7. **Script Plugin** (`script/script.ts`)
   - Injects browser helper
   - Options: inline or CDN
   - CSP-compatible with `nonce`

## Custom Elements System

### Purpose

Enable auto-scaling without breaking theme CSS selectors.

### Elements

- `marp-h1` through `marp-h6` - Scaled headings
- `marp-pre` - Scaled code blocks
- `marp-span` - Scaled inline math

### PostCSS Transformation

**File:** `src/custom-elements/postcss-plugin.ts`

Transforms theme CSS to support both native and custom elements:

```css
/* Input */
h1 { color: red; }

/* Output */
:is(h1, marp-h1) { color: red; }
```

### Browser Implementation

**File:** `src/custom-elements/browser/`

- Shadow DOM for isolated scaling
- `::part(auto-scaling)` for theme styling
- CSS custom properties for dimensions
- Automatic resize observer

### Theme Integration

Themes can target custom elements:

```scss
// Applies to both <h1> and <marp-h1>
h1 {
  color: var(--heading-color);
}

// Target the scaling wrapper specifically
marp-h1::part(auto-scaling) {
  display: flex;
  align-items: center;
}
```

## Theme System

### Theme Structure

Built-in themes in `themes/`:

```
themes/
├── README.md              # Theme documentation
├── example.md             # Visual showcase
├── default.scss           # GitHub Markdown style
├── gaia.scss              # Classic presentation
├── uncover.scss           # Minimal modern
└── assets/
    └── uncover-quote.svg
```

### Theme Metadata

CSS comment metadata defines theme capabilities:

```css
/**
 * @theme theme-name
 * @auto-scaling true
 * @size 16:9 1280px 720px
 * @size 4:3 960px 720px
 */

section {
  /* Theme styles */
}
```

### Required Features

All built-in themes MUST support:

1. **`invert` class** - Inverted color scheme (usually dark mode)
2. **Size presets** - At least `16:9` and `4:3`
3. **Auto-scaling** - Optional but recommended

### Theme Loading

In `src/marp.ts:1-463`:

```typescript
import defaultTheme from '../themes/default.scss'
import gaiaTheme from '../themes/gaia.scss'
import uncoverTheme from '../themes/uncover.scss'

// In constructor
this.themeSet.default = this.themeSet.add(defaultTheme)
this.themeSet.add(gaiaTheme)
this.themeSet.add(uncoverTheme)

// Register metadata types
this.themeSet.metaType = Object.freeze({
  'auto-scaling': String,
  size: Array,
})
```

### Theme Development

When modifying or creating themes:

1. Use SCSS for better organization
2. Define metadata in CSS comments
3. Test with `invert` class
4. Verify size presets work
5. Check auto-scaling compatibility
6. Test in sandbox: `npm run sandbox`

## Code Conventions

### TypeScript

- **No implicit any:** Disabled (`noImplicitAny: false`)
- **Interfaces:** Prefer interfaces for options
- **Type exports:** Export types for public API
- **Isolated modules:** Enabled for faster builds

### Naming Conventions

- **Plugins:** `*Plugin` suffix (e.g., `emojiPlugin`)
- **Tokens:** `marp_*` prefix (e.g., `marp_emoji`)
- **Custom elements:** `marp-*` prefix (e.g., `marp-h1`)
- **Data attributes:** `data-marp-*` (e.g., `data-marp-fitting-svg`)
- **Metadata:** kebab-case (e.g., `auto-scaling`)

### Formatting

**Prettier configuration:**

```json
{
  "semi": false,
  "singleQuote": true
}
```

**Key rules:**

- No semicolons
- Single quotes for strings
- 2-space indentation
- Trailing commas in multiline

### Imports

**ESLint enforces:**

- Alphabetical ordering
- Type imports separated
- No unused imports

```typescript
// Correct
import { Marp } from './marp'
import type { MarpOptions } from './options'
```

### File Organization

Each feature module should export:

```typescript
// markdown.ts or index.ts
export const markdown = marpitPlugin(/* ... */)
export const css = () => import('./style.scss')

// Optional
export interface FeatureOptions {
  // ...
}
```

## Common Tasks

### Adding a New Feature

1. **Create feature directory** in `src/feature-name/`
2. **Implement plugin:**
   ```typescript
   // src/feature-name/index.ts
   import marpitPlugin from '@marp-team/marpit/plugin'

   export const markdown = marpitPlugin((md) => {
     // Implementation
   })

   export const css = () => import('./style.scss')
   ```
3. **Add tests** in `test/feature-name.ts`
4. **Register plugin** in `src/marp.ts`
5. **Update types** if adding constructor options
6. **Document in README.md**
7. **Run full test suite:** `npm run test:coverage`

### Modifying Existing Features

1. **Read existing tests** in `test/` to understand behavior
2. **Make changes** in `src/`
3. **Update tests** to cover new cases
4. **Run tests:** `npm test`
5. **Check types:** `npm run check:ts`
6. **Update snapshots** if needed: `npm test -- -u`

### Adding Constructor Options

1. **Define interface** in appropriate file:
   ```typescript
   export interface NewFeatureOptions {
     enabled?: boolean
     config?: string
   }
   ```
2. **Add to MarpOptions** type (if exists or create)
3. **Update Marp constructor** in `src/marp.ts`
4. **Document** in README.md Constructor Options section
5. **Add tests** for all option combinations

### Updating Dependencies

```bash
# Check for updates
npx npm-check-updates

# Update and test
npm update
npm run build
npm run test:coverage
```

### Publishing Release

**Note:** Only maintainers can publish. Process handled by `prepack` script:

```bash
npm version minor   # Runs preversion checks + updates CHANGELOG
npm publish         # Runs prepack (build, tests, linting)
```

## Security Considerations

### HTML Sanitization

**Critical:** Always use XSS filtering for user content.

**Default allowlist** in `src/html/allowlist.ts:1-184`:

- Safe elements only (no `<script>`, `<iframe>`, etc.)
- Attribute sanitization (no `onclick`, `onerror`, etc.)
- URL protocols limited (no `javascript:`)

**Exception:** `<script>` blocks are allowed IF:

1. Content matches math typesetting patterns (MathJax)
2. Is processed by the math plugin
3. Does not contain executable code

### XSS Testing

When modifying HTML handling:

```typescript
// Always test these cases
const malicious = [
  '<img src=x onerror=alert(1)>',
  '<script>alert(1)</script>',
  '<a href="javascript:alert(1)">click</a>',
  '<iframe src="data:text/html,<script>alert(1)</script>">',
]
```

### Dependency Security

```bash
# Regular security audits
npm run check:audit

# Fix vulnerabilities
npm audit fix
```

## CI/CD Pipeline

### CircleCI

**File:** `.circleci/config.yml`

**Test matrix:**

- Node.js 18.20
- Node.js 20.19 (primary - includes lint + coverage)
- Node.js 22.21
- Node.js 24.10

**Workflow:**

1. Install dependencies
2. Run audit (`npm audit`)
3. Lint (Prettier, TypeScript, ESLint, stylelint)
4. Test with coverage
5. Upload to Codecov
6. Store test results

### Required Checks

All PRs must pass:

- ✓ All Node.js test matrices
- ✓ 95%+ code coverage
- ✓ No TypeScript errors
- ✓ ESLint and stylelint clean
- ✓ Prettier formatted
- ✓ No security vulnerabilities

## AI Assistant Guidelines

### When Making Changes

1. **Always read tests first** - Understand expected behavior from `test/` files
2. **Check coverage** - Run `npm run test:coverage` to ensure 95%+ coverage
3. **Preserve API compatibility** - This is a published library
4. **Update documentation** - Keep README.md in sync
5. **Run full validation** - Use `npm run prepack` before committing

### Code Review Checklist

Before submitting changes:

- [ ] Tests added/updated for all changes
- [ ] TypeScript types updated if API changed
- [ ] ESLint and Prettier clean
- [ ] No new security vulnerabilities
- [ ] Documentation updated
- [ ] Coverage remains ≥95%
- [ ] All tests pass on Node.js 18+
- [ ] Backward compatibility maintained

### Common Pitfalls

1. **Don't break markdown-it compatibility** - Plugins must follow markdown-it patterns
2. **Don't modify Marpit behavior** - Extend, don't override
3. **Don't skip security checks** - Always sanitize user HTML
4. **Don't ignore TypeScript errors** - Fix types, don't use `any`
5. **Don't forget browser compatibility** - Test custom elements in real browsers
6. **Don't skip theme testing** - Verify all three built-in themes

### Helpful Commands for Analysis

```bash
# Find usage of a feature
npm run grep "pattern" -- -r src/

# Check TypeScript compilation
npm run check:ts

# View build output
npm run build && ls -lah lib/

# Analyze bundle size
du -h lib/*

# Check test coverage for specific file
npm test -- --coverage --collectCoverageFrom="src/path/to/file.ts"
```

### Understanding the Codebase

When investigating an issue:

1. **Start with tests** - `test/marp.ts` has extensive examples
2. **Check README.md** - Feature documentation with examples
3. **Read plugin source** - Plugins are self-contained modules
4. **Use sandbox** - `npm run sandbox` for live testing
5. **Check snapshots** - `test/__snapshots__/` for expected outputs

### Debugging

```typescript
// Enable markdown-it debug mode (if needed)
const marp = new Marp()
marp.markdown.set({ debug: true })

// Access internal state
console.log(marp.themeSet.pack('default'))
console.log(marp.customElements.elements)

// Render with detailed output
const result = marp.render(markdown)
console.log({
  html: result.html,
  css: result.css,
  comments: result.comments,
})
```

## Additional Resources

- **Marpit Documentation:** https://marpit.marp.app
- **Marp Team Guidelines:** https://github.com/marp-team/.github/blob/master/CONTRIBUTING.md
- **markdown-it Documentation:** https://markdown-it.github.io
- **CircleCI Dashboard:** https://circleci.com/gh/marp-team/marp-core
- **Codecov Dashboard:** https://codecov.io/gh/marp-team/marp-core

## Quick Reference

### File Locations

| Purpose | Location |
|---------|----------|
| Main class | `src/marp.ts:1-463` |
| HTML allowlist | `src/html/allowlist.ts:1-184` |
| Math plugin | `src/math/math.ts:1-234` |
| Emoji plugin | `src/emoji/emoji.ts:1-267` |
| Auto-scaling | `src/auto-scaling/index.ts` |
| Default theme | `themes/default.scss` |
| Main tests | `test/marp.ts` (1,485 lines) |
| Build config | `rollup.config.mjs` |
| Jest config | `jest.config.mjs` |
| ESLint config | `eslint.config.mjs` |

### Import Paths

```typescript
// Main class
import { Marp } from '@marp-team/marp-core'

// Browser utilities (for bundlers)
import browser from '@marp-team/marp-core/browser'
```

### Key npm Scripts

```bash
npm run build          # Full production build
npm run watch          # Development watch mode
npm run sandbox        # Live development with preview
npm test               # Run all tests
npm run test:coverage  # Tests with coverage report
npm run lint:js        # ESLint
npm run lint:css       # Stylelint
npm run check:format   # Prettier check
npm run check:ts       # TypeScript check
npm run prepack        # Full CI validation
```

---

**Last Updated:** 2025-11-16
**Version:** 4.2.0
**Maintained by:** [@marp-team](https://github.com/marp-team)
