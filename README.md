# ToDo - Sistema de lista de tarefas

### Comandos para utilizar o projeto
- python -m venv venv
- source .venv/bin/activate (para Linux) ou venv\Scripts\activate.bat (para Windows)
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate

### Renomear o arquivo ".env_example" para ".env"
### Editar o arquivo ".env" com os dados do seu projeto

### Comando para iniciar o servidor de desenvolvimento (http://localhost:8000)
- python manage.py runserver 0.0.0.0:8000

### Comando para iniciar o servidor de produção (http://localhost:8000)
- python manage.py collectstatic
- gunicorn --workers 5 --bind 0.0.0.0:8000 core.wsgi:application
