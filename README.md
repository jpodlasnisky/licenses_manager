# # licenses_manager
Reestruturação do desafio castlabs/django-coding-challenge

Para rodar o ambiente, necessário rodar docker-compose up.

## Variáveis de ambiente
Há a necessidade de criar um arquivo .env com as variáveis de ambiente conforme segue:
SECRET_KEY = 'chave_segredo_django'
POSTGRES_NAME = 'nome do banco'
POSTGRES_USER = 'usuário do banco'
POSTGRES_USER = 'senha do usuário'
POSTGRES_HOST = 'host do banco'
POSTGRES_PORT = <porta>
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp server do email'
EMAIL_HOST_USER = 'usuário do email'
EMAIL_HOST_PASSWORD = 'senha do usuário do e-mail'
EMAIL_PORT = <porta>
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@myapp.com'Welcome to StackEdit!
