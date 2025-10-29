# Python — eccezioni, `try/except`, parsing e codice robusto

> File language: [IT]

Questa è una lezione pensata per chi **non ha mai usato** le eccezioni in Python o le ha usate “a tentoni”. Partiamo dal **perché** esistono, capiamo la **meccanica** (`try/except/else/finally`), vediamo **pattern pratici** (input utente, file, JSON, rete), **antipattern** da evitare e chiudiamo con **esercizi guidati** e un **cheatsheet**.

---

0. [Perché esistono le eccezioni](#0)
1. [Lessico minimo (senza dare nulla per scontato)](#1)
2. [Anatomia di `try/except/else/finally`](#2)
3. [Dove metterle: estensione minima del `try`](#3)
4. [Parsing di input numerico (con `,` o `.`)](#4)
5. [Validazione vs parsing (responsabilità chiare)](#5)
6. [Le eccezioni più comuni (mappa mentale)](#6)
7. [File I/O robusto: `open`, `with`, errori tipici](#7)
8. [JSON e CSV: messaggi d’errore utili](#8)
9. [Rete e timeouts (approccio idiomatico)](#9)
10. [“Lanciare” eccezioni (`raise`), `assert`, eccezioni custom](#10)
11. [Propagazione, re-raise, chaining (`from e`), logging](#11)
12. [EAFP vs LBYL: quando “provare” e quando “controllare”](#12)
13. [Performance: perché non abusarne (ma non temerle)](#13)
14. [Antipattern da evitare](#14)
15. [Testare le eccezioni](#15)
16. [Esercizi guidati (falli davvero)](#16)
17. [Errori tipici e soluzioni rapide](#17)
18. [Cheatsheet finale](#18)
19. [Riepilogo in una riga](#19)

---

<h2 id="0">0) Perché esistono le eccezioni</h2>

Quando qualcosa **può fallire** (input utente, file mancanti, rete lenta, dati malformati), hai due scelte:
• Far **crashare** il programma.
• **Gestire** il fallimento, informare bene l’utente e decidere cosa fare dopo.

Le **eccezioni** sono il linguaggio con cui Python segnala i fallimenti. `try/except` è lo strumento per reagire **senza** far collassare tutto.

---

<h2 id="1">1) Lessico minimo (senza dare nulla per scontato)</h2>

• **Errore / eccezione**: un evento anomalo (es. `ValueError`, `FileNotFoundError`).
• **Lanciare / sollevare**: generare l’eccezione con `raise`.
• **Catturare**: intercettare con `except` e gestire.
• **Propagare**: lasciare che l’eccezione salga lo stack fino a qualcuno che la gestisca.
• **Traceback**: la “scia” di chiamate che porta al punto dell’errore.
• **Parsing**: analizzare **stringhe** per ricavarne strutture/valori (es. `float("3.14")`).
• **EAFP**: *Easier to Ask Forgiveness than Permission* → prova e cattura.
• **LBYL**: *Look Before You Leap* → controlla prima di agire.

---

<h2 id="2">2) Anatomia di `try/except/else/finally`</h2>

```python
try:
    # solo la riga (o poche righe) che può fallire
    x = float(s)
except ValueError as e:
    # ramo di errore specifico
    print("Numero non valido:", e)
else:
    # eseguito SOLO se non ci sono eccezioni
    print("Ho convertito:", x)
finally:
    # eseguito SEMPRE (chiusure/cleanup)
    pass
```

• **`try`**: contiene l’operazione fragile.
• **`except <Tipo>`**: gestisci solo ciò che sai gestire.
• **`else`**: logica “felice” separata dal flusso d’errore.
• **`finally`**: cleanup (chiudere file/connessioni). Con i file, spesso preferisci `with`.

---

<h2 id="3">3) Dove metterle: estensione minima del `try`</h2>

**Regola d’oro:** il blocco `try` deve essere **piccolo**, mirato alla riga che può fallire.
Perché?
• Eviti di “nascondere” bug non correlati.
• Sai **cosa** ha fallito e **perché**.

🔴 Cattivo

```python
try:
    config = json.loads(Path("cfg.json").read_text())
    start_server(config)           # se crasha qui, sembra colpa del JSON
except Exception:
    print("Qualcosa è andato storto")
```

🟢 Meglio

```python
text = Path("cfg.json").read_text()
try:
    config = json.loads(text)
except json.JSONDecodeError as e:
    print("Config malformata:", e)
else:
    start_server(config)
```

---

<h2 id="4">4) Parsing di input numerico (con `,` o `.`)</h2>

```python
def parse_float(s: str, allow_comma: bool = True) -> float:
    s = s.strip()
    if allow_comma:
        s = s.replace(",", ".")
    return float(s)  # può lanciare ValueError
```

Uso interattivo con loop (UX buona, messaggi chiari):

```python
while True:
    s = input("Inserisci un numero (q per uscire): ").strip()
    if s.lower() == "q":
        print("Ciao!")
        break
    try:
        x = parse_float(s)
    except ValueError:
        print("Valore non valido. Esempi validi: 3,14  -2  1e3")
        continue

    if x > 0:   print("Positivo")
    elif x < 0: print("Negativo")
    else:       print("Zero")
```

• Qui il **parse** è `float(...)`: analizza la **stringa** secondo le regole dei numeri Python.
• L’uso di `try/except` evita il crash e migliora l’esperienza.

---

<h2 id="5">5) Validazione vs parsing (responsabilità chiare)</h2>

• **Parsing**: trasformare testo → valore (può fallire).
• **Validazione**: stabilire se il valore è **accettabile** per il tuo dominio.

```python
def parse_age(s: str) -> int:
    age = int(s)               # può lanciare ValueError
    if not (0 <= age <= 130):  # validazione dominio
        raise ValueError("Età fuori range")
    return age
```

Separare i due passi rende gli errori **comprensibili** e il codice **testabile**.

---

<h2 id="6">6) Le eccezioni più comuni (mappa mentale)</h2>

• **`ValueError`**: contenuto valido come tipo, ma **valore** sbagliato (`int("abc")`).
• **`TypeError`**: operazione con **tipo** sbagliato (`len(3)`).
• **`KeyError`**: chiave mancante in `dict`.
• **`IndexError`**: indice fuori range in liste/tuple.
• **`FileNotFoundError`**, **`PermissionError`**: file assente o accesso negato.
• **`ZeroDivisionError`**: divisione per zero.
• **`json.JSONDecodeError`**: JSON malformato.
• **`TimeoutError`** (o equivalenti libreria): operazioni scadute.

---

<h2 id="7">7) File I/O robusto: `open`, `with`, errori tipici</h2>

```python
from pathlib import Path

path = Path("data.txt")
try:
    text = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("File mancante:", path)
except PermissionError:
    print("Permessi insufficienti su", path)
else:
    print("Lettura OK, lunghezza:", len(text))
```

• Usa `with` per chiudere **sempre**:

```python
try:
    with open("out.txt", "w", encoding="utf-8") as f:
        f.write("ciao\n")
except OSError as e:  # macro-classe per I/O
    print("I/O error:", e)
```

• Evita `if path.exists()` prima di aprire (race condition): **apri e cattura** l’errore.

---

<h2 id="8">8) JSON e CSV: messaggi d’errore utili</h2>

```python
import json
from pathlib import Path

raw = Path("config.json").read_text()
try:
    cfg = json.loads(raw)
except json.JSONDecodeError as e:
    print(f"JSON non valido (riga {e.lineno}, col {e.colno}): {e.msg}")
else:
    print("Chiavi disponibili:", list(cfg))
```

CSV (valori attesi come numeri):

```python
import csv

with open("dati.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=1):
        try:
            price = float(row["price"])
        except (KeyError, ValueError) as e:
            print(f"[riga {i}] campo price non valido: {e}")
            continue
        # usa price...
```

---

<h2 id="9">9) Rete e timeouts (approccio idiomatico)</h2>

*(Esempio con `requests`; concetto valido per qualunque libreria di rete.)*

```python
import requests

try:
    r = requests.get("https://api.example.com/items", timeout=5)
    r.raise_for_status()  # lancia per HTTP 4xx/5xx
except requests.Timeout:
    print("Timeout: il server non ha risposto in tempo.")
except requests.HTTPError as e:
    print("Errore HTTP:", e.response.status_code)
except requests.RequestException as e:
    print("Errore di rete generico:", e)
else:
    data = r.json()  # può lanciare ValueError/JSONDecodeError
```

• Cattura **eccezioni specifiche** prima di quelle generiche.
• Stabilisci **timeout** espliciti.

---

<h2 id="10">10) “Lanciare” eccezioni (`raise`), `assert`, eccezioni custom</h2>

• `raise` segnala che **non puoi** proseguire:

```python
def sqrt_nonneg(x: float) -> float:
    if x < 0:
        raise ValueError("Serve un numero ≥ 0")
    return x ** 0.5
```

• `assert` è per **invarianti interne** (può essere disattivato con `-O`):

```python
def area_cerchio(r):
    assert r >= 0, "r deve essere ≥ 0"
    ...
```

• Eccezioni custom (migliorano messaggi e catch selettivo):

```python
class ConfigError(Exception):
    """Errore nella configurazione dell'app."""

def load_cfg(path):
    try:
        raw = Path(path).read_text()
        return json.loads(raw)
    except (OSError, json.JSONDecodeError) as e:
        raise ConfigError(f"Config non caricabile da {path}") from e
```

---

<h2 id="11">11) Propagazione, re-raise, chaining (`from e`), logging</h2>

• **Propagare**: non catturare se non sai cosa fare.
• **Re-raise**: dentro un `except`, se non puoi gestire davvero, usa `raise` “nudo”:

```python
try:
    ...
except SpecificError:
    log.warning("Provo fallback...")
    raise  # rilancia la stessa eccezione
```

• **Chaining**: `raise NuovaEccezione(...) from e` conserva il contesto.
• **Logging**: `logging.exception("Messaggio")` in un `except` stampa anche il traceback.

---

<h2 id="12">12) EAFP vs LBYL: quando “provare” e quando “controllare”</h2>

• **EAFP (consigliato in Python)**
Prova e cattura l’errore: più **lineare** e immune a race condition.

```python
try:
    val = d["key"]
except KeyError:
    val = default
```

• **LBYL** (utile per UX o casi economici)
Controlla prima **se** una condizione è vera, ma proteggi comunque l’operazione “vera”:

```python
if "key" in d:
    val = d["key"]   # può ancora fallire in scenari concorrenti
else:
    val = default
```

• File I/O: evita `if exists()`; **apri e gestisci l’errore**.

---

<h2 id="13">13) Performance: perché non abusarne (ma non temerle)</h2>

• Lanciare/catturare eccezioni **costa** più di un `if` → evita in **hot loops**.
• A livello applicativo, il costo è spesso **irrilevante** rispetto alla robustezza/UX.
• Non usare eccezioni per il **flusso normale** (es. per uscire da un ciclo comune).

---

<h2 id="14">14) Antipattern da evitare</h2>

• `except:` nudo (cattura anche `KeyboardInterrupt`, `SystemExit`).
• `except Exception:` che **inghiotte** tutto senza loggare.
• Blocchi `try` **enormi** che nascondono bug.
• Ignorare l’oggetto errore (`except ValueError:` e poi nessun messaggio).
• Fare roba delicata in `finally` che può **sovrascrivere** eccezioni precedenti.
• Rinomare variabili con nomi built-in (`file`, `list`, `dict`) e confondersi.

---

<h2 id="15">15) Testare le eccezioni</h2>

Con `pytest`:

```python
import pytest

def test_parse_age_invalida():
    with pytest.raises(ValueError, match="fuori range"):
        parse_age("999")
```

Testare che **si lanci** l’eccezione giusta fa parte della qualità del codice.

---

<h2 id="16">16) Esercizi guidati (falli davvero)</h2>

**A. Parser numerico “umano”**
• Scrivi `parse_decimal_it(s)` che accetta `3,14`, `-2`, `1.000,50`, spazi e segno.
• Restituisce `float`. Se invalido, `ValueError` con messaggio chiaro.
• Testa con una lista di esempi validi/invalidi.

**B. Lettura config con fallback**
• Prova a caricare `config.json`. Se manca → usa `default` e salva un `config.json` generato.
• Se c’è ma è malformato → stampa riga/colonna dell’errore e **esci** con `sys.exit(1)`.

**C. CSV robusto**
• Leggi `prezzi.csv` (`name,price`). Salta le righe con `price` invalido ma logga il problema.
• Somma i prezzi validi e stampa il totale formattato con 2 decimali.

**D. Mini-CLI**
• Con `argparse`, leggi `--amount` e `--rate`. Valida i range; in caso di errore **alza** `ArgumentTypeError` con messaggi leggibili.

---

<h2 id="17">17) Errori tipici e soluzioni rapide</h2>

• “Non capisco perché `except` non entra” → il `try` è **troppo grande** o catturi il **tipo sbagliato**.
• “Ho preso la chiave ma a volte crasha” → concorrenza: preferisci **EAFP** e cattura `KeyError`.
• “Il programma non chiude il file” → usa `with open(...)`.
• “Messaggi d’errore inutili” → includi `as e` e stampa parti salienti (`e.args`, riga/colonna per JSON).

---

<h2 id="18">18) Cheatsheet finale</h2>

```python
# try/except minimo e mirato
try:
    x = float(s)
except ValueError as e:
    print("Numero non valido:", e)

# else/finally
try:
    resource = acquire()
except ResourceError:
    recover()
else:
    use(resource)
finally:
    release(resource)

# re-raise e chaining
try:
    ...
except LowLevelError as e:
    raise HighLevelError("contesto utile") from e

# file I/O
from pathlib import Path
try:
    text = Path("file.txt").read_text(encoding="utf-8")
except FileNotFoundError:
    text = ""

# JSON con coordinate errore
try:
    obj = json.loads(text)
except json.JSONDecodeError as e:
    print(f"JSON errato (riga {e.lineno}, col {e.colno}): {e.msg}")

# dict: EAFP
try:
    value = d["k"]
except KeyError:
    value = default
```

---

<h2 id="19">19) Riepilogo in una riga</h2>

**Scrivi blocchi `try` piccoli, cattura eccezioni specifiche, separa il percorso felice (`else`) dal recupero errori (`except`), usa `with` per il cleanup, ed abbraccia lo stile EAFP quando i pre-controlli sono fragili o verbosi.**