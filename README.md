# Berkley

## Configuration
O programa não conta com uma venv ja criada, você precisa criar isso na mão usando o arquivo `requirements.txt`.
Para isso use os seguintes comandos:
    
    $ python3 -m venv venv
    
    #### PARA MAC OU LINUX ####
    $ source venv/bin/activate 
    
    #### PARA WINDOWS ####
    > \path\to\venv\Scripts\activate
    
    $ pip install -r requirements.txt

## Initialization
Você pode rodar o programa dentro de um docker usando um banco de dados postgres ou usando o sqlite3

#### Docker
+ Instale o Docker **CE** por esse [link](https://www.docker.com/get-docker)
+ Rode os seguintes comandos:

    
        $ docker-compose run web python manage.py makemigrations
        $ docker-compose run web python manage.py migrate
    
#### Sem Docker
+ Faça a seguinte modificação na variável estática DATABASES no arquivo `settings.py` na pasta **berkley**

```python 
DATABASES = {
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
## Running
###Docker
#####Web
Você pode rodar sua aplicação através do terminal usando o seguinte comando

        $ docker-compose run web python manage.py runserver

Sua aplicação poderá ser acessada em um dos seguintes endereços:
+ **localhost:8000**
+ **127.0.0.1:8000**

#####Database
Para acessar o banco de dados via terminal use o seguinte comando:

    $ docker exec -it berkley_db_1 psql -U postgres
    
Para acessar através do Pycharm ou outro conector
(Pode deixar a senha vazia)
  
    URL = jdbc:postgresql://localhost:5432/postgres
    USER = postgres
    
