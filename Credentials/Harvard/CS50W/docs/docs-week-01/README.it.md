# Git — appunti “da campo” (con tips e approfondimenti)

> **Obiettivo:** darti una mappa mentale chiara + un flusso di comandi quotidiani, con note pratiche per evitare errori comuni. Perfetto per CS50/CS50W e GitHub.

---

## 🧠 Modello mentale (la base per capire tutto)

- **Repository** = cartella con una sottocartella nascosta `.git/` che contiene tutta la **storia**.
- **Commit** = uno “snapshot” immutabile dei file **versionati** + un messaggio.
- **HEAD** = puntatore al **commit attuale** (di solito punta a un **branch**).
- **Branch** = un’etichetta (es. `main`, `develop`, `feature/login`) che punta a un commit; ad ogni commit il puntatore “avanza”.
- **Working tree vs Staging area vs Repository**
  - *Working tree*: i file reali sul disco.
  - *Staging (index)*: l’elenco di “cosa finirà nel prossimo commit”.
  - *Repository*: la storia salvata (commit passati).
- **Remoto (`origin`)** = copia ospitata su server (GitHub, GitLab…). Le **traccianti** collegano branch locali/remoti (es. `main` ↔ `origin/main`).

> **TIP:** pensa a Git come a un grafo di commit collegati (DAG). Branch e tag sono solo “etichette” che puntano a nodi del grafo.

---

## ⚙️ Setup iniziale (fallo una volta)

```bash
git config --global user.name  "Il Tuo Nome"
git config --global user.email "tu@email.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"   # VS Code come editor dei messaggi
```

> **TIP (SSH, niente password):**
> 1. `ssh-keygen -t ed25519 -C "tu@email.com"`
> 2. Copia `~/.ssh/id_ed25519.pub` in GitHub → **Settings → SSH keys**
> 3. `git remote set-url origin git@github.com:utente/repo.git`

---

## 🏁 Creare o clonare un repo

**Nuovo repo da zero**
```bash
mkdir progetto && cd progetto
git init
```

**Clonare un repo esistente**
```bash
git clone git@github.com:utente/repo.git
cd repo
```

> **TIP (tempo/spazio):**
> - *Shallow clone*: `git clone --depth=1 …`
> - *Sparse checkout* (solo alcune cartelle): `git sparse-checkout set path/`

---

## 🔁 Ciclo quotidiano (status → add → commit → push)

```bash
git status                 # cosa è cambiato?
git add file1 file2        # oppure: git add .   (tutti i cambi)
git commit -m "feat: messaggio chiaro"
git push                   # se primo push: git push -u origin <branch>
```

**Messaggi di commit**: sii descrittivo. Convenzione utile: **Conventional Commits**
- `feat:` aggiunge…
- `fix:` risolve…
- `docs:` aggiorna…
- `refactor:` modifica senza cambiare comportamento…

> **TIP:** usa `git add -p` per “spezzare” cambi grandi in commit piccoli e logici.

---

## 🌿 Branching e navigazione

```bash
git branch                 # lista
git switch -c feature/x    # crea e passa a un branch
git switch main            # torna a main
git branch -d feature/x    # elimina (se già mergiato)
```

> **TIP:** evita di lavorare su `main`. Crea sempre un branch funzionale: `feature/...`, `bugfix/...`.

---

## 🔀 Merge vs Rebase (e cosa scegliere)

**Merge** (sicuro, conserva la storia “ramificata”):
```bash
git switch main
git pull
git merge feature/x        # crea un commit di merge (o fast-forward se possibile)
```

**Rebase** (storia più lineare, ma riscrive i commit del branch):
```bash
git switch feature/x
git fetch origin
git rebase origin/main     # “riapplica” i tuoi commit sopra all’ultimo main
# risolvi conflitti, poi:
git rebase --continue
```

**Regola pratica**
- Rebase per pulire i **tuoi** branch prima della PR.
- **Mai** rebase su branch **già condivisi** (rischio divergenza remota).
- Su `main` preferisci merge “fast-forward” o **squash-merge** via PR.

---

## 🤝 Remoti, fetch, pull, tracking

**Collega un remoto (se serve):**
```bash
git remote add origin git@github.com:utente/repo.git
```

**Aggiornare riferimenti remoti:**
```bash
git fetch                   # scarica info nuove (non modifica il working tree)
git pull                    # = fetch + merge (o rebase se config: pull.rebase=true)
```

**Impostare il tracking al primo push:**
```bash
git push -u origin feature/x
```

> **TIP:** preferisci `git fetch` +  
> `git log --oneline --graph --decorate --all`  
> per **vedere** cosa cambierebbe prima di fare `pull`.

---

## 🧹 `.gitignore` (cosa NON tracciare)

Crea un file `.gitignore` alla radice:

```gitignore
# OS / editor
.DS_Store
.vscode/

# dipendenze / build
node_modules/
dist/
.env
```

> **TIP (se hai già aggiunto per errore):**
> ```bash
> git rm -r --cached path/da/ignorare
> echo "path/da/ignorare" >> .gitignore
> ```

---

## 🆘 Tornare indietro in sicurezza

**Scarta modifiche non aggiunte (working tree):**
```bash
git restore file.txt                 # singolo file
git restore --source=HEAD -- .       # tutto com’era a HEAD
```

**Togli dal palco (staging → working):**
```bash
git restore --staged file.txt
```

**Annulla un commit già pubblicato (sicuro):**
```bash
git revert <sha>                     # crea un nuovo commit “inverso”
```

**Reset (riscrive la storia locale, attento!):**
```bash
git reset --soft  <sha>   # conserva staging e working
git reset --mixed <sha>   # default: conserva working, svuota staging
git reset --hard  <sha>   # PERDITA modifiche locali
```

**Paracadute finale**: `git reflog` mostra **tutti** i movimenti di HEAD (anche dopo reset).  
Puoi recuperare uno SHA “perso” e fare `git reset --hard <sha>`.

> **TIP (se hai committato una password):** usa `git filter-repo` / **BFG Repo-Cleaner** per **riscrivere la storia** e *invalida* subito la chiave/secret.

---

## 🧳 Stash (parcheggia lavori in corso)

```bash
git stash            # salva rapido
git stash list
git stash apply      # riapplica (mantiene lo stash)
git stash pop        # riapplica + rimuovi dallo stash
git stash -p         # interattivo (a pezzi)
```

> **TIP:** utile quando devi cambiare branch “al volo” senza committare lavoro sporco.

---

## 🔎 Ispezionare la storia e i diff

```bash
git log --oneline --graph --decorate --all
git show <sha>                 # dettagli di un commit
git diff                       # differenze non staggate
git diff --staged              # differenze già in staging
git blame file.txt             # chi/quando ha cambiato ogni riga
```

> **TIP (alias utili):**
> ```bash
> git config --global alias.lg "log --oneline --graph --decorate --all"
> git config --global alias.st "status -sb"
> ```

---

## 🏷️ Tag e release

**Tag leggeri vs annotati** (meglio annotati per release):
```bash
git tag -a v1.0.0 -m "Prima release"
git push origin v1.0.0
```

> **TIP:** segui **SemVer** (`MAJOR.MINOR.PATCH`). Su GitHub puoi creare una **Release** a partire da un tag.

---

## 🧪 Rebase interattivo, squash, cherry-pick, bisect

**Pulire la storia del tuo branch:**
```bash
git rebase -i origin/main
# usa 's' (squash) o 'f' (fixup) per unire commit piccoli
```

**Portare un commit specifico su un altro branch:**
```bash
git cherry-pick <sha>
```

**Trovare il commit che ha introdotto un bug:**
```bash
git bisect start
git bisect bad                     # il commit attuale è “rotto”
git bisect good <sha_buono>        # commit noto come “buono”
# Git propone commit intermedi → testi → 'good' o 'bad' finché trova il colpevole
git bisect reset
```

---

## 🪝 Git Hooks (automatizza controlli)

- Posizione: `.git/hooks/` (esempi `.sample`).
- Usa **pre-commit** per lint/test automatici prima del commit (o strumenti come **Husky** in progetti JS).

---

## 🤏 Submodule, subtree, LFS (quando servono)

- **Submodule**: includi un repo dentro un altro (versionato a un commit). Complicano i flussi.
- **Subtree**: alternativa più semplice per *vendorizzare* codice esterno.
- **Git LFS**: per file binari pesanti (media, dataset) senza “gonfiare” la storia.

> **Consiglio:** se puoi, **evita** submodule finché non ne hai davvero bisogno.

---

## 🧭 Workflow consigliati

- **Feature Branch + PR (consigliato)**  
  Crea branch dalla `main` → sviluppa → test → PR → code review → merge (preferibilmente **squash merge** per una storia pulita).
- **Git Flow** (più “pesante”) con `develop`, `release/*`, `hotfix/*`.
- **Trunk-Based** (team molto agili) con PR piccole e frequenti.

> **TIP:** per CS50/CS50W o progetti personali, **Feature Branch + PR** è lo standard più semplice e pulito.

---

## 🧱 Risoluzione conflitti (passo–passo)

1. `git pull` o `git rebase` e compaiono i conflitti.
2. Apri i file: cerca i marker `<<<<<<<`, `=======`, `>>>>>>>`.
3. Unisci le parti giuste, rimuovi i marker.
4. `git add <file_risolto>`
5. Se sei in rebase: `git rebase --continue`. In merge: `git commit`.

> **TIP:** strumenti come **VS Code Merge Editor** velocizzano i conflitti.

---

## 🛡️ Errori comuni e fix veloci

- **“detached HEAD”**: stai guardando un commit/tag, non un branch → `git switch -c fix/qualcosa`.
- **“non-fast-forward” al push**: il remoto ha commit che non hai → `git pull --rebase` (oppure `git fetch` + rebase/merge manuale) e poi riprova.
- **Hai pushato roba privata**: *revoca credenziali subito* e riscrivi la storia con `git filter-repo` / **BFG**. Poi `git push --force-with-lease`.

---

## 📋 Checklist “prima di pushare”

- `git status` pulito?
- Commit piccoli, con messaggi chiari?
- Niente file sensibili o build? `.gitignore` ok?
- `git pull --rebase` **oppure** `git fetch` + rebase per allinearti a `origin/main`?
- Test/lint passano?

---

## 🛠️ Mini-cheatsheet (copiaincolla rapido)

```bash
# Inizializza / Clona
git init
git clone git@github.com:utente/repo.git

# Stato e differenze
git status -sb
git diff
git diff --staged

# Aggiungi e committa
git add -p
git commit -m "feat: descrizione corta ma chiara"

# Branch
git switch -c feature/x
git switch main
git branch -d feature/x

# Sincronizzazione
git fetch
git pull --rebase
git push -u origin feature/x

# Merge/Rebase
git switch main && git pull
git merge feature/x
# oppure
git switch feature/x
git rebase origin/main

# Undo (sicuri)
git restore file.txt
git restore --staged file.txt
git revert <sha>

# Reset (con cautela)
git reset --soft <sha>
git reset --mixed <sha>
git reset --hard <sha>

# Stash
git stash
git stash pop

# Log e ispezione
git lg     # se hai creato l'alias
git log --oneline --graph --decorate --all
git show <sha>
git blame file.txt

# Tag
git tag -a v1.0.0 -m "release"
git push origin v1.0.0
```

---

## 🔧 Alias utili da impostare

```bash
git config --global alias.st "status -sb"
git config --global alias.ci "commit"
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global pull.rebase true
```

---

## 🎯 Esempio concreto (stile CS50W: branch progetto)

```bash
# 1) Clona il tuo me50 / repo corso
git clone git@github.com:me50/USERNAME.git
cd USERNAME

# 2) Crea il branch richiesto
git switch -c web50/projects/2020/x/search

# 3) Copia i file del progetto (in root del branch), poi:
git add .
git commit -m "feat: project0 search - struttura base"
git push -u origin web50/projects/2020/x/search
```

> **TIP (allineare il branch con main):**
> ```bash
> git fetch origin
> git switch web50/projects/2020/x/search
> git rebase origin/main
> # risolvi eventuali conflitti → add → rebase --continue
> git push --force-with-lease
> ```

---

## 💡 Micro-tips finali

- **Commits atomici**: un’idea per commit → più facile fare review e rollback.
- **Force push**: solo sui **tuoi** branch in PR e sempre `--force-with-lease`.
- **Proteggi `main`** su GitHub con branch protection + require PR.
- **Template PR** e **CI** (lint/test) evitano regressioni.
- **Chiavi SSH separate** se usi più account GitHub (work/personal).
