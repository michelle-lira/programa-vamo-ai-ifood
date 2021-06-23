import datetime
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Date, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import or_, and_
from sqlalchemy.sql import func

engine = create_engine('postgresql+psycopg2://postgres:12345@localhost/qualified_18', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

class Cliente(Base):
    __tablename__= 'cliente'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    nome = Column('nome', String(30), nullable=False)
    sobrenome = Column('sobrenome', String(60), nullable=False)
    email = Column('email', String(50), nullable=False)
    data_cadastro = Column('data_cadastro', String(10), nullable=False)
    cliente_venda_relationship = relationship("Venda")

class Venda(Base):
    __tablename__= 'venda'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    cliente_id = Column('cliente_id', Integer, ForeignKey("cliente.id"), nullable=False)
    data_venda = Column('data_venda', String(10), nullable=False)
    venda_produto_venda_relationship = relationship("ProdutoVenda")

class Produto(Base):
    __tablename__= 'produto'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    nome = Column('nome', String(70), nullable=False)
    preco = Column('preco', Float, nullable=True)
    produto_produto_venda_relationship = relationship("ProdutoVenda")

class ProdutoVenda(Base):
    __tablename__= 'produto_venda'
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    venda_id = Column('venda_id', Integer, ForeignKey("venda.id"), nullable=False)
    produto_id = Column('produto_id', Integer, ForeignKey("produto.id"), nullable=False)
    quantidade = Column('quantidade', Integer, nullable=False)
    

# Base.metadata.create_all(engine)

# Inserindo dados na tabela Cliente
cliente1 = Cliente(nome="Freddie", sobrenome="Mercury", email="the_champion@gmail.com", data_cadastro="2019-1-1")
cliente2 = Cliente(nome="Raul", sobrenome="Seixas", email="toca_raul@gmail.com", data_cadastro="2020-1-1")
cliente3 = Cliente(nome="Jim", sobrenome="Morisson", email="light_my_fire@outlook.com", data_cadastro="2020-5-1")
cliente4 = Cliente(nome="Amy", sobrenome="Whinehouse", email="losing_game@yahoo.com.br", data_cadastro="2020-5-1")

# session.add_all([cliente1, cliente2, cliente3, cliente4])
# session.commit()
# print(cliente1.nome, cliente2.nome, cliente3.nome, cliente4.nome)

# Inserindo dados na tabela Venda
"""
venda1 = Venda(cliente_id=1, data_venda="2020-5-1")
venda2 = Venda(cliente_id=2, data_venda="2021-2-15")
venda3 = Venda(cliente_id=1, data_venda="2021-6-16")
venda4 = Venda(cliente_id=3, data_venda="2018-9-30")

session.add_all([venda1, venda2, venda3, venda4])
session.commit()
print(venda1.id, venda2.id, venda3.id, venda4.id)
"""

# Inserindo dados na tabela Produto
"""
produto1 = Produto(nome="Óculos escuros", preco=145.50)
produto2 = Produto(nome="Calça jeans", preco=90.90)
produto3 = Produto(nome="Camiseta branca", preco=117.35)
produto4 = Produto(nome="Bota preta", preco=29.90)
produto5 = Produto(nome="Relógio", preco=45.20)

session.add_all([produto1, produto2, produto3, produto4, produto5])
session.commit()
print(produto1.nome, produto2.nome, produto3.nome, produto4.nome, produto5.nome)
"""

# Inserindo dados na tabela ProdutoVenda
"""
produto_venda1 = ProdutoVenda(venda_id=1, produto_id=1, quantidade=3)
produto_venda2 = ProdutoVenda(venda_id=2, produto_id=2, quantidade=1)
produto_venda3 = ProdutoVenda(venda_id=3, produto_id=3, quantidade=2)
produto_venda4 = ProdutoVenda(venda_id=4, produto_id=4, quantidade=1)

session.add_all([produto_venda1, produto_venda2, produto_venda3, produto_venda4])
session.commit()
print(produto_venda1.id, produto_venda2.id, produto_venda3.id, produto_venda4.id)
"""

# Queries
# Selecione tudo da tabela Cliente
"""
clientes = session.query(Cliente).all()

for cliente in clientes:
    print(cliente.nome, cliente.sobrenome, cliente.email, cliente.data_cadastro)
"""

# Implemente o código sql equivalente ao código abaixo:
# select * from cliente where data_cadastro > '2020-01-01'
"""
clientes = session.query(Cliente).filter(Cliente.data_cadastro>"2020-1-1").all()

for cliente in clientes:
    print(cliente.nome, cliente.sobrenome, cliente.email, cliente.data_cadastro)
"""

# Implemente o código sql equivalente ao código abaixo:
# update produto
# set preco = 29.90
# where id = 3
"""
produto = session.query(Produto).filter(Produto.id==3).first()
produto.preco = 29.90

session.commit()
"""

# Implemente o código sql equivalente ao código abaixo:
# delete from produto
# where id = 2
"""
produto = session.query(Produto).filter(Produto.id==2).first()
session.delete(produto)

session.commit()
"""

"""
12. Q7: Utilizando python + SQLAlchemy, implemente o código equivalente ao SQL abaixo:

SELECT
  id,
  nome,
  sobrenome
FROM cliente
WHERE
  email like '%@gmail%'
  and data_cadastro > '2019-01-01';

"""
"""
resultado = session.query(Cliente.id, Cliente.nome, Cliente.sobrenome).filter(and_(Cliente.email.like('%gmail%'), Cliente.data_cadastro>'2019-01-01')).all()
print(resultado)
"""

"""
13. Desafio 1

Q8: Utilizando python + SQLAlchemy, implemente o código equivalente ao SQL abaixo:

SELECT
  c.id,
  c.nome,
  c.sobrenome,
  v.id
FROM
  cliente c
  JOIN venda v ON c.id = v.cliente_id
WHERE
  v.data_venda > '2020-05-01'
"""
"""
resultado = session.query(Cliente.id, Cliente.nome, Cliente.sobrenome, Venda.id).join(Venda).filter(Venda.data_venda>'2020-05-01').all()
print(resultado)
"""

"""
14.
Desafio 2

Q8: Utilizando python + SQLAlchemy, implemente o código equivalente ao SQL abaixo:

SELECT
  p.id,
  SUM(pv.quantidade) as total_vendido
FROM
  produto p
  JOIN produto_venda pv ON p.id = pv.produto_id
GROUP BY
  p.id
"""
resultado = session.query(Produto.id, func.sum(ProdutoVenda.quantidade).label('total_vendido')).join(ProdutoVenda).group_by(Produto.id).all()
print(resultado)
