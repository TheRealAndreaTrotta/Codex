# Python da zero 

> Per chi **non avesse mai scritto una riga di Python**. Partiamo dall’idea di base (perché Python), poi passiamo a installazione, sintassi e concetti fondamentali. Ogni sezione è accompagnata da esempi funzionanti. Alla fine saprai eseguire script, organizzare il codice in moduli, usare OOP e FP, e gestire le eccezioni.

---

## Sommario

0. [Introduzione](#introduzione)
1. [Variabili](#variabili)
2. [Formattare le stringhe](#formattare-le-stringhe)
3. [Condizioni](#condizioni)
4. [Sequenze](#sequenze)
5. [Stringhe](#stringhe) 
6. [Liste](#liste) 
7. [Tuple](#tuple) 
8. [Set](#set)
10. [Dizionari](#dizionari)
11. [Cicli](#cicli)
12. [Funzioni](#funzioni)
13. [Moduli](#moduli)
14. [Programmazione a Oggetti (OOP)](#programmazione-a-oggetti-oop)
15. [Programmazione Funzionale (FP)](#programmazione-funzionale-fp)
16. [Decoratori](#decoratori)
17. [Lambda](#lambda-functions)
18. [Eccezioni](#eccezioni)
19. [REPL vs Script, interprete e pip](#repl-vs-script-interprete-e-pip)

---

## Introduzione

Finora (nel percorso web) abbiamo visto **HTML e CSS** per creare pagine e **Git/GitHub** per versionare il codice e collaborare. Oggi entriamo in **Python**, uno dei due linguaggi principali che useremo nel corso.

> **Python 3** è lo standard che useremo. Esiste ancora **Python 2** in vecchi progetti, ma quando cerchi risorse online **assicurati** che siano per Python 3.

**Perché Python?**
- Potente e molto usato: permette di costruire in fretta applicazioni web anche complesse.
- Ecosistema ricchissimo di librerie.
- Sintassi pulita → ottimo per iniziare, ma resta valido anche da pro.

**Hello, world**

```python
print("Hello, world!")
```

Qui usiamo la funzione built‑in `print`, che accetta un argomento tra parentesi e lo **mostra nel terminale**.

**Come eseguirlo sul tuo computer**

1. Scrivi la riga in un editor e salva come `qualcosa.py`.
2. Apri il terminale, vai nella cartella del file.
3. Esegui:

```bash
python3 qualcosa.py   # su molti sistemi è python3
```

Se hai `python` al posto di `python3`, usa quello. Se Python non c’è, **installalo** (e installa anche **pip**: lo useremo più avanti).

**Interprete vs compilazione**
Quando esegui `python file.py`, l’**interprete** legge il file **riga per riga** ed esegue. Diverso da linguaggi come C o Java, che **compilano** prima in linguaggio macchina.

---

## Variabili

In Python assegni con `=`:

```python
a = 28
b = 1.5
c = "Hello!"
d = True
e = None
```

Python **inferisce il tipo** (non devi dichiararlo). Tipi comuni:

• `int`: intero
• `float`: decimale
• `str`: stringa (sequenza di caratteri)
• `bool`: `True`/`False`
• `NoneType`: valore speciale `None` (assenza di valore)

**Input dell’utente**

```python
name = input("Name: ")
print("Hello, " + name)
```

Nella prima riga, `name` riceve **ciò che ritorna** `input`. Nella seconda, usiamo `+` per **concatenare** stringhe (in Python `+` somma i numeri e concatena stringhe/liste).

---

## Formattare le stringhe

Le **f‑string** semplificano molto:

```python
name = "Andrea"
print(f"Hello, {name}")
# possiamo anche inserire funzioni/espressioni
print(f"2 + 2 = {2 + 2}")

# one‑liner equivalente dell’esempio sopra
print(f"Hello, {input('Name: ')}")
```

---

## Condizioni

```python
num = int(input("Number: "))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")
```

Una **condizione** contiene `if`/`elif`/`else` e (tranne l’`else`) un’espressione **booleana** che vale `True` o `False`.
L’**indentazione** è **obbligatoria** in Python (di solito 4 spazi) e determina cosa appartiene al blocco.

> ⚠️ `input()` ritorna **sempre una stringa** → se devi confrontare con numeri, **casta** con `int(...)`. Senza cast, otterresti un `TypeError` (stavi confrontando `str` con `int`).

---

## Sequenze

Una grande forza di Python è lavorare con **sequenze** di dati.

### Stringhe

**Ordinata:** Sì · **Mutabile:** No

```python
name = "Harry"
print(name[0])  # 'H'
print(name[1])  # 'a'
```

### Liste

**Ordinata:** Sì · **Mutabile:** Sì

```python
names = ["Harry", "Ron", "Hermione"]
print(names)        # lista intera
print(names[1])     # secondo elemento
names.append("Draco")
names.sort()
print(names)
```

### Tuple

**Ordinata:** Sì · **Mutabile:** No

```python
point = (12.5, 10.6)
```

### Set

**Ordinata:** No · **Mutabile:** (particolare) — niente duplicati

```python
s = set()
s.add(1); s.add(2); s.add(3); s.add(4)
s.add(3); s.add(1)     # duplicati ignorati
s.remove(2)
print(s)
print(f"The set has {len(s)} elements.")
# Output possibile: {1, 3, 4}\nThe set has 3 elements.
```

### Dizionari

**Ordinata:** No (in CPython 3.7+ mantiene l’ordine d’inserimento) · **Mutabile:** Sì

```python
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"])           # Gryffindor
houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])        # Gryffindor
```

---

## Cicli

Due forme principali: `for` e `while`. Partiamo da `for`.

```python
for i in [0, 1, 2, 3, 4, 5]:
    print(i)
```

Stesso risultato con `range`:

```python
for i in range(6):
    print(i)  # 0..5
```

Iterare una lista di nomi:

```python
names = ["Harry", "Ron", "Hermione"]
for name in names:
    print(name)
```

Iterare i caratteri di una stringa:

```python
name = "Harry"
for ch in name:
    print(ch)
```

---

## Funzioni

Definiamo e riutilizziamo comportamenti:

```python
def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")
```

---

## Moduli

Quando il progetto cresce, separiamo funzioni in file diversi.

`functions.py`:

```python
def square(x):
    return x * x
```

`square.py`:

```python
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")
```

In alternativa, importiamo l’intero modulo e usiamo la **dot notation**:

```python
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
```

Ricorda che esistono **moduli built‑in** (es. `math`, `csv`) e che puoi installarne altri con **pip** (es. `Django`, che useremo in seguito per il web).

---

## Programmazione a Oggetti (OOP)

La OOP organizza il codice attorno a **oggetti** che **memorizzano dati** e **espongono metodi**.

**Classe semplice `Point`**

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)
print(p.x)
print(p.y)
```

**Esempio più realistico: `Flight`**

```python
class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
```

> Nota: in Python, `0` è "falsy" → `if not self.open_seats():` è `True` quando non ci sono più posti.

---

## Programmazione Funzionale (FP)

Python permette anche uno stile **funzionale**: le funzioni sono valori e possono essere passate/ritornate.

### Decoratori

Un **decoratore** è una funzione che modifica il comportamento di un’altra funzione.

```python
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()
```

### Lambda functions

Le **lambda** creano funzioni anonime, utili quando servono al volo.

```python
square = lambda x: x * x
```

Esempio pratico: ordinare una lista di dizionari per nome.

```python
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])  # ordina per nome
print(people)
```

---

## Eccezioni

Errori a runtime generano **eccezioni**. Possiamo **gestirle** con `try`/`except`.

Divisione semplice:

```python
x = int(input("x: "))
y = int(input("y: "))

result = x / y
print(f"{x} / {y} = {result}")
```

Se `y` è `0` → `ZeroDivisionError`. Gestiamolo:

```python
import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
```

Se l’utente inserisce testo non numerico → `ValueError`. Gestiamo entrambi:

```python
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
```

---

## REPL vs Script, interprete e pip

• **REPL**: avvialo con `python3` (digita `exit()` o `Ctrl+D` per uscire).
• **Script**: salva il codice in `file.py` ed esegui `python3 file.py`.
• **Interprete**: Python legge ed esegue riga per riga (non compila come C/Java).
• **pip**: gestore pacchetti. Esempi:

```bash
python3 -m pip --version
python3 -m pip install requests
python3 -m pip install django
```

> Su alcuni sistemi puoi usare `pip3`/`python` invece di `python3`.

---

### Pronti per la prossima lezione

Nella prossima lezione passeremo a **Django** (framework web) e vedremo come collegare ciò che hai imparato a una vera applicazione web.

---

## Approfondimenti — mix CS50 + pratica “pro”

### REPL vs Script vs Notebook

• **REPL** (`python3`): perfetto per provare una riga alla volta.
• **Script** (`python3 file.py`): per programmi veri, versionabili con Git.
• **Notebook** (Jupyter): ottimo per data/AI, ma per web/CLI tieni file `.py`.

### Tipi, identità e mutabilità

• **Uguaglianza** `==` vs **Identità** `is` (stesso oggetto in memoria).
• Mutabile: `list`, `dict`, `set`. Immutabile: `tuple`, `str`, `int`, `float`, `frozenset`.
• Copie: `a = b` è alias. Usa `list(a)` / `a.copy()` per **shallow copy**, `copy.deepcopy(a)` per **deep copy**.

### Slicing e unpacking

```python
nums = [0,1,2,3,4,5]
print(nums[1:4])   # [1,2,3]
head, *body, tail = nums  # unpacking avanzato
```

### Comprehensions & generatori

```python
squares = [n*n for n in range(10)]                 # list comp
unique_evens = {n for n in range(20) if n%2==0}    # set comp
index_map = {i: ch for i, ch in enumerate('kai')}  # dict comp

# generator expression (lazy)
odd = (n for n in range(1000000) if n%2)

# generator con yield
def count_up_to(n):
    c = 1
    while c <= n:
        yield c
        c += 1
```

### Context manager (`with`)

```python
# file I/O sicuro
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello from Python!
")
# il file viene chiuso automaticamente
```

### File I/O & JSON con `pathlib`

```python
from pathlib import Path
import json

path = Path("data.json")
data = {"ok": True, "items": [1,2,3]}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

loaded = json.loads(path.read_text(encoding="utf-8"))
print(loaded["items"])  # [1,2,3]
```

### Type hints (PEP 484) & dataclass

```python
from typing import Optional, Iterable
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: Optional[int] = None

def avg(xs: Iterable[float]) -> float:
    total = 0.0
    count = 0
    for x in xs:
        total += x
        count += 1
    return total / count if count else 0.0
```

Esegui **type-check** con `mypy` (facoltativo): `python3 -m pip install mypy` → `mypy file.py`.

### `__name__ == "__main__"` e CLI con `argparse`

```python
import argparse

def main():
    p = argparse.ArgumentParser(description="Demo CLI")
    p.add_argument("name")
    p.add_argument("--times", type=int, default=1)
    args = p.parse_args()
    for _ in range(args.times):
        print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
```

Esempio: `python3 app.py Andrea --times 3`.

### Ambienti virtuali & dipendenze

```bash
python3 -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
# .venv\Scripts\activate
python -m pip install --upgrade pip
pip install requests
pip freeze > requirements.txt
# ripristino
pip install -r requirements.txt
```

Suggeriti: **pipx** (per tool globali), **uv/poetry** (gestione avanzata progetti).

### Testing rapido (pytest)

`calc.py`

```python
def add(a, b):
    return a + b
```

`test_calc.py`

```python
from calc import add

def test_add():
    assert add(2, 3) == 5
```

```bash
python -m pip install pytest
pytest -q
```

### Debugging & logging

```python
# breakpoint interattivo
x = 42
breakpoint()  # entra in pdb da Python 3.7+

# logging di base
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Parto…")
```

### Stile (PEP 8) & tool

• Nomi: `snake_case` per funzioni/variabili, `PascalCase` per classi, `UPPER_CASE` per costanti.
• **black** (format), **ruff/flake8** (lint), **isort** (import).
• Docstring `"""Spiega cosa fa, parametri e ritorni"""`.

### OOP avanzata

```python
class Account:
    bank = "KaiBank"          # attributo di classe
    def __init__(self, owner, balance=0.0):
        self.owner = owner     # attributo di istanza
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("amount must be > 0")
        self._balance += amount

    def __repr__(self):
        return f"Account(owner={self.owner!r}, balance={self._balance:.2f})"
```

Oppure con **dataclasses**:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

### FP pratica

```python
from functools import lru_cache, partial

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

pow10 = partial(pow, 10)  # pow10(x) == pow(10, x)
```

### Eccezioni avanzate

```python
class NotEnoughFunds(Exception):
    pass

try:
    raise NotEnoughFunds("Balance too low")
except NotEnoughFunds as e:
    print("Transfer failed:", e)
else:
    print("Ok")
finally:
    print("Always executed")
```

---

## Mini‑progetto: To‑Do CLI (file JSON)

**Requisiti**
• Comandi: `add`, `list`, `done` (completa e rimuove).
• Dati persistenti su `todo.json`.
• Solido su input mancanti.

`todo.py`

```python
from __future__ import annotations
import argparse, json
from pathlib import Path

DB = Path("todo.json")

def load():
    if DB.exists():
        return json.loads(DB.read_text(encoding="utf-8"))
    return {"tasks": []}

def save(data):
    DB.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def cmd_add(text: str):
    data = load()
    data["tasks"].append({"text": text, "done": False})
    save(data)
    print("Added:", text)

def cmd_list():
    data = load()
    if not data["tasks"]:
        print("(no tasks)")
        return
    for i, t in enumerate(data["tasks"], 1):
        mark = "✓" if t["done"] else "✗"
        print(f"{i:2}. [{mark}] {t['text']}")

def cmd_done(index: int):
    data = load()
    i = index - 1
    if i < 0 or i >= len(data["tasks"]):
        raise IndexError("Task index out of range")
    data["tasks"][i]["done"] = True
    save(data)
    print("Completed:", data["tasks"][i]["text"])

def main():
    p = argparse.ArgumentParser(prog="todo", description="Simple To‑Do CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add")
    p_add.add_argument("text")

    sub.add_parser("list")

    p_done = sub.add_parser("done")
    p_done.add_argument("index", type=int)

    args = p.parse_args()

    if args.cmd == "add":
        cmd_add(args.text)
    elif args.cmd == "list":
        cmd_list()
    elif args.cmd == "done":
        cmd_done(args.index)

if __name__ == "__main__":
    main()
```

**Uso**

```bash
python3 todo.py add "Studiare Python"
python3 todo.py list
python3 todo.py done 1
```

---

## Esercizi (consigliati)

• Scrivi `is_even(n)` e usa `assert` per testarla.
• Con una **list comprehension**, crea i multipli di 3 sotto 100.
• Dato `people = [{"name":"A","age":20}, …]`, ordina per età (lambda).
• Implementa un **context manager** personalizzato che misura il tempo (`time.perf_counter`).
• Aggiungi al To‑Do CLI il comando `clear` con conferma.
• Aggiungi i **type hints** a tutto il progetto e lancia `mypy`.
• Scrivi test `pytest` per `cmd_add`/`cmd_done` usando un file DB temporaneo.
• Trasforma `Flight` per usare una `dataclass` `Passenger(name: str)`.

---

## Guida concettuale — utilità, potenzialità & trade‑off (non solo codice)

> Qui spiego **perché** userai ogni concetto, **quando** conviene, e **cosa evitare**. Pochi esempi, molta strategia.

### Interprete vs compilazione

**Perché importa**: l'interprete di Python esegue riga per riga → ottimo per **prototipare** e **automatizzare**. Compilati (C/Java) danno massime prestazioni ma ciclo di sviluppo più lento.
**Trade‑off**: Python è più lento su CPU‑bound puro, ma spesso recuperi con librerie C ottimizzate (es. NumPy) e con la **produttività**.

### REPL vs Script vs Notebook

• **REPL**: sperimentazione rapida, verifica funzioni, debugging veloce.
• **Script**: automazioni, CLI, job schedulati, progetti versionati.
• **Notebook**: analisi dati, AI/ML, report esplorativi.
**Evita**: notebook per logica di produzione; meglio promuovere in moduli `.py` testabili.

### Variabili e tipi (dinamici)

**Perché**: tipizzazione dinamica accelera lo sviluppo e riduce boilerplate.
**Attenzione**: errori di tipo emergono **a runtime**; usa **type hints** + `mypy` per prevenire bug.
**Concetti chiave**: `None` come "assenza di valore"; "truthiness" (0, '', [], {}, None sono falsy).

### Stringhe & f‑string

**Perché**: formattazione leggibile e sicura (evita concatenazioni fragili).
**Quando**: log, messaggi utente, reporting.
**Evita**: f‑string con input non validati in contesti sensibili (inserisci sanitizzazione).

### Condizioni

**Perché**: separare i casi chiave.
**Pattern utili**: **guard clauses** (ritorna presto se invalidi), `match` per casi multipli.
**Evita**: `if` annidati profondi; preferisci funzioni piccole e nomi espliciti.

### Sequenze: scegliere la struttura giusta

• **list**: ordine, mutabile, uso generale.
• **tuple**: immutabile, record leggeri (coordinate, chiavi).
• **set**: membership/duplicati; operazioni insiemistiche veloci.
• **dict**: mappare chiave→valore, base di molte strutture applicative.
**Complessità media**: `in` su set/dict ≈ O(1), su list/tuple ≈ O(n).

### Cicli & iterazione

**Perché**: visitare collezioni.
**Pattern**: `enumerate` per indici, `zip` per avanzare in parallelo, generatori per flussi infiniti o grandi.
**Evita**: modificare la lista mentre la iteri (usa copia o comprensioni).

### Funzioni

**Perché**: riuso, testabilità, composizione.
**Buone pratiche**: una funzione = una responsabilità; docstring; parametri nominali.
**Trappola**: default **mutabili**. Non fare `def f(x=[])`; usa `None` e crea dentro: `x = [] if x is None else x`.

### Moduli & pacchetti

**Perché**: organizzare il codice, **namespace** chiari, riuso.
**Concetti**: import assoluti, pacchetti con `__init__.py`, entry‑point via `if __name__ == "__main__"`.
**Evita**: import circolari (rifattorizza in moduli condivisi).

### OOP (oggetti, non solo classi)

**Perché**: modellare entità con **dati + comportamenti**; incapsulare invarianti (es. `balance >= 0`).
**Linee guida**: preferisci **composizione** a ereditarietà; usa `@property` per garantire validazioni; `__repr__` utile nel debug.
**Dataclass**: comoda per oggetti‑dati (meno boilerplate) → attenzione: sono mutabili di default.

### FP (funzionale) pratico

**Perché**: trasformazioni dichiarative, meno stato condiviso.
**Strumenti**: `map/filter`, **lambda** per callback rapide, `functools` (`lru_cache`, `partial`).
**Evita**: catene di lambda opache; se diventa illeggibile, scrivi funzioni nominate.

### Comprehensions & generatori

**Perché**: costruire collezioni in modo **espressivo**; generatori sono **lazy** e risparmiano memoria.
**Quando**: dataset grandi/stream → generatori; liste piccole → list comp.
**Tool**: `itertools` (`chain`, `groupby`, `islice`).

### Context manager

**Perché**: gestione **sicura** delle risorse (file, lock, connessioni).
**Come**: `with` garantisce cleanup in caso di eccezioni.
**Custom**: implementa `__enter__/__exit__` o usa `contextlib.contextmanager`.

### Type hints

**Perché**: IDE più smart, refactor sicuri, contratti espliciti.
**Nota**: non sono enforce a runtime; usa `mypy/pyright` per verificarli.
**Avanzato**: `Protocol`, `TypedDict`, `Literal` per modelli più precisi.

### Eccezioni

**Perché**: flusso di errore **separato** dal flusso normale.
**Pattern**: `try/except/else/finally`, eccezioni **di dominio** personalizzate.
**Evita**: catturare `Exception` in blocchi enormi; limita lo scope e logga il contesto.

### Ambienti virtuali & dipendenze

**Perché**: **isolamento** e replicabilità.
**Pattern**: `requirements.txt` per pin rapidi; `pyproject.toml` (poetry/uv) per progetti moderni.
**Evita**: dipendenze globali condivise tra progetti.

### Testing (pytest)

**Perché**: fiducia nei refactor, prevenzione regressioni.
**Tecniche**: `parametrize`, **fixtures** per setup pulito, `coverage` per misurare.

### Debugging & logging

**Perché**: osservabilità.
**Strumenti**: `breakpoint()` per ispezionare stato; livelli log (`DEBUG`→`CRITICAL`).
**Evita**: `print` debugging lasciato nel codice di produzione.

### Stile (PEP 8) & tool

**Perché**: leggibilità di team.
**Stack consigliato**: **black** (format), **ruff** (lint), **isort** (import), **pre‑commit** (hook).
**CI**: integra test+lint nei workflow (GitHub Actions).

### CLI con `argparse`

**Perché**: trasformare script in **strumenti** con help e parametri.
**UX**: descrizioni chiare, error code (`sys.exit`), messaggi utili.

### Performance: quando pensarci

**Prima**: scegli la struttura dati giusta.
**Misura**: `timeit`, profiler (`cProfile`).
**Ottimizza**: usa built‑in C‑ottimizzati, evita micro‑ottimizzazioni premature.

### Dati & formati

**JSON**: interoperabile web; **CSV**: tabelle; **YAML/TOML**: config.
**Schema**: dataclass/`pydantic` per validare (quando serve).

---

## Mappa mentale del corso (da tenere a mente)

1. **Base**: sintassi, tipi, sequenze, funzioni.
2. **Struttura**: moduli, pacchetti, OOP/FP.
3. **Robustezza**: eccezioni, type hints, test, logging.
4. **Prodotto**: CLI, ambienti, packaging, performance.
5. **Prossimo step**: **Django/FastAPI** (web), **pandas/NumPy** (data), **automazione** (script schedulati).
