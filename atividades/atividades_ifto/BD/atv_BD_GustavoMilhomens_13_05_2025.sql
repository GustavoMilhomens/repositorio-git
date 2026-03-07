-- atv_BD_GustavoMilhomens
drop database if exists escola;

create database if not exists escola;

use escola;

create table aluno(
	id_aluno integer(255) not null auto_increment, -- pk
	nome varchar(100) not null,
	cpf integer(11) not null,
	data_nascimento date not null,
	email varchar(255) not null,
	telefone varchar(16) not null,
    constraint pk_id_aluno primary key (id_aluno)
);
 
create table diciplina(
	id_diciplina integer(255) not null auto_increment, -- pk
	nome varchar(100) not null,
	carga_horaria time not null,
	ementa varchar(255) not null,
	semestre date not null,
    constraint pk_id_diciplina primary key (id_diciplina)
);

create table matricula(
	id_matricula integer(255) not null , -- pk
	id_aluno integer(255) not null, -- fk
	data_matricula date not null,
	status varchar(255) not null,
    constraint pk_id_matricula primary key (id_matricula),
    constraint fk_id_aluno foreign key (id_aluno) references aluno(id_aluno)
);

create table professor(
	id_professor integer(255) not null auto_increment, -- pk
	titulacao varchar(255) not null,
	cargo varchar(100) not null,
	email varchar(255) not null,
	telefone varchar(16) not null,
    constraint pk_id_professor primary key (id_professor)
);

create table biblioteca(
	nome varchar(100) not null ,-- pk 
	localizacao varchar(255) not null,
	telefone varchar(16) not null,
	horario date not null,
	funcionamento varchar(255),
    constraint pk_nome_biblioteca primary key (nome) 
);

create table turma(
	id_turma integer(255) not null ,-- pk
	semestre date not null , 
	ano date not null ,
	id_disciplina integer(255) not null,  -- fk
    constraint pk_id_turma primary key (id_turma),
    constraint fk_id_diciplina foreign key (id_disciplina) references diciplina(id_diciplina)
); 

create table departamento(
	id_departamento integer(255) not null auto_increment, -- pk
	nome varchar(100) not null,
	sigla varchar(10),
	email varchar(255) not null,
	ramal int not null,
    constraint pk_id_departamento primary key (id_departamento) 
    
);

create table emprestimo(
	id_emprestimo integer(255) not null auto_increment ,-- pk
	data_emprestimo date not null,
	data_devolucao date not null,
    constraint pk_id_empresimo primary key (id_emprestimo)
);

create table funcionario(
	id_funcionario integer(255) not null auto_increment,
	constraint pk_id_funcionario primary key (id_funcionario)
);



describe aluno;
describe diciplina;
describe matricula;
describe professor;
describe biblioteca;
describe turma;
describe departamento;
describe emprestimo;
describe funcionario;





