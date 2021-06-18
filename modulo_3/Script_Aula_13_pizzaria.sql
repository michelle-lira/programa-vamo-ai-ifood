/* Uso do COUNT */

select count(*) from tb_cliente;
 
select count (categoria) from tb_pizza;

select count(preco) from tb_pedido; 

select count(categoria) from tb_pizza where categoria like '%Zero Lactose%';

select categoria, count(*) as quantidade_zero_lactose
from tb_pizza 
where categoria = 'Zero Lactose'
group by categoria;

select categoria, count(*) 
from tb_pizza 
group by categoria having count(*) > 7;

/* Uso do SUM e AVG */

select sum (preco) from tb_pedido;

select sum(preco) from tb_pizza;

select avg(preco) from tb_pizza;

select avg(preco) from tb_pedido;


select categoria, min (preco) as categoria
from tb_pizza
group by categoria;

select categoria, avg(preco) as preco_medio
from tb_pizza 
group by categoria
order by avg(preco); 

/* Case when */

SELECT
case 
	when p.nome like '%CATUPIRY' then 'Item n�o vegano'
	else 'talvez vegano'
end
FROM tb_pizza p
ORDER by p.nome;


SELECT p.nome,
case 
	when p.nome like '%CATUPIRY' then 'Item n�o vegano'
	else 'talvez vegano'
end
FROM tb_pizza p
ORDER by p.nome;

select *,
case 
	when  cl.endereco ilike '%Beira mar%' then 'Frete gr�tis'
	else 'Sem promo��o'
end
from tb_cliente cl;

select * from tb_cliente;

select *,
case 
	when  cl.endereco ilike '%Beira mar%' then 'Frete gr�tis'
	else 'Sem promo��o'
end
order by 'Sem promo��o'
from tb_cliente cl;

/* LIMIT, FETCH e OFFSET */

select * 
from tb_pizza 
limit 5;

select * 
from tb_pizza 
order by id_pizza
fetch first 5 row only;

select * 
from tb_pizza 
limit 5
offset (1-1) * 5;

select * from tb_pizza;

select * 
from tb_pizza
fetch first 5 row only
offset (1-1) * 5;

select nome,
case 
	when preco < 50 then '40-45'
	when preco >= 50 and preco < 60 then '50-55'
	else '60-65'
end	as "Faixa de pre�o"
from tb_pizza;

select * from tb_pizza
where categoria = 'TRADICIONAIS';

/* Quest�o: Selecionar a pizza mais cara da categoria �Tradicionais� que possui �a� como segundo caractere. */

/* seleciona as colunas nome e preco, utilizando o operador MAX para pegar o maior valor */
select nome, max(preco)
/* indica de qual tabela essas colunas ser�o selecionadas */
from tb_pizza 
/* coloca uma condi��o para o campo "nome", dizendo que quer que todos os nomes de pizza que contenham a letra "A" na 
 segunda posi��o sejam buscadas */
/* o operador "ilike" normaliza a quest�o do case sensitive, buscando por tudo que contenha o termo, independente de 
 estar escrito com a letra mai�scula ou min�scula */
where nome ilike '%_a%' and categoria = 'Tradicionais'
/* agrupa por nome e pela categoria "Tradicionais" */
group by nome, categoria
/* limita o resultado a uma linha */
limit 1;









