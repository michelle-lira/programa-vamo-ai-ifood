-- ALTERANDO DADOS
-- alter database biblioteca rename to mercearia;
--alter table produtos rename qtd to qtd_estoque;

-- QUERIES
select * from clientes;
select * from produtos; 
select * from pedidos;

select * from produtos p where preco > 10.00;
select nome_cliente from clientes;
select nome_cliente, sobrenome_cliente from clientes;
select sobrenome_cliente, nome_cliente from clientes;
select nome_produto from produtos p;
select nome_produto, descricao, preco 
from produtos p;
select nome_produto, preco from produtos p;
select cod_cliente, cod_pedido from pedidos p;

-- WHERE
select *
from clientes c 
where cod_cliente = 4;

select *
from clientes c 
where cod_cliente = 3;

select nome_produto, qtd_estoque
from produtos p 
where qtd_estoque < 10;

select cod_produto, qtde
from pedidos p 
where cod_cliente = 1;

-- ORDER BY
select * from produtos p 
order by nome_produto;

select * from produtos p 
order by qtd_estoque desc;

select nome_produto, preco 
from produtos p
order by nome_produto, preco;

select nome_produto, descricao 
from produtos p
order by descricao nulls first;

select * from produtos p 
where preco > 10.00
order by preco desc;

select nome_produto, qtd_estoque
from produtos p 
where qtd_estoque >= 15
order by qtd_estoque asc;

-- LIMIT E OFFSET
select * from produtos p 
order by preco 
limit 10;

select * from produtos p 
order by preco 
limit 3
offset 2;

select * from produtos p 
order by preco desc
offset 2;

select * from produtos p 
order by preco desc
limit 5;

select * from produtos p 
order by preco desc
limit all; -- em geral, não é necessário, mas existe

-- OPERADORES DE COMPARAÇÃO
select nome_produto, preco
from produtos p 
where preco  > 12.00;

select nome_produto, qtd_estoque 
from produtos p 
where qtd_estoque <=20;

select nome_produto, qtd_estoque 
from produtos p 
where qtd_estoque <=20 and qtd_estoque > 10;

select nome_produto, qtd_estoque 
from produtos p 
where nome_produto != 'Refrigerante';

-- BETWEEN
--select 
--from 
--where 
--between ou not between
--and

select nome_produto, preco 
from produtos
where preco between 10 and 20; -- ou 'not between'

select nome_produto, preco 
from produtos
where 
	preco between 3.50 and 5.00 or
	preco between 10.00 and 20.00
order by preco asc;

select nome_produto, preco, qtd_estoque 
from produtos
where 
	preco between 2.00 and 6.00 and
	qtd_estoque < 10
order by preco desc;

select nome_produto, preco 
from produtos
where 
	preco not between 5.00 and 12.00;

-- JOIN
select nome_cliente, cod_pedido
from pedidos p
right join clientes c on c.cod_cliente = p.cod_cliente;

select nome_cliente, cod_pedido
from pedidos p
left join clientes c on c.cod_cliente = p.cod_cliente;

-- UPDATE
--update produtos 
--set descricao = 'Pote de margarina vegetal'
--where cod_produto = 11;

--update produtos 
--set preco = 3.95
--where nome_produto = 'Sabonete';

--update produtos 
--set preco = 3.95
--where nome_produto = 'Sabonete';

--update produtos 
--set qtd_estoque = qtd_estoque - 3.95
--where preco > 15.00;

--update produtos 
--set preco = preco * 1.10;  --não usei where pra que a alteração fosse total

-- DELETE FROM 
-- delete from nome_tabela
-- where condições

--delete from produtos 
--where cod_produto = 12;

--delete from produtos 
--where qtd_estoque <= 5;

-- TRUNCATE TABLE
-- limpa os registros de uma tabela, mas não apaga a tabela





































































