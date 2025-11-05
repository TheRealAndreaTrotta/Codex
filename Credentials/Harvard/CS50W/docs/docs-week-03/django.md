# 1) Nella cartella dove vuoi creare il progetto
python3 -m venv .venv
source .venv/bin/activate

# 2) Installa Django nell'ambiente --> prima volta in cui si installa django
python3 -m pip install Django   

# 3) Verifica che Django sia visibile --> prima volta in cui si installa django
python3 -m django --version

# 4) Crea il progetto (usa il modulo, così non ti serve 'django-admin' nel PATH)
python3 -m django startproject lecture3

# 5) Avvia il server di sviluppo
cd lecture3
python3 manage.py runserver
