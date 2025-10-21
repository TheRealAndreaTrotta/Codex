# HTML & CSS Appunti — con esempi

> File language: [EN](README.md) * [IT]

## Indice

* [1. Struttura base & `<!doctype html>`](#1-struttura-base--doctype-html)
* [2. Headings (H1–H6)](#2-headings-h1h6)
* [3. Testo & font di sistema](#3-testo--font-di-sistema)
* [4. Link](#4-link)
* [5. Immagini](#5-immagini)
* [6. Liste (ol/ul)](#6-liste-olul)
* [7. `div` e semantica](#7-div-e-semantica)
* [8. Tabelle](#8-tabelle)
* [9. Form (etichette, datalist, submit)](#9-form-etichette-datalist-submit)
* [10. Selettori CSS (tipo, classe, id, attributo)](#10-selettori-css-tipo-classe-id-attributo)
* [11. Discendente vs Figlio diretto](#11-discendente-vs-figlio-diretto)
* [12. Pseudo-classi: `:hover` essenziale](#12-pseudo-classi-hover-essenziale)
* [13. Flexbox (layout monodimensionale)](#13-flexbox-layout-monodimensionale)
* [14. Grid (layout bidimensionale)](#14-grid-layout-bidimensionale)
* [15. Responsive design (viewport + media queries)](#15-responsive-design-viewport--media-queries)
* [16. File esterni & SCSS](#16-file-esterni--scss)
* [17. Accessibilità: note rapide](#17-accessibilità-note-rapide)
* [18. Errori comuni (e come li abbiamo corretti)](#18-errori-comuni-e-come-li-abbiamo-corretti)
* [19. Mini-esercizi](#19-mini-esercizi)

---

## 1. Struttura base & `<!doctype html>`

**Cos'è il doctype?** È una dichiarazione che informa il browser della versione HTML utilizzata. Oggi è sempre:

```html
<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Titolo della pagina</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <!-- Contenuto -->
  </body>
</html>
```

> Nota: `lang` aiuta accessibilità e SEO; `meta viewport` è fondamentale per il mobile.

---

## 2. Headings (H1–H6)

Gli heading strutturano la gerarchia del contenuto (un solo `h1` per pagina è una buona pratica):

```html
<h1>Titolo pagina</h1>
<h2>Sezione</h2>
<h3>Sottosezione</h3>
```

---

## 3. Testo & font di sistema

Per partire leggeri e coerenti su tutti i device:

```css
body {
  font: 16px/1.55 system-ui, -apple-system, "Segoe UI", Roboto, Ubuntu, Arial, sans-serif;
  color: #111;
}
```

> Usa `line-height` ≥ 1.4 per leggibilità. Per webfont, valuta il caricamento differito.

---

## 4. Link

```html
<a href="https://example.com">Visita Example</a>
<a href="image.html">Apri esempio immagini</a>
```

> Testo link chiaro, niente “clicca qui” generico; usa link relativi per file locali.

---

## 5. Immagini

```html
<figure>
  <img src="assets/foto.jpg" alt="Descrizione chiara dell’immagine" width="800" height="533" />
  <figcaption>Didascalia opzionale.</figcaption>
</figure>
```

```css
img { max-width: 100%; height: auto; display: block; }
```

> Specificare `width` e `height` aiuta a prevenire il layout shift.

---

## 6. Liste (ol/ul)

```html
<h2>Ordered</h2>
<ol>
  <li>Primo</li>
  <li>Secondo</li>
  <li>Terzo</li>
</ol>

<h2>Unordered</h2>
<ul>
  <li>Voce A</li>
  <li>Voce B</li>
  <li>Voce C</li>
</ul>
```

> Le liste annidate vanno sempre dentro un `li` del livello superiore.

---

## 7. `div` e semantica

`div` è neutro. Preferisci tag semantici quando possibile: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`.

```html
<main>
  <section>
    <h2>Sezione</h2>
    <p>Contenuto…</p>
  </section>
</main>
```

---

## 8. Tabelle

```html
<table>
  <caption>Dati di esempio</caption>
  <thead>
    <tr>
      <th>Colonna 1</th>
      <th>Colonna 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Valore A</td>
      <td>Valore B</td>
    </tr>
  </tbody>
</table>
```

```css
table { border-collapse: collapse; }
th, td { border: 1px solid #000; padding: 8px; text-align: left; }
```

> In `thead` i `th` devono stare dentro un `tr`.

---

## 9. Form (etichette, datalist, submit)

```html
<form action="#" method="get">
  <label>
    Nome completo
    <input type="text" name="name" placeholder="Nome e cognome" required />
  </label>

  <label>
    Password
    <input type="password" name="password" required />
  </label>

  <fieldset>
    <legend>Colore preferito</legend>
    <label><input type="radio" name="color" value="red" /> Rosso</label>
    <label><input type="radio" name="color" value="green" /> Verde</label>
    <label><input type="radio" name="color" value="blue" /> Blu</label>
  </fieldset>

  <label>
    Paese
    <input type="text" name="country" list="countries" />
  </label>
  <datalist id="countries">
    <option value="Italy"></option>
    <option value="France"></option>
    <option value="Spain"></option>
  </datalist>

  <button type="submit">Invia</button>
</form>
```

> Ogni controllo va etichettato. `fieldset`+`legend` raggruppano logicamente.

---

## 10. Selettori CSS (tipo, classe, id, attributo)

```css
/* tipo */
p { margin-bottom: 1rem; }

/* classe */
.card { border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; }

/* id (evita per styling ripetuto) */
#hero { padding-block: 48px; }

/* attributo */
input[type="password"] { letter-spacing: 0.08em; }
a[target="_blank"] { text-decoration: underline; }
```

> Preferisci classi per lo styling. Gli id sono unici e più utili per ancore/JS.

---

## 11. Discendente vs Figlio diretto

```css
/* Qualsiasi discendente */
ul li { color: #444; }

/* Solo figli diretti */
ul > li { color: #e11d48; }
```

```html
<ol>
  <li>Elemento
    <ul>
      <li>Sotto-elemento</li>
    </ul>
  </li>
</ol>
```

> L’`ul` annidato deve essere dentro un `li` dell’`ol`.

---

## 12. Pseudo-classi: `:hover` essenziale

```css
a { color: #0ea5e9; text-decoration: none; }
a:hover { text-decoration: underline; }
.button:hover { transform: translateY(-1px); }
```

> Usa transizioni leggere (`transition`) per feedback eleganti.

---

## 13. Flexbox (layout monodimensionale)

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

> Flex è ideale per allineamento e distribuzione nello **spazio in una direzione**.

---

## 14. Grid (layout bidimensionale)

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
  grid-template-columns: 200px 200px auto; /* o repeat(3, 1fr) */
  column-gap: 20px;
  row-gap: 10px; /* oppure: gap: 10px 20px; */
}
.item { background: #cffafe; border: 1px solid #67e8f9; padding: 20px; text-align: center; }
```

> Usa `gap` moderno; `grid-row-gap`/`grid-column-gap` sono deprecati.

---

## 15. Responsive design (viewport + media queries)

```css
/* Mobile-first: stili base per schermi piccoli */
body { font-family: system-ui; background: #fff; }

/* Da 601px in su */
@media (min-width: 601px) {
  body { background: #eef6ff; }
}

/* Fino a 600px */
@media (max-width: 600px) {
  body { background: #ffe4e6; }
}
```

> Ricorda `meta viewport` nell’`<head>` e unità con `px`/`rem`. Definisci breakpoint chiari.

---

## 16. File esterni & SCSS

I browser **non** leggono `.scss`. Compila prima in CSS:

```bash
sass variables.scss variables.css
```

Poi collega il CSS compilato:

```html
<link rel="stylesheet" href="variables.css" />
```

> Mantieni i CSS modulari (tokens/base/components) e importa in un file aggregatore.

---

## 17. Accessibilità: note rapide

* Testi alternativi (`alt`) descrittivi per le immagini.
* Associa sempre `label` agli input (wrapping o `for`/`id`).
* Ordine gerarchico corretto degli heading.
* Contrasto colore sufficiente, focus visibile.

---

## 18. Errori comuni (e come li abbiamo corretti)

* Tag malformati: es. `body>` → corretto `<body>`.
* Attributi duplicati/typo: es. `<html html lang="en">` → `<html lang="en">`.
* `ul` fuori da `li` in liste annidate → spostato dentro il `li` padre.
* `thead` senza `tr` → aggiunto `tr` attorno ai `th`.
* Media query senza unità → aggiunto `px`.
* Collegamento `.scss` in HTML → compila in `.css` e collega quello.

---