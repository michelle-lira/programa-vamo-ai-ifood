-- VER TODOS OS BANCOS EXISTENTES 
-- NO DBEAVER
--select datname from pg_catalog.pg_database;

-- NO PGADMIN4:
--select datname from pg_database;

-- CRIANDO BANCO DE DADOS
CREATE DATABASE mercearia
WITH
OWNER = proprietário
ENCODING = "UTF-8"
LC_COLLATE = 'pt_BR.UTF-8'
LC_CTYPE = 'pt_BR.UTF-8'
TABLESPACE = pg_default
CONNECTION LIMIT = -1;

-- CRIANDO TABELAS
create table clientes (
	cod_cliente int primary key,
	nome_cliente varchar(30) not null,
	sobrenome_cliente varchar(50) not null
);

create table produtos (
	cod_produto int primary key,
	nome_produto varchar(40) not null,
	descricao text null,
	preco numeric check(preco > 0) not null,
	qtd_estoque smallint default 0
);
-- default 0: quando eu cadastrar um produto, se ñ fornecer preço, vai ser 0

create table pedidos (
	cod_pedido serial primary key,
	cod_cliente int not null references clientes(cod_cliente),
	cod_produto int not null references produtos(cod_produto),
	qtde smallint not null
	-- foreign key (cod_produto) references produtos(cod_produto)
);

--INSERINDO DADOS
insert into clientes (cod_cliente, nome_cliente, sobrenome_cliente)
values (1, 'Fabio', 'Oliveira');
insert into clientes (cod_cliente, nome_cliente, sobrenome_cliente)
values (2, 'Mônica', 'da Silva');
insert into clientes (cod_cliente, nome_cliente, sobrenome_cliente)
values (3, 'Ana', 'Oliveira');

insert into produtos (cod_produto, nome_produto, descricao, preco, qtd_estoque)
values 
(1, 'Álcool Gel', 'Garrafa de álcool em gel de 1L na concentração 70%', 12.90, 20),
(2, 'Luvas de Látex', 'Caixa de luvas de látex com 100 unidades', 32.50, 25),
(3, 'Pasta de Dentes', 'Tubo de pasta de dentes de 90g', 3.60, 12),
(4, 'Sabonete', 'Sabonete antibacteriano', 3.50, 5),
(5, 'Enxaguante Bucal', 'Antisséptico bucal de 500ml', 17.00, 28);

insert into produtos (cod_produto, nome_produto, descricao, preco, qtd_estoque)
values 
(6, 'Detergente', 'Detergente líquido 500ml', 1.89, 32),
(7, 'Leite Integral', 'Leite Integral de 1L', 4.60, 70),
(8, 'Refrigerante', 'Garrafa de Refrigerante de 600ml', 3.70, 14),
(9, 'Refrigerante', 'Garrafa de Refrigerante de 1L', 6.89, 16),
(10, 'Refrigerante', 'Lata de refrigerante de 350ml', 2.99, 45),
(11, 'Desinfetante Multiuso', 'Desinfetante lavanda com 500ml', 7.00, 32);

insert into produtos (cod_produto, nome_produto, preco, qtd_estoque)
values 
(12, 'Margarina', 3.20, 8);

insert into produtos (cod_produto, nome_produto, descricao, preco, qtd_estoque)
values 
(13, 'Sabão em Pó', 'Caixa de sabão em pó de 1/2 kg', 12.50, 5),
(14, 'Biscoito', 'Pacote de biscoito integral 110g', 3.45, 16),
(15, 'Manteiga', 'Pote de manteiga 250g', 8.70, 5);

insert into pedidos (cod_cliente, cod_produto, qtde)
values 
(1, 2, 3),
(2, 3, 2),
(1, 3, 4);

insert into pedidos (cod_cliente, cod_produto, qtde)
values 
(2, 6, 3),
(2, 5, 2),
(3, 8, 5);
-- a coluna cod_pedido é serial então não preciso inserir dados nela
-- o próprio banco autoincrementa


































































