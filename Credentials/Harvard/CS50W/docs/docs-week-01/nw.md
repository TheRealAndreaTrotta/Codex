# Git e GitHub — lezione completa “da zero”

Questa è una lezione pensata per chi **non ha mai usato Git o GitHub**. Partiamo dal problema che risolvono, capiamo i concetti uno alla volta e poi li mettiamo in pratica con comandi reali. Alla fine avrai un flusso di lavoro quotidiano chiaro e saprai cosa fare quando qualcosa “si incastra”.

---

# Indice della lezione

1. Introduzione: perché esistono Git e GitHub
2. Concetti fondamentali

   * Repository, Working tree, Staging area
   * Commit, HEAD, Branch, Remote
3. Installazione e prima configurazione

   * Config di base
   * Accesso SSH a GitHub
   * Alias utili
4. Creare o clonare un repository

   * Nuovo repo locale
   * Nuovo repo su GitHub e collegamento `origin`
   * Clonare un repo già online
5. Il ciclo di lavoro base

   * `git status` → `git add` → `git commit` → `git push`
6. `git add` spiegato

   * Cosa mette in stage, casi tipici, rimuovere dallo stage
7. `git commit` in dettaglio

   * `-m` (message), `-a` (all tracked), `-am` combinato, `--amend`
8. `.gitignore`

   * Cosa ignorare, come rimediare se hai già committato file da escludere
9. Vedere differenze e storia

   * `status`, `diff`, `diff --staged`, `log`, `show`, `blame`
10. GitHub: che cos’è e quando usarlo

    * PR, review, Actions, Pages (panoramica)
11. Sincronizzazione con il remoto

    * `fetch` vs `pull`
    * Messaggio “divergent branches” e scelte: `--rebase`, `--no-rebase`, `--ff-only`
12. Branching e HEAD

    * Perché usare i branch, comandi base, “detached HEAD”
13. Merge e Rebase

    * Differenze pratiche, quando scegliere l’uno o l’altro
14. Merge conflicts

    * Riconoscere i marker, risolvere, `--ours` / `--theirs`, completare l’operazione
15. Tornare indietro in sicurezza

    * `restore`, `revert`, `reset` (soft/mixed/hard), `reset --hard origin/main`, `reflog`
16. Stash: parcheggiare lavori in corso
17. Lavorare bene con GitHub

    * Flusso PR pulito, Fork, GitHub Pages
18. Esercizio guidato passo-passo
19. Errori tipici e soluzioni rapide
20. Cheatsheet dei comandi essenziali
21. Riepilogo “in una riga” dei concetti chiave

---

## 0) Perché esistono Git e GitHub

Immagina di lavorare a un progetto e salvare i file come `progetto_finale_DEF2_vera.zip`. Dopo pochi giorni non ricordi più **cosa** è cambiato, **quando** e **perché**. Se collabori con qualcuno, scambiare file per email diventa un incubo.

**Git** risolve questo problema: tiene una **cronologia** del tuo progetto, come una macchina del tempo. Ogni “scatto” della macchina del tempo si chiama **commit**.
**GitHub** è un sito che ospita una copia online (remota) del tuo progetto, così puoi **pubblicare**, **collaborare** e **fare backup**.

---

## 1) Concetti fondamentali (senza dare nulla per scontato)

* **Repository (repo)**: cartella del progetto che contiene una sottocartella nascosta `.git/`. Dentro `.git/` c’è tutta la **storia**.
* **Working tree**: i file “normali” sul disco, dove modifichi il codice.
* **Staging area (o index)**: una “lista di cose” che finiranno nel **prossimo commit**.
* **Commit**: uno snapshot dei file in staging, con un **messaggio** che spiega cosa hai fatto.
* **HEAD**: un puntatore che indica **dove sei** nella storia (di solito punta al **branch** su cui stai).
* **Branch**: una linea di sviluppo con un nome (es. `main`, `feature/login`). Serve per lavorare su una modifica **senza toccare** il codice stabile.
* **Remote (es. `origin`)**: la copia online del repo, tipicamente su GitHub.

> Immagine mentale: Git è un **grafo** di commit. I branch sono solo **etichette** che puntano a uno dei commit.

---

## 2) Installazione e prima configurazione

Verifica che Git sia installato:

```bash
git --version
```

Configura il tuo nome e la tua email (appaiono nella cronologia):

```bash
git config --global user.name  "Il Tuo Nome"
git config --global user.email "tu@email.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"    # usa VS Code per i messaggi
```

Imposta un comportamento predefinito sensato per `git pull` (spiegazione al §10):

```bash
git config --global pull.rebase true
git config --global rebase.autoStash true
```

Accesso a GitHub **senza password** (consigliato):

```bash
ssh-keygen -t ed25519 -C "tu@email.com"
# copia ~/.ssh/id_ed25519.pub in GitHub → Settings → SSH and GPG keys
```

---

## 3) Creare o clonare un repository

### 3.1. Creare un nuovo repo **locale**

```bash
mkdir mio-progetto && cd mio-progetto
git init
```

### 3.2. Creare un nuovo repo **su GitHub**

* Vai su github.com → pulsante “New” → scegli un nome.
* Lascia vuoto se vuoi inizializzare da locale (oppure aggiungi un README).

Collega il remoto e pubblica:

```bash
git remote add origin git@github.com:utente/mio-progetto.git
git add .
git commit -m "Inizializzazione progetto"
git push -u origin main
```

`-u` stabilisce il collegamento tra il tuo branch locale e quello remoto (tracking). Da ora in poi, basterà `git push`.

### 3.3. Clonare un repo **già online** (caso più comune)

```bash
git clone git@github.com:utente/repo.git
cd repo
```

---

## 4) Il ciclo di lavoro base (sempre uguale)

1. **Guarda cosa è cambiato**

```bash
git status
```

2. **Scegli cosa fotografare** (staging)

```bash
git add file1 file2     # selettivo
git add .               # tutto ciò che è cambiato nella cartella corrente
```

3. **Scatta la foto** (commit)

```bash
git commit -m "feat: aggiunge form di login"
```

4. **Pubblica online** (push)

```bash
git push
```

> Finché non fai `git push`, le tue modifiche **restano solo sul tuo computer**.

---

## 5) Che cosa fa davvero `git add`

`git add` **prende la versione attuale** di un file e la **mette in staging**: quel contenuto finirà nel **prossimo commit**. Non crea un commit, non invia su GitHub.

* File **nuovo** → comincia a essere tracciato e messo in staging.
* File **già tracciato e modificato** → le modifiche vanno in staging.
* File **eliminato** → usa `git add -A` o `git add -u` per mettere in staging anche le cancellazioni.
* File **in `.gitignore`** → viene ignorato (puoi forzare con `git add -f`).

Errore comune: “non in stage” **non** significa “in `.gitignore`”. `.gitignore` è una **lista di esclusione**; lo staging è **cosa includere nel prossimo commit**.

Togli dallo staging:

```bash
git restore --staged path/file
```

---

## 6) `git commit` spiegato bene (cosa significano i flag)

### 6.1. Commit classico

```bash
git commit -m "messaggio"
```

* `-m` = **message**. Passi il messaggio direttamente da riga di comando.

### 6.2. Commit senza `git add` (solo file già tracciati)

```bash
git commit -am "messaggio"
```

* `-a` = **all (tracked)**: mette **automaticamente in staging** tutte le modifiche e le cancellazioni dei file **già tracciati**.
  Non include **nuovi file**: per quelli serve **prima** `git add`.
* `-am` è semplicemente la combinazione di `-a` e `-m`.

### 6.3. Modificare l’ultimo commit

```bash
git commit --amend
```

* Corregge il messaggio o aggiunge/toglie file dallo **stesso** commit precedente.
  Se l’avevi già pubblicato, il push richiederà `--force-with-lease` sul tuo branch.

---

## 7) `.gitignore` (cosa non deve entrare nella storia)

Esempio tipico:

```gitignore
# file di sistema / editor
.DS_Store
.vscode/

# build e dipendenze
dist/
node_modules/

# segreti e configurazioni locali
.env
```

Se hai **già** committato qualcosa da ignorare:

```bash
git rm -r --cached path/da/ignorare
echo "path/da/ignorare" >> .gitignore
git commit -m "chore: aggiorna .gitignore e rimuove file dall'indice"
```

---

## 8) Vedere le differenze e la storia

```bash
git status -sb                    # panoramica compatta
git diff                          # differenze non in staging
git diff --staged                 # differenze in staging
git log --oneline --graph --decorate --all
git show <sha>                    # dettaglio di un commit
git blame path/file               # chi ha cambiato ogni riga
```

---

## 9) Che cos’è GitHub e quando lo usi

* È il “posto nel cloud” dove vive la **copia remota** del tuo repo.
* Serve per **collaborare**: apri **Pull Request** (PR) per proporre modifiche, ricevi **review**, fai girare **test automatici** (GitHub Actions).
* Puoi anche pubblicare siti statici con **GitHub Pages**.

Flusso tipico di collaborazione:

1. Crei un **branch** per una feature.
2. Fai commit e push.
3. Apri una **Pull Request** verso `main`.
4. Qualcuno revisiona → risolvi i commenti → si fa **merge**.

---

## 10) Sincronizzare: `fetch`, `pull` e “divergent branches”

* `git fetch` **scarica** gli aggiornamenti dal remoto ma **non** tocca i tuoi file.
* `git pull` = `fetch` **+** integrazione degli aggiornamenti nel tuo branch (merge o rebase).

Se vedi:

```
hint: You have divergent branches and need to specify how to reconcile them.
```

significa che **tu e il remoto avete entrambi nuovi commit**. Devi dire a Git **come** conciliarli:

* **Rebase** (storia lineare, consigliato per progetti personali):

  ```bash
  git pull --rebase
  ```
* **Merge** (storia ramificata, conservativa):

  ```bash
  git pull --no-rebase
  ```
* **Fast-forward only** (permetti solo avanzamenti lineari):

  ```bash
  git pull --ff-only
  ```

Impostare un default valido **una volta sola**:

```bash
git config --global pull.rebase true       # preferisci rebase lineare
# oppure:
git config --global pull.rebase false      # preferisci merge
# oppure:
git config --global pull.ff only           # solo fast-forward
```

---

## 11) Branching: perché esiste e come si usa

**Senza** branch: lavori sempre su `main`. Se rompi qualcosa, blocchi tutti.
**Con** i branch: per ogni funzionalità apri una “linea di lavoro” dedicata; quando è pronta, la unisci a `main`.

Comandi essenziali:

```bash
git branch                        # elenco branch (asterisco = corrente)
git checkout -b feature/login     # crea e passa al nuovo branch
# equivalente moderno: git switch -c feature/login
git checkout main                 # torna a main  (o: git switch main)
git merge feature/login           # unisci in main
git branch -d feature/login       # elimina il branch (dopo il merge)
git push -u origin feature/login  # pubblica il branch su GitHub
```

**HEAD** indica su quale branch/commit stai lavorando.
Se vedi “detached HEAD”, significa che stai guardando un **commit** senza branch: crea un branch se vuoi continuare da lì:

```bash
git switch -c hotfix/urgente
```

---

## 12) Merge e Rebase: differenze pratiche

**Merge**

* Crea, se necessario, un **commit di merge** che unisce due storie.
* Pro: non riscrive la storia; sicuro per rami condivisi.
* Contro: la cronologia include commit di merge e può sembrare “ramificata”.

**Rebase**

* “Riapplica” i tuoi commit sopra a una base più recente.
* Pro: storia **lineare**, più facile da leggere.
* Contro: **riscrive** i commit del branch; non farlo su commit già condivisi con altri (potresti dover fare `git push --force-with-lease`).

Esempi:

```bash
# Merge tipico
git switch main
git pull
git merge feature/x

# Rebase per pulire una feature prima della PR
git switch feature/x
git fetch origin
git rebase origin/main
# risolvi conflitti → git add <file> → git rebase --continue
```

---

## 13) Merge conflicts: come riconoscerli e risolverli

Quando due persone cambiano **la stessa parte** di un file in modi diversi, Git non sa quale versione tenere. Segnala un conflitto introducendo dei **marker** nel file:

```text
a = 1
<<<<<<< HEAD
b = 2
=======
b = 3
>>>>>>> 56782736387980937883
c = 3
```

Procedura di risoluzione:

1. Apri il file, **scegli** cosa tenere (la tua versione, la loro o un mix) e **rimuovi i marker**.
2. Aggiungi i file risolti:

   ```bash
   git add <file_risolto>
   ```
3. Completa l’operazione:

   * se stai **rebasando**: `git rebase --continue`
   * se stai **mergiando**:  `git commit`

Se ti blocchi: `git rebase --abort` o `git merge --abort`.

Scorciatoie utili su un file in conflitto:

```bash
git checkout --ours   -- path/file   # prendi interamente la tua versione
git checkout --theirs -- path/file   # prendi interamente la versione remota
```

---

## 14) Tornare indietro in sicurezza

* **Scartare modifiche non committate**:

  ```bash
  git restore path/file
  git restore --source=HEAD -- .
  ```
* **Annullare un commit mantenendo la storia** (crea un commit che “inverte”):

  ```bash
  git revert <sha>
  ```
* **Riscrivere la storia locale** (attenzione):

  ```bash
  git reset --soft  <sha>   # tieni staging e working tree
  git reset --mixed <sha>   # default: svuota staging, tieni working tree
  git reset --hard  <sha>   # perdi modifiche locali
  ```
* **Allinearti esattamente al remoto**:

  ```bash
  git reset --hard origin/main      # o origin/master nei repo più vecchi
  ```
* **Paracadute** (quasi sempre puoi recuperare):

  ```bash
  git reflog
  ```

Se hai committato **segreti** (token, password): invalida/ruota le chiavi e riscrivi la storia con `git filter-repo` o **BFG Repo-Cleaner**.

---

## 15) Parcheggiare il lavoro: `git stash`

Se devi cambiare branch ma hai modifiche non pronte:

```bash
git stash            # salva le modifiche (file tracciati)
git stash -u         # include anche file non tracciati
git stash pop        # applica e rimuove dallo stash
git stash apply      # applica ma lascia nello stash
git stash -p         # “a pezzi”
```

---

## 16) Lavorare bene con GitHub

**Pull Request (PR) pulita**

1. `git checkout -b feature/x`
2. commit piccoli, messaggi chiari
3. `git fetch && git rebase origin/main` prima di aprire la PR
4. apri PR su GitHub (descrivi cosa hai fatto, come testare)
5. dopo review, fai **Squash merge** (un solo commit in `main`)

**Fork**: copia di un repo altrui nel tuo account (per proporre modifiche).
**GitHub Pages**: pubblica un sito statico

1. repo con `index.html`
2. `git push`
3. Settings → Pages → scegli branch → ottenieni l’URL.

---

## 17) Esercizio guidato (fallo davvero)

1. Crea una cartella vuota e inizializza Git:

   ```bash
   mkdir prova-git && cd prova-git
   git init
   ```
2. Crea un file e committalo:

   ```bash
   echo "ciao" > index.txt
   git add index.txt
   git commit -m "feat: aggiunge index.txt"
   ```
3. Modifica e usa `-am`:

   ```bash
   echo "riga2" >> index.txt
   git commit -am "feat: aggiunge riga2 a index.txt"
   ```

   Osserva: non hai usato `git add` perché `index.txt` era **già tracciato**.
4. Crea un branch, fai una modifica e mergiala:

   ```bash
   git checkout -b feature/saluto
   echo "hello" >> index.txt
   git commit -am "feat: aggiunge hello"
   git checkout main
   git merge feature/saluto
   ```
5. Pubblica su GitHub (crea un repo vuoto sul sito, poi):

   ```bash
   git remote add origin git@github.com:TUO-UTENTE/prova-git.git
   git push -u origin main
   ```

---

## 18) Errori tipici e soluzioni rapide

* **“non-fast-forward” al push**: il remoto ha commit che non hai.
  Soluzione: `git pull --rebase`, risolvi eventuali conflitti, poi `git push`.
* **“detached HEAD”**: sei su un commit senza branch.
  Soluzione: `git switch -c nome-branch`.
* **`.gitignore` non funziona**: hai già tracciato quei file.
  Soluzione: `git rm -r --cached path/`, poi aggiorna `.gitignore` e committa.

---

## 19) Cheatsheet finale

```bash
# Inizializza / clona
git init
git clone <URL> && cd repo

# Stato e differenze
git status -sb
git diff
git diff --staged

# Aggiungi e committa
git add -p
git commit -m "messaggio"
git commit -am "messaggio"     # -a = all (solo file già tracciati), -m = message

# Pubblica
git push -u origin <branch>

# Sincronizza
git fetch
git pull --rebase               # oppure --no-rebase / --ff-only

# Branching
git checkout -b feature/x       # o: git switch -c feature/x
git checkout main               # o: git switch main
git merge feature/x
git branch -d feature/x

# Conflitti (aiuti veloci)
git checkout --ours   -- path/file
git checkout --theirs -- path/file

# Undo sicuri
git restore path/file
git revert <sha>
git reset --hard origin/main
git reflog

# Ignora file
echo "dist/" >> .gitignore
git rm -r --cached dist/
git commit -m "chore: ignora dist"
```

---

### Cosa ricordare in una riga

* **`git add`** prepara i file per il prossimo commit (staging).
* **`git commit -m`** crea lo snapshot con un messaggio; **`-a`** aggiunge **automaticamente** le modifiche ai file **già tracciati**; **`-am`** = `-a` + `-m`.
* **`git push`** pubblica su GitHub; **`git pull`** ti allinea (meglio con `--rebase`).
* Lavora su **branch**, apri **PR** e risolvi i conflitti con metodo.
