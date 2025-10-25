# Git e GitHub — lezione completa e pratica

Obiettivo: capire come funziona Git (version control), come usarlo **correttamente** ogni giorno, quando scegliere **merge** o **rebase**, come risolvere i **merge conflict**, e come pubblicare e collaborare con **GitHub**.  
Stile: spiegazione + esempi pronti da copiare.

---

## 1. Che cosa sono Git e GitHub

**Git** è un sistema di controllo di versione. Registra *istantanee* (commit) del tuo progetto nel tempo e ti permette di:
- tenere traccia di ogni modifica;
- lavorare su **branch** separati (feature, bugfix) senza toccare il codice stabile;
- fondere il lavoro (merge/rebase) e **tornare indietro** quando serve.

**GitHub** è un servizio web che ospita repository Git remoti. Serve per:
- sincronizzare il tuo lavoro fra più macchine/persone (push/pull);
- fare **Pull Request** (code review, CI);
- pubblicare siti statici con **GitHub Pages**.

---

## 2. Installazione e configurazione iniziale (una volta sola)

```bash
git config --global user.name  "Il Tuo Nome"
git config --global user.email "tu@email.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"      # usa VS Code per i messaggi
git config --global pull.rebase true               # preferisci storia lineare
git config --global rebase.autoStash true          # stasha auto le modifiche durante pull/rebase
```

Autenticazione **SSH** (evita password):
```bash
ssh-keygen -t ed25519 -C "tu@email.com"
# copia ~/.ssh/id_ed25519.pub su GitHub → Settings → SSH and GPG keys
```

Alias utili:
```bash
git config --global alias.st "status -sb"
git config --global alias.lg "log --oneline --graph --decorate --all"
```

---

## 3. Repository: locale e remoto

- Un **repository** è una cartella con una sottocartella nascosta `.git/` (contiene la storia).
- **Locale** = sul tuo computer; **remoto** = su GitHub (tipicamente chiamato `origin`).

Creare un nuovo repo **locale**:
```bash
mkdir progetto && cd progetto
git init
```

Clonare un repo **remoto** nella cartella in cui vuoi lavorare/pubblicare:
```bash
git clone <URL>   # es. git@github.com:utente/repo.git
cd repo
```

---

## 4. Il modello mentale di Git (tre aree)

- **Working tree**: i file sul disco.
- **Staging area (index)**: cosa finirà nel **prossimo commit**.
- **Repository**: la storia salvata (i commit).

**HEAD** è un puntatore al commit corrente (di solito al branch su cui stai).

---

## 5. Flusso quotidiano di lavoro

```bash
git status                         # vedi cosa è cambiato
git add <file> ...                 # metti in staging (prepara al commit)
git commit -m "messaggio chiaro"   # crea lo snapshot
git push                           # pubblica su GitHub
```

Messaggi: segui “Conventional Commits” (utile e leggibile)
```
feat: aggiunge la pagina profilo
fix: corregge validazione email
docs: aggiorna README
refactor: rinomina componenti
```

---

## 6. `git add`: che cosa fa esattamente

`git add file.example` prende **la versione attuale** di quel file e la **mette in staging**.  
Non crea un commit e non manda nulla su GitHub.

Casi tipici:
- file **nuovo** → inizia a essere tracciato e staged;
- file **modificato** → le modifiche entrano in stage;
- file **in `.gitignore`** → viene ignorato (forza con `git add -f`).

Rimuovere dallo stage:
```bash
git restore --staged file.example
```

Convenienze:
```bash
git add -p           # “a pezzi”, selezioni hunk per hunk
git add -u           # traccia modifiche e cancellazioni dei file già tracciati
git add -A           # aggiunge TUTTO (nuovi, modifiche, cancellazioni) in tutto il repo
```

---

## 7. `git commit`: tutte le opzioni fondamentali spiegate

Comando base:
```bash
git commit -m "messaggio"
```
- `-m` sta per **message**: specifica il messaggio del commit da riga di comando.

Commit veloce senza `git add` (solo file **già tracciati**):
```bash
git commit -am "messaggio"
```
- `-a` sta per **all (tracked)**: aggiunge automaticamente allo stage **tutte le modifiche e cancellazioni dei file già tracciati**.  
  **Non** include i file **nuovi**: per quelli serve prima `git add`.

Altre opzioni utili:
```bash
git commit --amend            # modifica l'ultimo commit (contenuto e/o messaggio)
git commit --no-verify        # salta gli hook pre-commit (se configurati)
```

---

## 8. Pubblicare davvero online

Finché non fai `git push`, i commit restano **solo in locale**.
```bash
git push
# primo push di un branch nuovo:
git push -u origin <nome-branch>
```

---

## 9. Allinearsi con il remoto: `fetch` e `pull`

- `git fetch` **scarica** aggiornamenti dal remoto ma **non** li fonde nel tuo branch.
- `git pull` = `fetch` **+** integrazione (merge o rebase).

Se vedi:
```
hint: You have divergent branches and need to specify how to reconcile them.
```
significa che il tuo branch e `origin/<branch>` hanno **storie divergenti**. Devi scegliere **come** conciliarle:

Uso puntuale:
```bash
git pull --rebase    # integra con rebase (storia lineare)
git pull --no-rebase # integra con merge (storia ramificata)
git pull --ff-only   # solo fast-forward (fallisce se c'è divergenza)
```

Imposta il default per tutti i repo (una volta):
```bash
git config --global pull.rebase true      # preferisci rebase lineare
# oppure
git config --global pull.rebase false     # preferisci merge
# oppure
git config --global pull.ff only          # permetti solo avanzamenti lineari
```

---

## 10. Merge, Rebase e Fast-Forward (perché e quando)

**Merge**  
Unisce i due rami creando, se necessario, un **commit di merge**.
```bash
git switch main
git pull
git merge feature/login
```
Pro: non riscrive la storia; sicuro in team.  
Contro: la storia può risultare ramificata.

**Rebase**  
“Riapplica” i commit del tuo branch **sopra** la punta aggiornata di un altro branch.
```bash
git switch feature/login
git fetch origin
git rebase origin/main
# risolvi conflitti → git add ... → git rebase --continue
```
Pro: storia lineare, leggibile.  
Contro: **riscrive** i commit del branch; **non** usare per riscrivere storia **già condivisa**.

**Fast-Forward**  
Avanzamento lineare senza commit di merge quando possibile.
```bash
git pull --ff-only
```

Regola pratica: rebase per pulire i **tuoi** branch prima della PR, merge per integrare in `main`.

---

## 11. Vedere cosa è cambiato (ispezione)

```bash
git status -sb                 # panoramica compatta
git diff                       # differenze non staged
git diff --staged              # differenze staged
git log --oneline --graph --decorate --all
git show <sha>                 # dettagli di un commit
git blame path/file            # chi ha cambiato cosa e quando
```

---

## 12. `.gitignore` e come rimediare agli errori

Esempio:
```gitignore
# sistema / editor
.DS_Store
.vscode/

# build / dipendenze
dist/
node_modules/

# segreti
.env
```

Hai già committato qualcosa che dovevi ignorare?
```bash
git rm -r --cached path/da/ignorare
echo "path/da/ignorare" >> .gitignore
git commit -m "chore: aggiorna .gitignore e rimuove file dall'indice"
```

---

## 13. Tornare indietro in sicurezza

Scartare modifiche **non** committate:
```bash
git restore path/file
git restore --source=HEAD -- .
```

Annullare un commit **senza** riscrivere la storia:
```bash
git revert <sha>       # crea un commit “inverso”
```

Riscrivere la storia locale (attenzione):
```bash
git reset --soft  <sha>   # tieni staging e working tree
git reset --mixed <sha>   # default: tieni working, svuoti staging
git reset --hard  <sha>   # perdi modifiche locali
```

Allinearsi esattamente al remoto:
```bash
git reset --hard origin/main      # (o origin/master nei repo più vecchi)
```

Recupero d’emergenza:
```bash
git reflog                        # cronologia dei movimenti di HEAD (anche “persi”)
```

Se hai committato **segreti** (token, password): ruotali/invalidali subito e riscrivi la storia con `git filter-repo` o **BFG Repo-Cleaner**.

---

## 14. Branching e HEAD (concetto, utilità, potenziale)

Perché i **branch**: sviluppi una feature o un fix **in parallelo** al codice stabile. Quando è pronto, lo unisci.

Comandi base:
```bash
git branch                      # elenca i branch (asterisco = corrente)
git checkout -b feature/x       # crea e passa al nuovo branch
# oppure: git switch -c feature/x
git checkout main               # torna a main
git merge feature/x             # integra la feature in main
git branch -d feature/x         # elimina il branch (se già mergiato)
git push -u origin feature/x    # pubblica il branch su GitHub
```

**HEAD** indica “dove sei”:
- normalmente punta a `refs/heads/<branch>`;
- “detached HEAD” = sei su un commit specifico (es. dopo `git checkout <sha>`).  
  Crea un branch se vuoi continuare lì:
  ```bash
  git switch -c hotfix/urgente
  ```

---

## 15. Merge conflicts: riconoscerli e risolverli

Esempio di file in conflitto:
```txt
a = 1
<<<<<<< HEAD
b = 2
=======
b = 3
>>>>>>> 56782736387980937883
c = 3
```

Procedura:
```bash
# 1) apri i file, scegli le versioni corrette, rimuovi i marker
git add <file_risolto>

# 2) completa l’operazione:
git rebase --continue    # se stavi rebasando
# oppure
git commit               # se stavi mergiando

# 3) se vuoi annullare:
# git rebase --abort
# git merge  --abort
```

Scorciatoie:
```bash
git checkout --ours   -- path/file   # prendi la tua versione
git checkout --theirs -- path/file   # prendi la versione del remoto
```

---

## 16. Stash: parcheggiare lavori in corso

```bash
git stash            # salva le modifiche (tracciate)
git stash -u         # include anche i file non tracciati
git stash pop        # applica e rimuove dallo stash
git stash apply      # applica ma lascia nello stash
git stash -p         # a pezzi
git stash branch esperimento   # crea un branch da quello stash
```

---

## 17. Funzioni utili di GitHub

**Pull Request (PR) standard pulito**
1. `git checkout -b feature/x`
2. commit piccoli, messaggi chiari
3. `git fetch && git rebase origin/main`
4. apri PR su GitHub (descrizione, checklist, test)
5. merge con **Squash** su `main` per una storia pulita

**Fork**: copia un repo altrui nel tuo account per proporre modifiche.  
**GitHub Pages**: pubblica un sito statico
1. repo con `index.html`
2. `git push`
3. Settings → Pages → scegli branch → ottieni URL.

---

## 18. Buone pratiche riassunte

- Lavora su **feature branch**, non direttamente su `main`.
- Fai **commit atomici**: un’idea, un commit.
- Sincronizza spesso: `git fetch` + `git pull --rebase`.
- Proteggi `main` su GitHub (branch protection, CI obbligatoria).
- Evita `--force`; se serve, usa `--force-with-lease` e **solo** sui tuoi branch.

---

## 19. Cheatsheet essenziale

```bash
# Inizializza / clona
git init
git clone <URL> && cd repo

# Stato / diff / log
git status -sb
git diff
git diff --staged
git lg

# Aggiungi e committa
git add -p
git commit -m "feat: ..."
git commit -am "fix: ..."      # -a = all tracked, -m = message
git commit --amend

# Pubblica
git push -u origin <branch>

# Sincronizza
git fetch
git pull --rebase              # (--no-rebase | --ff-only)

# Branching
git checkout -b feature/x
git checkout main
git merge feature/x
git branch -d feature/x

# Conflitti (helper)
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

## 20. Glossario dei flag citati

- `-m` = **message** (per `git commit`).
- `-a` = **all (tracked)**: includi automaticamente modifiche e cancellazioni dei file **già tracciati** (non i nuovi).
- `-p` = **patch**: modalitá interattiva “a pezzi”.
- `--amend` = riscrivi l’ultimo commit (messaggio e/o contenuto).
- `--rebase / --no-rebase / --ff-only` (per `git pull`) = strategia di integrazione.
- `--hard` (per `git reset`) = ripristina working tree e index al commit indicato **perdendo** modifiche locali.
- `origin/main` vs `origin/master` = nome del branch remoto predefinito (i repo moderni usano `main`).

---

### Conclusione
Con queste basi **spiegate** (non solo “appunti”) puoi:
- lavorare in locale con uno schema chiaro,
- capire cosa fanno davvero `git add`, `git commit -m`, `git commit -am`,
- scegliere consapevolmente **merge** o **rebase**,
- risolvere conflitti con metodo,
- pubblicare e collaborare su GitHub come un professionista.
