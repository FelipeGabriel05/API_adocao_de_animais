# API Adoção de Animais
* Api feita em Django rest framework, utilizando os metodos get, post e delete.
* Nessa api é feito o cadastro de um novo pet e também a exclusão de um pet já adicionado.
* A proposta é listar todos os pets disponíveis para adoção.

# URLS
* api/pets => lista todos os pets
* api/pet/id => mostra o pet correspondente ao id da url.

# Biblioteca usada
Instalado usando o pip.
* pip install djangorestframework

# Ambiente virtual
* Ativar no cmd do windows: .\env\Scripts\activate
* Desativa no windows: deactivate

# Executando a api
* Ative o ambiente virtual, nela estão contidos as bibliotecas utilizadas na aplicação
* Em seguida, acesse api_pets. Com o comando: cd api_pets [para windows].
* python manage.py runserver

# Caso haja migrações para serem feitas
* python manage.py makemigrations app
* python manage.py migrate

