USE simple_api;

CREATE TABLE users (
    uid int auto_increment primary key,
    name varchar(50) not null,
    age int not null
);