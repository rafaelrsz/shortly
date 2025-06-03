# TODO'S

* Completar o crud do encurtador em "meus links" na view /links
  * Visualizar e apagar links do usuário logado (acho que não precisa ter edição)

# como rodar

## clonar o repositório

- usar o git clone e clonar o repositório.
- entrar no diretório do projeto

## criar o ambiente virtual e instalar o django

### criar ambiente virtual

- rodar o comando `pip install virtualenv`
- criar o virtualvenv com o comando `virtualenv venv`
- ativar o ambiente virtual com o comando `source venv/Scripts/activate
` (no bash) e `source ./venv/Scripts/activate
` (no PowerShell)
- para desativar é só usar o comando `deactivate`

### instalar o django

- rodar o comando `pip install django`

## fazer as migrações e rodar o projeto

### fazer migrações

- executar os dois comandos para executar as migrações
  - `python manage.py makemigrations`
  - `python manage.py migrate`

### rodar o projeto

- rodar o projeto com o comando `python manage.py runserver`
  