# Git — appunti “da campo” (approfonditi, pratici, con esempi)

> Obiettivo: andare **oltre le basi**. Capire *come* Git funziona, *quando* scegliere merge/rebase, *come* risolvere conflitti in fretta, e *come* usare al meglio GitHub (PR, Actions, Pages).

---

## 🧭 Mappa rapida (concetti chiave)

- **Repository** = cartella con `.git/` (database degli oggetti + index).
- **Oggetti Git**:  
  - **blob** (contenuto file), **tree** (directory), **commit** (snapshot + metadati), **tag** (etichetta su commit).  
- **Commit** = snapshot immutabile → referenziato da SHA.  
- **HEAD** = puntatore al branch corrente (o a un commit se “detached”).  
- **Index / Staging** = “lista della spesa” del *prossimo commit*.  
- **Remote** (es. `origin`) = copia su GitHub.  
- **Branch** = etichetta che punta a un commit (si muove ad ogni commit).

> Mental model: Git è un **grafo aciclico** di commit. Branch e tag sono solo *etichette* su nodi del grafo.

---

## ⚙️ Setup raffinato (una volta)

```bash
git config --global user.name  "Il Tuo Nome"
git config --global user.email "tu@email.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --global pull.rebase true         # storia lineare di default
git config --global rebase.autoStash true    # stash automatico durante rebase/pull
# Fine line endings (consiglio: mac/linux)
git config --global core.autocrlf input
# (Windows spesso:)
# git config --global core.autocrlf true
```

**SSH** (evita password):
```bash
ssh-keygen -t ed25519 -C "tu@email.com"
# copia ~/.ssh/id_ed25519.pub in GitHub → Settings → SSH and GPG keys
```

Alias utili:
```bash
git config --global alias.st "status -sb"
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.co "checkout"
git config --global alias.br "branch"
```

---

## 🧪 Basi solide (con chiarimenti richiesti)

### Clonare nella cartella dove vuoi lavorare/pubblicare
```bash
git clone <URL>   # es: git@github.com:utente/repo.git
cd repo
```

### Cosa fa `git add file.example`?
- **Staggia** la versione *attuale* di `file.example` (prepara al prossimo commit).  
- Non crea commit, non pusha.  
- Se è nuovo → inizia a tracciarlo; se è già tracciato → aggiunge le modifiche; se è in `.gitignore` → viene ignorato (forza con `-f`).

Togli dallo stage:
```bash
git restore --staged file.example
```

### Commit singolo vs commit “tutti i tracciati”
```bash
git commit -m "msg"      # committa ciò che è in stage (file nuovi inclusi)
git commit -am "msg"     # committa TUTTE le modifiche ai file già tracciati
                         # (non include file nuovi non 'add'-ati)
```

### Pubblicare davvero online
Finché non fai `push`, tutto resta **in locale**:
```bash
git commit -m "message"
git push
```

### Vedere cosa è cambiato
```bash
git status            # file modificati, non tracciati, staged
git diff              # differenze non staged
git diff --staged     # differenze staged
```

---

## 🔁 Sincronizzare con il remoto (e il messaggio “divergent branches”)

- **`git fetch`**: aggiorna riferimenti remoti (non tocca file locali).  
- **`git pull`**: `fetch` + integra (merge/rebase).

Se Git dice:
```
hint: You have divergent branches and need to specify how to reconcile them.
```
Scegli lo stile (una volta per tutte):
```bash
# consigliato: rebase lineare
git config --global pull.rebase true
# oppure merge classico
git config --global pull.rebase false
# oppure consenti solo fast-forward
git config --global pull.ff only
```

Uso puntuale:
```bash
git pull --rebase    # lineare
git pull --no-rebase # merge
git pull --ff-only   # solo fast-forward (fallisce se divergono)
```

---

## 🔀 Merge vs Rebase (scelte consapevoli)

| Strategia         | Quando usarla                                 | Pro                                   | Contro/Note                                 |
|-------------------|-----------------------------------------------|----------------------------------------|---------------------------------------------|
| **Merge**         | Integrare branch *pubblici* o team numerosi   | Non riscrive storia, sicuro            | Commit di merge, storia “ramificata”        |
| **Rebase**        | Pulire branch *privati* prima della PR        | Storia lineare, facile da leggere      | Riscrive commit → non su storia condivisa   |
| **Squash merge**  | Accorpare commit “rumorosi” in PR             | 1 commit pulito su `main`              | Perdi granularità dei commit della feature  |
| **FF-only**       | Solo avanzamenti lineari                       | Storia senza commit di merge           | Fallisce se serve un merge/rebase           |

Comandi tipici:
```bash
# Merge
git switch main
git pull
git merge feature/x

# Rebase (pulizia di feature/x)
git switch feature/x
git fetch origin
git rebase origin/main
# risolvi conflitti → git add … → git rebase --continue
```

---

## 🧱 Merge conflicts (veloce & bene)

Esempio:
```txt
a = 1
<<<<<<< HEAD
b = 2
=======
b = 3
>>>>>>> 56782736387980937883
c = 3
```
Passi:
```bash
# 1) modifica i file, scegli cosa tenere, rimuovi i marker
git add <file_risolto>
# 2) se rebase:
git rebase --continue
#    se merge:
git commit
# Se serve annullare:
# git rebase --abort  |  git merge --abort
```

Tool utili: VS Code Merge Editor (“Accept Current/Incoming/Both”).  
Trucchi nel file in conflitto:
```bash
# prendi la tua versione
git checkout --ours   -- path/file
# prendi la versione remota
git checkout --theirs -- path/file
```

---

## 🧳 Stash avanzato

```bash
git stash           # salva modifiche tracciate
git stash -u        # include non tracciati (untracked)
git stash -a        # include anche ignorati (attenzione!)
git stash pop       # applica + rimuovi dallo stash
git stash apply     # applica e lascia nello stash
git stash branch feature/esperimento   # crea branch da quello stash
```

Opzioni utili:
```bash
git stash --keep-index   # stasha solo ciò che NON è staged
git stash -p             # interattivo (a pezzi)
```

---

## 🧰 Tornare indietro in sicurezza

```bash
# scarta modifiche non committate
git restore file.txt
git restore --source=HEAD -- .

# annulla un commit (NON riscrive storia)
git revert <sha>

# riscrivi storia locale (ATTENZIONE)
git reset --soft  <sha>    # tiene staging & working
git reset --mixed <sha>    # default: svuota staging
git reset --hard  <sha>    # PERDE modifiche locali
git reset --hard origin/main   # riallinea alla versione remota
# (vecchi repo: origin/master)
```

Paracadute:
```bash
git reflog   # recupera SHA “persi” dopo reset/checkout
```

---

## 🧭 Branching pro & HEAD

Perché **branch**: lavorare su feature/bugfix senza toccare `main`, aprire PR, fare review, fare rollback mirati.

```bash
git branch                  # elenco (asterisco = corrente)
git checkout -b feature/x   # crea & passa (oppure: git switch -c feature/x)
git checkout main           # torna (oppure: git switch main)
git merge feature/x         # integra in main
git branch -d feature/x     # elimina (se mergiato)
git push -u origin feature/x # collega branch remoto
```

**HEAD**:
- Punta al branch attivo (es. `refs/heads/main`).  
- *Detached HEAD*: sei “su un commit” (es. dopo `git checkout <sha>`). Crea un branch se vuoi continuare lì:
```bash
git switch -c hotfix/quick
```

---

## 🔎 Log & selezioni potenti (per capire *cosa* è successo)

```bash
git log --oneline --graph --decorate --all
git log --since="2 weeks ago" -- path/file
git show <sha>
git diff A..B         # differenze dei contenuti tra A e B
git log A..B          # commit raggiungibili da B ma non da A
git log A...B         # commit che differenziano A e B (symmetric diff)
# genitori:
git show HEAD^        # il primo genitore
git show HEAD~2       # due commit indietro
```

Statistiche:
```bash
git shortlog -sn      # autori e numero commit
git blame -L 10,30 file.txt   # chi ha toccato righe 10..30
```

---

## ✍️ Rifinire la storia (amend, autosquash, cherry-pick, bisect)

```bash
git commit --amend               # modifica l'ultimo commit (msg o contenuto)
git commit -m "fixup! <msg>"     # crea commit di fix
git rebase -i --autosquash origin/main   # unisce i fixup! automaticamente

git cherry-pick <sha>            # porta un commit specifico sul branch attuale

# trovare il commit “colpevole”
git bisect start
git bisect bad
git bisect good <sha_buono>
# → testi suggeriti da Git → good/bad finché isoli il commit
git bisect reset
```

---

## 🧹 `.gitignore` & `.gitattributes` (qualità di vita)

`.gitignore` (esempio):
```gitignore
.DS_Store
.vscode/
node_modules/
dist/
.env
```
Hai già committato roba da ignorare?
```bash
git rm -r --cached path/da/ignorare
echo "path/da/ignorare" >> .gitignore
```

`.gitattributes` (line endings, linguaggi, LFS):
```gitattributes
* text=auto
*.sh text eol=lf
# LFS (es.)
*.psd filter=lfs diff=lfs merge=lfs -text
```

---

## 🏷️ Tag, release & firma

```bash
git tag -a v1.2.0 -m "Release 1.2.0"
git push origin v1.2.0
git push --follow-tags  # push commit + tag annotati

# Firma (GPG) per “Verified”
git tag -s v1.2.0 -m "signed"
git verify-tag v1.2.0
git config --global user.signingkey <GPG_KEY_ID>
git commit -S -m "feat: commit firmato"
```

`git describe --tags` → utile per build/versioni.

---

## 📦 Submodule, Subtree, LFS (quando e perché)

- **Submodule**: include un repo come dipendenza “fissata” a un commit.  
  Pro: allinea versioni; Contro: flusso più complesso.
  ```bash
  git submodule add <URL> path/
  git submodule update --init --recursive
  ```
- **Subtree**: copia codice esterno *vendorizzato* (più semplice da usare).  
- **Git LFS**: traccia file binari grandi senza gonfiare la storia.
  ```bash
  git lfs install
  git lfs track "*.psd"
  git add .gitattributes
  git commit -m "chore: track psd via LFS"
  ```

---

## 🧼 Manutenzione & pulizia

```bash
git fetch -p                       # prune: rimuove riferimenti a branch remoti cancellati
git branch -d vecchio/branch       # elimina locale (sicuro)
git branch -D branch               # forza eliminazione locale
git push origin --delete branch    # elimina remoto
git gc                             # garbage collection (pulizia interna)
```

---

## 🧩 GitHub al meglio: PR, protezioni, Actions, Pages

**Pull Request (PR) flow “pulito”**
1. `git checkout -b feature/x`
2. commit piccoli + messaggi chiari
3. rebase su `origin/main` prima della PR
4. apri PR con descrizione, checklist, screenshot/test
5. **Squash merge** in `main` (storia pulita)

**Branch protection (Settings → Branches):**
- Richiedi PR, status checks (CI), code review, niente force-push su `main`.

**PR/Issue template (nella repo):**
```
.github/PULL_REQUEST_TEMPLATE.md
.github/ISSUE_TEMPLATE/bug_report.md
```

**CODEOWNERS** (review automatiche):
```
# .github/CODEOWNERS
src/auth/*  @team-auth
```

**GitHub Actions** (CI base):
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm ci
      - run: npm run lint && npm test --if-present
```

**GitHub Pages**:
- Repo statico con `index.html`.
- Settings → Pages → Branch `main` → salva → attendi URL.  
  (Oppure usa Action dedicata per generare branch `gh-pages`.)

---

## 🧠 FAQ veloci (punti che spesso confondono)

- **“Non ho fatto `git add`, quindi il file ‘rimane .gitignore’?”**  
  No. “Non staged” **≠** “ignorato**”. `.gitignore` è una lista di **esclusione**; lo staging è **selezione** per il commit.

- **`git reset --hard origin/master` vs `origin/main`**  
  I repo moderni usano `main`. Usa quello che vedi su GitHub.

- **Ho fatto `--amend` e ora non posso pushare**  
  Hai riscritto la storia: fai `git push --force-with-lease` *sul tuo branch*, non su `main`.

- **Rinominare/spostare file**  
  Git lo rileva automaticamente nei diff; puoi anche esplicitarlo: `git mv old new`.

- **Lavorare su più branch in parallelo senza cambiare cartella**  
  Usa **worktree**:
  ```bash
  git worktree add ../repo-feature feature/x
  ```

---

## 📋 Mini-cheatsheet (avanzato)

```bash
# Status/diff/log
git st
git diff --stat
git lg
git log -p -- path/file

# Staging preciso
git add -p path/file
git restore -p path/file

# Commit & refine
git commit --amend
git commit -m "fixup! corregge X"
git rebase -i --autosquash origin/main

# Sync
git fetch -p
git pull --rebase
git push -u origin <branch>

# Conflicts helpers
git checkout --ours   -- path/file
git checkout --theirs -- path/file

# Undo
git revert <sha>
git reset --hard origin/main
git reflog

# Branching
git checkout -b feature/x
git merge feature/x
git branch -d feature/x
git push origin --delete feature/x

# Tags/release
git tag -a v1.3.0 -m "release"
git push --follow-tags
git describe --tags
```

---

### Conclusione
Con questa cassetta degli attrezzi puoi:
- Lavorare *pulito* su feature branch,
- Tenere la **storia lineare** (rebase) o **esplicita** (merge),
- Risolvere conflitti velocemente,
- Pubblicare con PR protette da CI,
- Tornare indietro **in sicurezza** quando serve.

Se vuoi, preparo anche una **cheatsheet A4** “Git Pro” o uno **script di dotfiles** per applicare tutte le config su un nuovo Mac/PC.
