# ToDo - Sistema de lista de tarefas
Um sistema de lista de tarefas desenvolvido em Python com Django, projetado para demonstrar habilidades em desenvolvimento backend.

## Funcionalidades
- Sistema simples e eficiente para gerenciamento de tarefas.
- Criação, leitura, atualização e exclusão (CRUD) de tarefas.

## Tecnologias Utilizadas
- **Linguagem**: Python 3.x
- **Framework**: Django
- **Banco de Dados**: SQLite (padrão, configurável para outros bancos)

## Requisitos
Certifique-se de ter as seguintes ferramentas instaladas em seu sistema:
- Python 3.8 ou superior
- pip (Python Package Installer)

## Instalação
### 1. Clone o repositório:
- git clone https://github.com/MuzNocci/INTERVIEW_smax_backend.git
- cd INTERVIEW_smax_backend

### 2. Comandos para utilizar o projeto
- python -m venv venv
- source .venv/bin/activate (para Linux) ou venv\Scripts\activate.bat (para Windows)
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate

### 3. Renomear o arquivo ".env_example" para ".env"
### 4. Editar o arquivo ".env" com os dados do seu projeto

## Deploy
### 5. Comando para iniciar o servidor de desenvolvimento (http://localhost:8000)
- python manage.py runserver 0.0.0.0:8000

### 5. Comando para iniciar o servidor de produção (http://localhost:8000)
- python manage.py collectstatic
- gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 5
