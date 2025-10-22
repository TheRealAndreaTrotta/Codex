# HTML & CSS Notes — with examples

> File language: [IT](README.it.md) * [EN]

## Table of contents

* [1. Base structure & `<!doctype html>`](#1-base-structure--doctype-html)
* [2. Headings (H1–H6)](#2-headings-h1h6)
* [3. Text & system fonts](#3-text--system-fonts)
* [4. Links](#4-links)
* [5. Images](#5-images)
* [6. Lists (ol/ul)](#6-lists-olul)
* [7. `div` and semantics](#7-div-and-semantics)
* [8. Tables](#8-tables)
* [9. Forms (labels, datalist, submit)](#9-forms-labels-datalist-submit)
* [10. CSS selectors (type, class, id, attribute)](#10-css-selectors-type-class-id-attribute)
* [11. Descendant vs direct child](#11-descendant-vs-direct-child)
* [12. Pseudo-classes: `:hover` essentials](#12-pseudo-classes-hover-essentials)
* [13. Flexbox (one-dimensional layout)](#13-flexbox-one-dimensional-layout)
* [14. Grid (two-dimensional layout)](#14-grid-two-dimensional-layout)
* [15. Responsive design (viewport + media queries)](#15-responsive-design-viewport--media-queries)
* [16. External files & SCSS](#16-external-files--scss)
* [17. Accessibility: quick notes](#17-accessibility-quick-notes)
* [18. Common mistakes (and how we fixed them)](#18-common-mistakes-and-how-we-fixed-them)
* [19. Mini-exercises](#19-mini-exercises)

---

## 1. Base structure & `<!doctype html>`

**What is the doctype?** It tells the browser which HTML version is used. Today it’s always:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Page title</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <!-- Content -->
  </body>
</html>
```

> `lang` helps a11y and SEO; `meta viewport` is essential for mobile.

---

## 2. Headings (H1–H6)

Headings define content hierarchy (one `h1` per page is a good practice):

```html
<h1>Page title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
```

---

## 3. Text & system fonts

Start light and consistent across devices:

```css
body {
  font: 16px/1.55 system-ui, -apple-system, "Segoe UI", Roboto, Ubuntu, Arial, sans-serif;
  color: #111;
}
```

> Prefer `line-height` ≥ 1.4 for readability. For webfonts, consider deferred loading.

---

## 4. Links

```html
<a href="https://example.com">Visit Example</a>
<a href="image.html">Open image example</a>
```

> Use descriptive link text; avoid generic “click here”. Use relative links for local files.

---

## 5. Images

```html
<figure>
  <img src="assets/photo.jpg" alt="Clear description of the image" width="800" height="533" />
  <figcaption>Optional caption.</figcaption>
</figure>
```

```css
img { max-width: 100%; height: auto; display: block; }
```

> Explicit `width`/`height` helps prevent layout shift.

---

## 6. Lists (ol/ul)

```html
<h2>Ordered</h2>
<ol>
  <li>First</li>
  <li>Second</li>
  <li>Third</li>
</ol>

<h2>Unordered</h2>
<ul>
  <li>Item A</li>
  <li>Item B</li>
  <li>Item C</li>
</ul>
```

> Nested lists must always be placed inside a parent `li`.

---

## 7. `div` and semantics

`div` is neutral. Prefer semantic tags when possible: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`.

```html
<main>
  <section>
    <h2>Section</h2>
    <p>Content…</p>
  </section>
</main>
```

---

## 8. Tables

```html
<table>
  <caption>Sample data</caption>
  <thead>
    <tr>
      <th>Column 1</th>
      <th>Column 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Value A</td>
      <td>Value B</td>
    </tr>
  </tbody>
</table>
```

```css
table { border-collapse: collapse; }
th, td { border: 1px solid #000; padding: 8px; text-align: left; }
```

> In `thead`, `th` elements must be wrapped in a `tr`.

---

## 9. Forms (labels, datalist, submit)

```html
<form action="#" method="get">
  <label>
    Full name
    <input type="text" name="name" placeholder="First and last name" required />
  </label>

  <label>
    Password
    <input type="password" name="password" required />
  </label>

  <fieldset>
    <legend>Favorite color</legend>
    <label><input type="radio" name="color" value="red" /> Red</label>
    <label><input type="radio" name="color" value="green" /> Green</label>
    <label><input type="radio" name="color" value="blue" /> Blue</label>
  </fieldset>

  <label>
    Country
    <input type="text" name="country" list="countries" />
  </label>
  <datalist id="countries">
    <option value="Italy"></option>
    <option value="France"></option>
    <option value="Spain"></option>
  </datalist>

  <button type="submit">Submit</button>
</form>
```

> Every control needs a label. `fieldset` + `legend` group related inputs.

---

## 10. CSS selectors (type, class, id, attribute)

```css
/* type */
p { margin-bottom: 1rem; }

/* class */
.card { border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; }

/* id (avoid for repeated styling) */
#hero { padding-block: 48px; }

/* attribute */
input[type="password"] { letter-spacing: 0.08em; }
a[target="_blank"] { text-decoration: underline; }
```

> Prefer classes for styling. IDs are unique—better for anchors or JS hooks.

---

## 11. Descendant vs direct child

```css
/* any descendant */
ul li { color: #444; }

/* only direct children */
ul > li { color: #e11d48; }
```

```html
<ol>
  <li>Item
    <ul>
      <li>Sub-item</li>
    </ul>
  </li>
</ol>
```

> The nested `ul` must live inside a parent `li` of the `ol`.

---

## 12. Pseudo-classes: `:hover` essentials

```css
a { color: #0ea5e9; text-decoration: none; }
a:hover { text-decoration: underline; }
.button:hover { transform: translateY(-1px); }
```

> Add light `transition`s for polished feedback.

---

## 13. Flexbox (one-dimensional layout)

```html
<div class="row">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

```css
.row {
  display: flex;
  gap: 16px;
  justify-content: center;   /* or space-between */
  align-items: center;
}
.row > div { padding: 12px; background: #e5f2ff; border: 1px solid #93c5fd; }
```

> Flex is great for alignment and space distribution **in one direction**.

---

## 14. Grid (two-dimensional layout)

```html
<div class="grid">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
</div>
```

```css
.grid {
  display: grid;
  grid-template-columns: 200px 200px auto; /* or repeat(3, 1fr) */
  column-gap: 20px;
  row-gap: 10px; /* or: gap: 10px 20px; */
}
.item { background: #cffafe; border: 1px solid #67e8f9; padding: 20px; text-align: center; }
```

> Use modern `gap`; `grid-row-gap`/`grid-column-gap` are deprecated.

---

## 15. Responsive design (viewport + media queries)

```css
/* Mobile-first: base styles for small screens */
body { font-family: system-ui; background: #fff; }

/* From 601px and up */
@media (min-width: 601px) {
  body { background: #eef6ff; }
}

/* Up to 600px */
@media (max-width: 600px) {
  body { background: #ffe4e6; }
}
```

> Don’t forget the `meta viewport` in `<head>`. Use clear breakpoints and proper units.

---

## 16. External files & SCSS

Browsers **do not** read `.scss`. Compile to CSS first:

```bash
sass variables.scss variables.css
```

Then link the compiled CSS:

```html
<link rel="stylesheet" href="variables.css" />
```

> Keep CSS modular (tokens/base/components) and import them in an aggregator.

---

## 17. Accessibility: quick notes

* Descriptive `alt` text for images.
* Always associate `label`s with inputs (wrapping or `for`/`id`).
* Correct heading order and hierarchy.
* Sufficient color contrast and visible focus states.

---

## 18. Common mistakes (and how we fixed them)

* Malformed tags: e.g., `body>` → correct `<body>`.
* Duplicate/typo attributes: `<html html lang="en">` → `<html lang="en">`.
* Nested lists: `ul` outside of `li` → move inside the parent `li`.
* `thead` without `tr` → wrap `th` in a `tr`.
* Media query without units → add `px`.
* Linking `.scss` directly → compile to `.css` and link that file.

---