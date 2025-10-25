# Git — appunti “da campo” (lineari, pratici, con immagini)

> Obiettivo: mappa mentale chiara + flusso quotidiano dei comandi, per lavorare bene da solo o in team (CS50/CS50W & GitHub).

---

## Indice
1. Introduzione: Git vs GitHub  
2. Setup iniziale  
3. Creare o clonare un repository  
4. Flusso locale: `status → add → commit → push`  
5. Staging spiegato: cosa fa `git add file.example`  
6. Commit: `-m` vs `-am` (pro & contro)  
7. Pubblicare online: `git push`  
8. Sincronizzare: `git fetch` / `git pull` + *divergent branches*  
9. Merge vs Rebase vs Fast-Forward (quando usare cosa)  
10. .gitignore (e come rimediare agli errori)  
11. Ispezione: `status`, `diff`, `log`, `show`, `blame`  
12. Tornare indietro: `restore`, `revert`, `reset`, `reflog`  
13. Branching e HEAD (concetto, utilità, potenziale)  
14. Merge conflicts (riconoscerli e risolverli)  
15. Funzioni utili di GitHub (Fork, PR, Pages)  
16. Mini-cheatsheet

---

## 1) Introduzione: Git vs GitHub

- **Git**: sistema di *version control* da riga di comando.  
  - Salva **snapshot** del codice (commit), permette **branch** separati, **merge/rebase**, **undo** sicuri.
- **GitHub**: sito che ospita repo Git **remoti** (sincronizzazione, PR, issues, Pages, ecc).

> Repository = cartella con `.git/` (tutta la storia). Può essere **locale** (tuo PC) o **remoto** (GitHub).

---

## 2) Setup iniziale (una volta)

```bash
git config --global user.name  "Il Tuo Nome"
git config --global user.email "tu@email.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"  # VS Code per messaggi
# (consigliato) Pull lineare
git config --global pull.rebase true
git config --global rebase.autoStash true
```

**SSH (niente password):**
```bash
ssh-keygen -t ed25519 -C "tu@email.com"
# copia ~/.ssh/id_ed25519.pub su GitHub → Settings → SSH Keys
```

---

## 3) Creare o clonare un repository

**Nuovo repo locale**
```bash
mkdir progetto && cd progetto
git init
```

**Clonare il repo remoto nella cartella dove vuoi lavorare/pubblicare**
```bash
git clone <URL>   # es: git@github.com:utente/repo.git  (SSH)
cd repo
```

> TIP (tempo/spazio): `git clone --depth=1 …` (shallow) • `git sparse-checkout set path/` (solo sottocartelle)

---

## 4) Flusso locale: `status → add → commit → push`

```bash
git status
git add file1 file2      # oppure: git add .
git commit -m "feat: messaggio chiaro"
git push                 # primo push?  git push -u origin <branch>
```

**Messaggi leggibili** (Conventional Commits): `feat: ...` • `fix: ...` • `docs: ...` • `refactor: ...`

> TIP: `git add -p` per committare “a pezzetti” in modo logico.

---

## 5) Staging spiegato: cosa fa `git add file.example`

- **`git add file.example`** mette **la versione attuale** del file nell’**staging area** ⇒ pronta per il **prossimo commit**.  
- Non crea un commit, non invia su GitHub.
- Se il file era:
  - **nuovo** → diventa tracciato e staged;
  - **modificato** → le modifiche correnti vanno in stage;
  - **in `.gitignore`** → viene saltato (forza con `git add -f`).

Togli dallo stage: `git restore --staged file.example`.

---

## 6) Commit: `-m` vs `-am`

```bash
git commit -m "msg"        # committa ciò che è in stage (anche file nuovi)
git commit -am "msg"       # committa TUTTE le modifiche ai file già tracciati
                           # (non include file nuovi non ancora 'add')
```

---

## 7) Pubblicare online: `git push`

Finché non fai `git push`, i tuoi commit restano **solo in locale**.
```bash
git commit -m "message"
git push
```

---

## 8) Sincronizzare: `git fetch` / `git pull` + *divergent branches*

- **`git fetch`**: aggiorna i riferimenti remoti, non tocca i file locali.  
- **`git pull`**: `fetch` + integra (merge o rebase).

Se vedi:
```
hint: You have divergent branches and need to specify how to reconcile them.
```
Scegli uno stile:

```bash
# (consigliato) rebase lineare
git pull --rebase

# oppure: merge classico
git pull --no-rebase

# oppure: solo fast-forward (fallisce se serve merge)
git pull --ff-only
```

Imposta il **default** per tutti i repo:
```bash
git config --global pull.rebase true        # rebase
# o
git config --global pull.rebase false       # merge
# o
git config --global pull.ff only            # fast-forward only
```

---

## 9) Merge vs Rebase vs Fast-Forward

| Strategia        | Pro                         | Contro / Note                           | Comando tipico                |
|------------------|-----------------------------|-----------------------------------------|--------------------------------|
| **Merge**        | Sicuro, conserva la storia  | Storia “ramificata” con commit di merge | `git merge feature/x`         |
| **Rebase**       | Storia lineare e pulita     | Riscrive commit del branch              | `git rebase origin/main`      |
| **Fast-Forward** | Nessun commit extra         | Fallisce se i rami sono divergenti      | `git pull --ff-only`          |

> Regola pratica: rebase per pulire i **tuoi** branch prima della PR. Evita di rebase-are storia **già condivisa**.

---

## 10) `.gitignore` (cosa non tracciare)

```gitignore
# OS / editor
.DS_Store
.vscode/

# build / dipendenze
node_modules/
dist/
.env
```

Hai già committato qualcosa da ignorare?
```bash
git rm -r --cached path/da/ignorare
echo "path/da/ignorare" >> .gitignore
```

---

## 11) Ispezione: `status`, `diff`, `log`, `show`, `blame`

```bash
git status -sb
git diff                 # differenze non staged
git diff --staged        # differenze staged
git log --oneline --graph --decorate --all
git show <sha>           # dettaglio commit
git blame file.txt       # chi/quando ha cambiato ogni riga
```

Alias utili:
```bash
git config --global alias.st "status -sb"
git config --global alias.lg "log --oneline --graph --decorate --all"
```

---

## 12) Tornare indietro: `restore`, `revert`, `reset`, `reflog`

- **Scartare modifiche non committate**  
  ```bash
  git restore file.txt
  git restore --source=HEAD -- .
  ```
- **Annullare un commit preservando la storia (sicuro)**  
  ```bash
  git revert <sha>
  ```
- **Riscrivere la storia locale (attenzione!)**  
  ```bash
  git reset --soft  <sha>   # tieni staging & working
  git reset --mixed <sha>   # default: tieni working, svuota staging
  git reset --hard  <sha>   # PERDITA modifiche locali
  ```
- **Allinearsi esattamente al remoto**  
  ```bash
  git reset --hard origin/main     # (o origin/master su repo vecchi)
  ```
- **Paracadute**  
  ```bash
  git reflog    # recupera SHA “persi” dopo reset/checkout
  ```

> Se hai committato segreti: usa `git filter-repo` o **BFG** e **revoca** le credenziali.

---

## 13) Branching e HEAD (concetto, utilità, potenziale)

- **Branch**: linea di sviluppo indipendente (nuove feature, bugfix), poi **merge/rebase** in `main`.  
- **HEAD**: puntatore al commit/branch su cui stai lavorando.

Comandi base:
```bash
git branch                    # elenco (asterisco = branch corrente)
git checkout -b feature/x     # Crea + passa al nuovo branch  (equivale a:)
# git switch -c feature/x
git checkout main             # torna a main  (equivale a: git switch main)
git merge feature/x           # unisci in main
git branch -d feature/x       # elimina branch (se mergiato)
```

Immagini utili:
- *No branch vs feature branch*: vedi `no_branch.png` e `branch.png`
- *Multi-user sync*: `mult_users.png`

---

## 14) Merge conflicts (riconoscerli e risolverli)

Esempio di conflitto:
```txt
a = 1
<<<<<<< HEAD
b = 2
=======
b = 3
>>>>>>> 56782736387980937883
c = 3
d = 4
```

**Risoluzione (passi):**
1. Apri i file, scegli cosa tenere, **rimuovi i marker** `<<<<<<< ======= >>>>>>>`.
2. `git add <file_risolto>`
3. Continua l’operazione:
   - se era **rebase**: `git rebase --continue`
   - se era **merge**:  `git commit`
4. In difficoltà? `git merge --abort` o `git rebase --abort`.

Editor come **VS Code Merge Editor** offrono “Accept Current / Incoming / Both”.

---

## 15) Funzioni utili di GitHub

- **Fork**: tua copia di un repo altrui (per proporre modifiche).
- **Pull Request**: chiedi di unire i tuoi cambi al repo originale (review, CI).
- **GitHub Pages** (pubblica un sito statico):
  1. Crea repo con `index.html`
  2. `git push`
  3. Repo → **Settings → Pages** → scegli branch (es. `main`)  
  4. Attendi l’URL pubblicato.

---

## 16) Mini-cheatsheet (copia/incolla)

```bash
# Inizializza / Clona
git init
git clone <URL>

# Stato e differenze
git status -sb
git diff
git diff --staged

# Aggiungi e committa
git add -p
git commit -m "feat: descrizione"
git commit -am "fix: solo file già tracciati"

# Pubblica
git push -u origin <branch>

# Sincronizza
git fetch
git pull --rebase    # o --no-rebase / --ff-only

# Branching
git checkout -b feature/x
git checkout main
git merge feature/x
git branch -d feature/x

# Undo (sicuri)
git restore file.txt
git restore --staged file.txt
git revert <sha>

# Reset (con cautela)
git reset --hard origin/main
# o a uno SHA specifico:
git reset --hard <sha>

# Log e ispezione
git lg
git show <sha>
git blame file.txt
```