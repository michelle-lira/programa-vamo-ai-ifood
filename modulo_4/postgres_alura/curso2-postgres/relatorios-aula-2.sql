-- QUERIES

-- RELATÓRIO COM TODOS OS DADOS DOS ALUNOS E OS IDs DOS RESPECTIVOS CURSOS
-- EM QUE ESTÃO MATRICULADOS
SELECT * 
  FROM aluno
  JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id;

-- 3 ALUNOS MATRICULADOS NA MAIOR QUANTIDADE DE CURSOS
  SELECT a.primeiro_nome, 
	     a.ultimo_nome,
         COUNT(ac.curso_id) AS numero_cursos
    FROM aluno AS a 
    JOIN aluno_curso ac ON ac.aluno_id = a.id
GROUP BY a.primeiro_nome, a.ultimo_nome
ORDER BY numero_cursos desc
   LIMIT 3;

-- RELATÓRIO COM O ALUNO QUE ESTÁ MATRICULADO NO MAIOR NÚMERO DE CURSOS
  SELECT aluno.primeiro_nome,
         aluno.ultimo_nome,
		 COUNT(aluno_curso.curso_id) AS numero_cursos
    FROM aluno
	JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
GROUP BY 1, 2
ORDER BY numero_cursos DESC
   LIMIT 1;
 
SELECT *
  FROM aluno;
  
SELECT * 
  FROM aluno_curso;
 
 -- RELAÇÃO TOTAL DOS ALUNOS E AS RESPECTIVAS QUANTIDADES DOS CURSOS
 -- NOS QUAIS ESTÃO MATRICULADOS
  SELECT aluno.primeiro_nome,
         aluno.ultimo_nome,
		 COUNT(aluno_curso.curso_id) AS numero_cursos
    FROM aluno
	JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
GROUP BY 1, 2
ORDER BY numero_cursos DESC;
   
-- RELATÓRIO COM O CURSO QUE TEM MAIS ALUNOS MATRICULADOS
  SELECT curso.nome,
  		 COUNT(aluno_curso.aluno_id) numero_alunos
    FROM curso
	JOIN aluno_curso ON aluno_curso.curso_id = curso.id
GROUP BY 1
ORDER BY numero_alunos DESC
   LIMIT 1;
  
-- RELATÓRIO COM OS CURSOS E QTD DE ALUNOS MATRICULADOS  
  SELECT curso.nome,
  		 COUNT(aluno_curso.aluno_id) numero_alunos
    FROM curso
	JOIN aluno_curso ON aluno_curso.curso_id = curso.id
GROUP BY 1
ORDER BY numero_alunos DESC;

-- SELECIONAR TODOS OS CURSOS MESMO QUE NÃO TENHA ALUNO MATRICULADO
-- E ORDENE POR ID
   SELECT * 
     FROM curso c 
LEFT JOIN aluno_curso ac ON ac.curso_id = c.id
 ORDER BY c.id;

-- SELECIONAR TODOS OS ALUNOS MESMO QUE NÃO ESTEJAM MATRICULADOS EM
-- NENHUM CURSO E ORDENE POR ID
   SELECT * 
     FROM aluno a 
LEFT JOIN aluno_curso ac ON ac.aluno_id = a.id
 ORDER BY a.id; 

SELECT * 
  FROM categoria;
 
SELECT *
  FROM curso;
 
-- RELATÓRIO COM AS CATEGORIAS, INCLUSIVE AS CATEGORIAS SEM CURSOS EXISTENTES
   SELECT c.nome, 
          COUNT(c2.id) AS numero_cursos
     FROM categoria c 
LEFT JOIN curso c2 ON c2.categoria_id = c.id
GROUP BY c.nome
ORDER BY c.nome, numero_cursos desc;

-- RELATÓRIO COM AS CATEGORIAS E QTD DE CURSOS EXISTENTES EM CADA UMA
  SELECT c.nome, 
         count(c2.id) AS numero_cursos
    FROM categoria c 
    JOIN curso c2 ON c2.categoria_id = c.id
GROUP BY c.nome
ORDER BY c.nome, numero_cursos desc;


-- FILTRANDO A PARTIR DE LISTAS: EQUIVALE A CONSULTAR USANDO OR

-- SELECIONAR OS CURSOS QUE PERTENCEM ÀS CATEGORIAS 2 OU 3
SELECT * 
  FROM curso 
 WHERE categoria_id IN (2, 3);

-- SELECIONAR OS ALUNOS CUJOS PRIMEIROS NOMES SÃO:
-- "VINICIUS", "DIOGO" E "LUAN"
SELECT * 
  FROM aluno 
 WHERE primeiro_nome IN ('Vinicius', 'Diogo', 'Luan');

-- FILTRAR TODOS OS CURSOS DE "CATEGORIA" QUE NÃO POSSUEM ESPAÇOS NO NOME
SELECT id 
  FROM categoria 
 WHERE nome NOT LIKE '% %';

-- CURSOS CUJOS NOME DA CATEGORIA POSSUI "DE"
SELECT curso.nome 
  FROM curso 
 WHERE categoria_id 
    IN (
        SELECT id 
        FROM categoria 
        WHERE nome LIKE '% de %'
);

-- FILTRAR CURSOS CUJO NOME DA CATEGORIA NÃO POSSUEM ESPAÇOS
SELECT curso.nome FROM curso WHERE categoria_id IN (
	SELECT id FROM categoria WHERE nome NOT LIKE '% %'
);

-- SELECIONAR OS CURSOS INCLUÍDOS EM CATEGORIAS QUE COMECEM COM
-- A LETRA "D" 
SELECT curso.nome FROM curso WHERE categoria_id IN (
	SELECT id FROM categoria WHERE nome LIKE 'D%'
);

-- SELECIONAR OS CURSOS INCLUÍDOS EM CATEGORIAS QUE TERMINEM COM
-- A LETRA "o" 
SELECT curso.nome FROM curso WHERE categoria_id IN (
	SELECT id FROM categoria WHERE nome LIKE '%o'
);

-- RELATÓRIO COM TODOS OS DADOS DOS ALUNOS E TODOS OS DADOS DOS CURSOS 
-- NOS QUAIS ESTÃO MATRICULADOS
SELECT *
FROM aluno a 
JOIN aluno_curso ac ON ac.aluno_id = a.id 
JOIN curso c ON c.id = ac.curso_id;

-- FILTRANDO A CATEGORIA QUE TEM MAIS CURSOS EXISTENTES
  SELECT c.nome, 
         count(c2.id) AS numero_cursos
    FROM categoria c 
    JOIN curso c2 ON c2.categoria_id = c.id
GROUP BY c.nome
ORDER BY c.nome, numero_cursos desc
limit 1;


-- SUBQUERIES
-- RELATÓRIO COM TODAS AS CATEGORIAS QUE TEM QUANTIDADE DE CURSOS MAIOR QUE 5
SELECT categoria,
       numero_cursos
FROM (
  SELECT categoria.nome AS categoria, 
         COUNT(curso.id) AS numero_cursos
    FROM categoria 
    JOIN curso ON curso.categoria_id = categoria.id
GROUP BY categoria
) AS categoria_cursos
WHERE numero_cursos > 5;

-- RELATÓRIO COM TODAS AS CATEGORIAS QUE TEM QUANTIDADE DE CURSOS MAIOR QUE 3
SELECT categoria,
       numero_cursos
FROM (
  SELECT categoria.nome AS categoria, 
         COUNT(curso.id) AS numero_cursos
    FROM categoria 
    JOIN curso ON curso.categoria_id = categoria.id
GROUP BY categoria
) AS categoria_cursos
WHERE numero_cursos > 3;

-- PODEMOS SIMPLIFICAR A QUERY ANTERIOR USANDO HAVING:
  SELECT categoria.nome AS categoria, 
         COUNT(curso.id) AS numero_cursos
    FROM categoria 
    JOIN curso ON curso.categoria_id = categoria.id
GROUP BY categoria
  HAVING COUNT(curso.id )> 3;

-- RELATÓRIO COM TODAS AS CATEGORIAS QUE TEM QUANTIDADE DE CURSOS IGUAL A 3
SELECT categoria,
       numero_cursos
FROM (
  SELECT categoria.nome AS categoria, 
         COUNT(curso.id) AS numero_cursos
    FROM categoria 
    JOIN curso ON curso.categoria_id = categoria.id
GROUP BY categoria
) AS categoria_cursos
WHERE numero_cursos = 3
ORDER BY categoria;


-- FUNÇÕES DE STRING
SELECT (primeiro_nome || ' ' || ultimo_nome) as nome_completo from aluno;

-- EXIBIR O PRIMEIRO NOME + ESPAÇO (IGNORANDO VALORES NULOS)
"""
-- SE A QUERY FOR SOLICITADA ASSIM:
SELECT ('Vinicius' || ' ' || NULL); 
-- VAI RETORNAR TUDO NULO
"""
SELECT CONCAT('Vinicius', ' ', NULL);

SELECT CONCAT('Vinicius', ' ', 'José de Alencar');

SELECT UPPER(CONCAT('Vinicius', ' ', NULL));

SELECT LOWER(CONCAT('Vinicius', ' ', NULL, 'José de Alencar'));

-- A FUNÇÃO TRIM ELIMINA ESPAÇOS ANTES E DEPOIS DA STRING
SELECT TRIM(UPPER(CONCAT('Vinicius', ' ', NULL, 'José de Alencar')) || ' ');

--FUNÇÕES DE DATA
SELECT NOW();

SELECT TO_CHAR(NOW(), 'DD/MM/YYYY');

SELECT TO_CHAR(128,3::REAL,'999D99');

SELECT (primeiro_nome || ' ' || ultimo_nome) AS nome_completo, 
       NOW()::DATE,   -- converte de now (timestamp) para date
       data_nascimento 
  FROM aluno;
 
SELECT (primeiro_nome || ' ' || ultimo_nome) AS nome_completo, 
       AGE(data_nascimento) as idade
  FROM aluno;

SELECT (primeiro_nome || ' ' || ultimo_nome) AS nome_completo, 
       EXTRACT(YEAR FROM AGE(data_nascimento)) as idade
  FROM aluno;

-- FUNÇÕES ARITMÉTICAS
SELECT PI();

SELECT @ -13145454648;


-- VIEWS
-- CONCEITO DE VIEW: UTILIZAR UMA TABELA VIRTUAL E DAR UM NOME PRA ELA

-- CRIAR VIEW "CURSOS POR CATEGORIA"
CREATE VIEW vw_cursos_por_categoria AS SELECT categoria.nome AS categoria, 
         COUNT(curso.id) AS numero_cursos
    FROM categoria 
    JOIN curso ON curso.categoria_id = categoria.id
GROUP BY categoria;

SELECT * FROM vw_cursos_por_categoria vcpc;

-- CRIAR VIEW "CURSOS DE PROGRAMAÇÃO"
CREATE VIEW vw_cursos_programacao AS SELECT nome FROM curso WHERE categoria_id = 2;

SELECT * FROM vw_cursos_programacao;

SELECT * FROM vw_cursos_programacao WHERE nome = 'PHP';

-- JOIN COM VIEWS
SELECT categoria.id AS categoria_id, vw_cursos_por_categoria.*
FROM vw_cursos_por_categoria 
JOIN categoria ON categoria.nome = vw_cursos_por_categoria.categoria;





































