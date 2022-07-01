-- CREAMOS LA BBDD
create database if not exists simpsons_quotes;

use simpsons_quotes;

-- CREAMOS LA TABLA PRINCIPAL INVOICES
create table quotes (
  id INT NOT NULL PRIMARY KEY,
  quote VARCHAR(255) NOT NULL
);

-- INSERTAMOS VALORES DE PRUEBA
insert into quotes (id, quote)
values (1,'Yo no fui!');

insert into quotes (id, quote)
values (2,'Doh!');

insert into quotes (id, quote)
values (3,'A la grande le puse cuca');

insert into quotes (id, quote)
values (4,'Plan dental! Lisa necesita frenos!');

insert into quotes (id, quote)
values (5,'La comida va aqui! Claro que si!');

insert into quotes (id, quote)
values (6,'Si es claro y amarillo seguro que es juguillo, si es turbio y picoson es sidra muchachon');

insert into quotes (id, quote)
values (7,'Ay! ese perro tiene la cola peluda');