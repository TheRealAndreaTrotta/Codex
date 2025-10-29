# Python — Lecture 2

> Note per Andrea: questa è la versione *README/lezione* in stile Git&GitHub che avevamo fatto. È pensata per essere letta velocemente, con esempi eseguibili e piccole challenge.

---

## Indice

* [Introduzione](#introduzione)
* [Python (cos'è e come si usa)](#python-cosè-e-come-si-usa)
* [Variabili](#variabili)
* [Formattazione delle stringhe (f-strings)](#formattazione-delle-stringhe-f-strings)
* [Condizioni](#condizioni)
* [Sequenze](#sequenze)

  * [Stringhe](#stringhe)
  * [Liste](#liste)
  * [Tuple](#tuple)
  * [Set](#set)
  * [Dizionari](#dizionari)
* [Cicli (Loops)](#cicli-loops)
* [Funzioni](#funzioni)
* [Moduli](#moduli)
* [Programmazione a Oggetti (OOP)](#programmazione-a-oggetti-oop)
* [Programmazione Funzionale](#programmazione-funzionale)

  * [Decoratori](#decoratori)
  * [Lambda](#lambda)
* [Eccezioni](#eccezioni)
* [Appendice: setup veloce su macOS/Linux/Windows](#appendice-setup-veloce-su-macoslinuxwindows)
* [Mini-esercizi](#mini-esercizi)

---

## Introduzione

Finora abbiamo visto HTML/CSS e Git/GitHub. Oggi entriamo in **Python 3**, linguaggio semplice ma potente, perfetto per web app (Django/Flask), scripting, data, automazione.

> Useremo **Python 3**. Quando cerchi risorse esterne, verifica sempre che siano aggiornate a Python 3.

---

## Python (cos'è e come si usa)

**Interprete**: Python esegue il codice *riga per riga* (non compila in binario come C/Java).

**Hello, world**

```python
print("Hello, world!")
```

**Come eseguirlo**

1. Crea `hello.py` con il contenuto sopra.
2. Da terminale, nella cartella del file:

```bash
python3 hello.py   # su macOS/Linux di solito è python3
# oppure
python hello.py    # su Windows o dove 'python' punta a Python 3
```

> Se `python` dà *command not found*, usa `python3`. Se manca anche quello, vedi la [Appendice](#appendice-setup-veloce-su-macoslinuxwindows).

**Pip (gestore pacchetti)**: installeremo librerie terze parti più avanti (es. `pip install requests`).

---

## Variabili

Assegnazione e tipi (tipi *inferiti*):

```python
a = 28            # int
b = 1.5           # float
c = "Hello!"      # str
d = True          # bool
e = None          # NoneType
```

**Input utente**

```python
name = input("Name: ")
print("Hello, " + name)
```

> `input()` **restituisce sempre una stringa**. Se ti serve un numero:

```python
num = int(input("Number: "))
```

---

## Formattazione delle stringhe (f-strings)

Più pulite e leggibili:

```python
name = input("Name: ")
print(f"Hello, {name}")

# One-liner (nota le virgolette interne singole)
print(f"Hello, {input('Name: ')}")
```

---

## Condizioni

Indentazione **obbligatoria** in Python (spazi, non tab misti):

```python
num = int(input("Number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")
```

> Errore classico: confrontare `str` con `int` (es. dimenticare `int(...)`).

---

## Sequenze

Concetti chiave:

* **Ordinato?** l'ordine degli elementi è significativo.
* **Mutabile?** gli elementi possono cambiare dopo la creazione.

### Stringhe

* **Ordinato**: Sì
* **Mutabile**: No

```python
name = "Harry"
print(name[0])  # 'H'
print(name[1])  # 'a'
```

### Liste

* **Ordinato**: Sì
* **Mutabile**: Sì

```python
names = ["Harry", "Ron", "Hermione"]
print(names)         # lista intera
print(names[1])      # 'Ron'

names.append("Draco")
names.sort()
print(names)
```

### Tuple

* **Ordinato**: Sì
* **Mutabile**: No

```python
point = (12.5, 10.6)
```

### Set

* **Ordinato**: No
* **Mutabile**: **Sì** (puoi aggiungere/rimuovere elementi)
* **Unicità**: ogni valore appare una sola volta

```python
s = set()

s.add(1); s.add(2); s.add(3); s.add(4)
s.add(3); s.add(1)   # duplicati ignorati

s.remove(2)

print(s)                         # {1, 3, 4}
print(f"The set has {len(s)} elements.")  # 3
```

### Dizionari

* **Ordinato**: Dal 3.7 l'inserimento è preservato (ma pensali concettualmente *non ordinati*)
* **Mutabile**: Sì
* **Struttura**: `chiave -> valore`

```python
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"])  # Gryffindor

houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])  # Gryffindor
```

---

## Cicli (Loops)

```python
# range(n) genera 0..n-1
for i in range(6):
    print(i)

names = ["Harry", "Ron", "Hermione"]
for name in names:
    print(name)

for ch in "Harry":
    print(ch)
```

---

## Funzioni

```python
def square(x):
    return x * x

for i in range(10):
    print(f"The square of {i} is {square(i)}")
```

Suggerimenti:

* Documenta con docstring (`"""testo"""`).
* Tipizza opzionalmente:

```python
def square(x: int) -> int:
    """Return x squared."""
    return x * x
```

---

## Moduli

Separa funzioni e usale altrove.

`functions.py`

```python
def square(x):
    return x * x
```

`square.py`

```python
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}")
```

Oppure importa il modulo intero:

```python
import functions
print(functions.square(7))
```

> Moduli built‑in utili: `math`, `csv`, `json`, `datetime`, `pathlib`, `itertools`.

---

## Programmazione a Oggetti (OOP)

**Classe semplice**

```python
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

p = Point(2, 8)
print(p.x, p.y)  # 2 8
```

**Esempio pratico: volo con capienza**

```python
class Flight:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.passengers: list[str] = []

    def open_seats(self) -> int:
        return self.capacity - len(self.passengers)

    def add_passenger(self, name: str) -> bool:
        if self.open_seats() == 0:
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

---

## Programmazione Funzionale

Python tratta le funzioni come valori.

### Decoratori

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

> NB: per funzioni con argomenti, usa `*args, **kwargs` nel `wrapper`.

### Lambda

```python
square = lambda x: x * x

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

people.sort(key=lambda person: person["name"])  # ordina per nome
print(people)
```

---

## Eccezioni

Gestione degli errori con `try/except` (e opzionalmente `else/finally`).

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
else:
    print(f"{x} / {y} = {result}")
finally:
    pass  # cleanup se serve
```

---

## Appendice: setup veloce su macOS/Linux/Windows

* **Controlla versione**: `python3 --version` (oppure `python --version`).
* **macOS**: usa Homebrew

  * `brew install python`
  * esegui con `python3` e `pip3`.
* **Linux (Debian/Ubuntu)**: `sudo apt update && sudo apt install python3 python3-pip`
* **Windows**: scarica da python.org, spunta *Add Python to PATH*; poi `py`, `python`, `pip`.
* **Virtual env (consigliato)**:

  * `python3 -m venv .venv` → `source .venv/bin/activate` (Win: `.venv\Scripts\activate`)
  * `pip install -U pip`

---

## Mini-esercizi

• **E1 – F-strings**: chiedi nome e città e stampa `Ciao NAME, com'è il tempo a CITY?`
• **E2 – Condizioni**: leggi un intero e stampa *pari/dispari/zero*.
• **E3 – Liste**: leggi 5 nomi, ordina alfabeticamente, stampa l'indice di ciascuno.
• **E4 – Dizionario**: mappa `nome → voto` e calcola la media.
• **E5 – OOP**: crea classe `BankAccount` con `deposit`, `withdraw`, `balance`.
• **E6 – Eccezioni**: estendi E5 gestendo `withdraw` oltre il saldo (solleva `ValueError`).

---

### Extra tips

• Mantieni lo stile PEP 8 (indentazione 4 spazi).
• Usa `if __name__ == "__main__":` per il codice eseguibile nei moduli.
• Salva snippet utili in una cartella `snippets/` del tuo progetto.
• Quando hai dubbi sui tipi, prova il REPL (`python3`) per sperimentare velocemente.
