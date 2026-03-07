drop database if exists escola;

create database if not exists escola;

use escola;

create table pessoa(
cpf integer(11) not null,
    email varchar(255) not null,
    sexo char(1) not null,
    nome varchar(255) not null,
    nacionali varchar(50) not null,
    data_nascim date not null,
    ft_3x4 blob ,
constraint pk_pessoa primary key (cpf)
);
insert into pessoa set 

create table professor(
id_pessoa integer(11) not null,
    matricula integer not null,
    cart_trabalho integer not null,
    turno time not null,
    hor_entrada date not null,
    hor_saida date not null,
    salario numeric(10,2) not null,
    carga_hor time not null,    
    administra  bool not null,
    constraint pk_matricula_professor primary key (matricula),
    constraint id_fk_pessoa_prof foreign key (id_pessoa) references pessoa(cpf)
);

create table ambiente(
id_ambiente integer(255) not null auto_increment,
    nome_ambiente varchar(50) not null ,
    utilidade varchar(255) not null,
    capacidade_pessoas integer not null,
    tamanho float not null,
    tipo varchar(100),
    constraint pk_id_ambiente primary key (id_ambiente)
);

create table aluno(
id_pessoa integer(11) not null,
prev_conclusao date not null,
    periodo_referencia date not null,
    horario_aproveitado time not null,
    matricula integer not null,
    constraint pk_matricula_aluno primary key (matricula),
    constraint id_fk_pessoa_aluno foreign key (id_pessoa) references pessoa(cpf)
);

create table tercerizado(
id_terceriz integer not null auto_increment,
    cargo varchar(50) not null,
    turno time not null,
    port_arma bool not null,
    id_pessoa integer(11) not null,
    hor_entrada date not null,
    hor_saida date not null,
    salario numeric(10,2) not null,
    carga_hor time not null,
    constraint pk_id_terceriz primary key (id_terceriz),
    constraint id_fk_pessoa_terceriz foreign key (id_pessoa) references pessoa(cpf)
);


describe pessoa;