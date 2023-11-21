# REQUISITOS DEL PROYECTO:

    [X] Conexion a una BD (PostgreSQL o MongoDB)
    [X] Minimo un CRUD (menos usuarios y roles)
    [] Controlador con lógica
    [X] Rutas protegidas
    [X] Modelos relacionados
    [] Despliegue en Render funcional
    [X] BackEnd con Flask, Django o NodeJS
    [X] Documentación con Swagger o Postman
    [X] Repositorio en Github con archivo README.md

# BASE DE DATOS RELACIONAL

## Tabla - Clientes

| variable     | Type      | key                    |
| ------------ | --------- | ---------------------- |
| id           | int       | primary key - not null |
| name         | char(50)  | not null               |
| surname      | char(50)  | not null               |
| phone_number | char (18) | not null               |
| email        | email     | not null               |
| password     | char (12) | not null               |
| direction    | text      |                        |
| status       | boolean   | not null               |

## Tabla - Categories

| variable | Type     | key                    |
| -------- | -------- | ---------------------- |
| id       | int      | primary key - not null |
| name     | char(25) | not null - unique      |
| status   | boolean  | not null               |

## Tabla - Métodos de pago

| variable | Type     | key                    |
| -------- | -------- | ---------------------- |
| id       | int      | primary key - not null |
| name     | char(25) | not null - unique      |
| status   | boolean  | not null               |

## Tabla - Productos

| variable        | Type      | key                    |
| --------------- | --------- | ---------------------- |
| id              | int       | primary key - not null |
| name            | char(50)  | not null               |
| category        | char(25)  | Foreign key            |
| barcode         | char(20)  | not null               |
| customs_code    | char (30) | not null               |
| price           | float     | not null               |
| stock           | float ()  | not null               |
| description     | text      | not null               |
| Image           | text      | not null               |
| number_of_order | int       | not null               |
| status          | boolean   | not null               |

## Tabla - Item_Carrito

| variable          | Type | key                    |
| ----------------- | ---- | ---------------------- |
| id                | int  | primary key - not null |
| id_producto       | int  | foreign key            |
| cantidad_producto | int  |                        |

## Tabla - Carrito_compra

| variable        | Type      | key                    |
| --------------- | --------- | ---------------------- |
| id              | int       | primary key - not null |
| id_shoppingcart | float     | foreign key            |
| payment_method  | char (25) | foreign key            |
| direction       | text      | not null               |
| total           | decimal   | defailt = 0.00         |

## Tabla - users

| variable | Type      | key                    |
| -------- | --------- | ---------------------- |
| id       | int       | primary key - not null |
| name     | char(50)  | not null               |
| surname  | char(50)  | not null               |
| username | char(50)  | not null               |
| email    | email     | not null               |
| password | char (12) | not null               |
| status   | boolean   | not null               |

# FORMA DE EJECUTAR en caso de moficicaciones

## - Iniciar el entorno virtuañ

    python -m venv venv

## - Instalar los requerimientos

    pip install -r requirements.txt

## - Generar las variables entorno:

    DEBUG = True
    DB_NAME =
    DB_USER =
    DB_PASSWORD =
    DB_HOST =
    DB_PORT =

## -El archivo principal es el TiendaProyectoFinal

# URL EN LOCAL:

    http://127.0.0.1:8000/swagger-ui/
