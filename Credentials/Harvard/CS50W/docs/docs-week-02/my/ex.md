# Facile — Analizzatore di numero

**Obiettivo**
• Chiedi un numero intero all’utente e stampa:

* se è **positivo/negativo/zero**
* se è **pari/dispari**

**Criteri di successo**
• Input: `-3` → Output: `negativo, dispari`
• Input: `0` → Output: `zero, pari`
• Gestisci input non valido con un messaggio d’errore pulito (niente stacktrace).

**Hint**
• `int(input(...))` + `try/except ValueError`
• `n % 2 == 0` per la parità
• Usa **f-string** ed **indentazione** pulita

---

# Medio — Dedup & Count dei nomi

**Obiettivo**
• Leggi una riga tipo:
`Harry, Ron, Hermione, Harry, Draco, ron`
• Stampa:

* l’elenco **unico** dei nomi in ordine alfabetico (case-insensitive)
* la **frequenza** di ciascun nome (normalizzato, es. tutto minuscolo)
* il **più frequente** (tie-break alfabetico)

**Criteri di successo**
• Input: `Harry, Ron, Hermione, Harry, Draco, ron`

* Unici: `draco, harry, hermione, ron`
* Frequenze: `harry: 2, ron: 2, draco: 1, hermione: 1`
* Più frequente: `harry` (ma se hai pareggio, scegli alfabeticamente)

**Hint**
• `.split(',')` → `.strip()` → `.lower()`
• `dict` (o `collections.Counter`) per contare
• Ordina con `sorted(items, key=lambda kv: (-kv[1], kv[0]))`

---

# Hard — Mini “Car Inventory” CLI (JSON)

**Obiettivo**
• Crea una CLI per gestire un piccolo inventario auto salvato in `cars.json`.

**Comandi richiesti**
• `add` — aggiunge un’auto

* argomenti obbligatori: `--brand`, `--model`, `--year` (int), `--price` (float), `--fuel` (scelte: diesel, petrol, hybrid, electric)
* opzionali: `--euro` (es. `6d-temp`), `--km` (int)
  • `list` — mostra l’inventario
* filtri opzionali: `--fuel`, `--max-price`, `--brand`
* sorting opzionale: `--sort price|year|brand`
  • `stats` — stampa statistiche base
* `count totale`, `prezzo medio`, `anno mediano`, `count per brand`

**Requisiti tecnici**
• **File I/O**: `pathlib.Path` + JSON (crea file se non esiste)
• **Type hints** + `@dataclass Car` (`brand: str`, `model: str`, `year: int`, `price: float`, `fuel: str`, `euro: str|None`, `km: int|None`)
• **argparse** per la CLI; entrypoint con `if __name__ == "__main__":`
• **Validazioni**: year ≥ 1990; price > 0; fuel tra le scelte; km ≥ 0
• **Error handling**: messaggi chiari, `sys.exit(1)` su input invalidi
• **Bonus**: `pytest` con test su `add` e `list` (filtri/sort)

**Criteri di successo (esempi)**
• `python3 inv.py add --brand Peugeot --model 308 --year 2022 --price 21999.99 --fuel diesel --euro 6d-isc-fcm --km 89000`
• `python3 inv.py list --fuel diesel --sort price --max-price 23000`
• `python3 inv.py stats` → mostra conteggio, prezzo medio, ecc.

**Hint**
• `dataclasses.asdict(car)` per serializzare
• Per `median` puoi usare `statistics.median`
• Ordina con `sorted(lista, key=lambda c: (c['price']))` ecc.

---
