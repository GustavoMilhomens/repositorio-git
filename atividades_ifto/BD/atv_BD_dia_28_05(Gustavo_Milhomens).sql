drop database if exists biblioteca;
create database if not exists biblioteca;

use biblioreca;

create table livro(
    titulo varchar(100) not null,
    autor varchar(100) not null,
    ano_publicacao int not null,
    isbn varchar(20) not null,
    id_livro int not null auto_increment,
    constraint pk_livro primary key (id_livro)
);

create table autor(
    id_autor int auto_increment,
    nome varchar(100) not null,
    nacionalidade varchar(50) not null,
    constraint pk_autor primary key (id_autor)
);

alter user 'root'@'localhost' identified with mysql_native_password by '150520';
flush privileges;