# Comando para iniciar o servidor (http://localhost:8000)
gunicorn --bind 0.0.0.0:8000 core.wsgi:application