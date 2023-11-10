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
| id_carrito   | int       | foreign key            |

## Tabla - Categories

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

## Tabla - Lista_productos_a_comprar

| variable          | Type  | key                    |
| ----------------- | ----- | ---------------------- |
| id                | int   | primary key - not null |
| id_producto       | int   | foreign key            |
| cantidad_producto | int   |                        |
| total             | float |                        |
| datetime          | time  |                        |

## Tabla - Carrito_compra

| variable          | Type      | key                    |
| ----------------- | --------- | ---------------------- |
| id                | int       | primary key - not null |
| id_lista_producto | float     | foreign key            |
| payment_method    | char (25) | not null               |
| direction         | text      | not null               |

## Tabla - users

| variable     | Type      | key                    |
| ------------ | --------- | ---------------------- |
| id           | int       | primary key - not null |
| name         | char(50)  | not null               |
| surname      | char(50)  | not null               |
| phone_number | char (18) | not null               |
| email        | email     | not null               |
| password     | char (12) | not null               |
| status       | boolean   | not null               |

5º Crear las migraciones

```sh
python manage.py makemigrations
python manage.py makemigrations <nombre_app>
```

6º Sincronizar migraciones

```sh
python manage.py migrate
```
