# lacrei_api

API RESTful para gerenciamento de consultas médicas.  
Desenvolvido com Django, Django REST Framework, PostgreSQL, Docker e GitHub Actions.

## Como rodar o projeto

```bash
git clone https://github.com/SEU_USUARIO/lacrei_api.git
cd lacrei_api
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver