import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, DateTime, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    "postgresql+psycopg2://postgres:12345@localhost/pizzaria_3",
    execution_options={
        "isolation_level": "REPEATABLE_READ"
    },
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column('id', Integer, primary_key=True)
    nome = Column('nome', String)
    email = Column('email', String)
    endereco = Column('endereco', String)


class Pizza(Base):
    __tablename__ = 'pizza'
    id = Column('id', Integer, primary_key=True)
    nome = Column('nome', String)
    descricao = Column('descricao', String)
    categoria = Column('categoria', String)
    preco = Column('preco', Float)


class Pedido(Base):
    __tablename__= 'pedido'
    id = Column('id', Integer, primary_key=True)
    id_cliente = Column('id_cliente', Integer, ForeignKey("cliente.id"), nullable=False)
    observacao = Column('observacao', String, nullable=True)
    tipo_entrega = Column('tipo_entrega', String, nullable=False)
    preco = Column('preco', Float, nullable=True)
    data_pedido = Column('data_pedido', DateTime, nullable=True)

# Base.metadata.create_all(engine)

"""
cliente1 = Cliente(nome="Rael", email="rael@email.com", endereco="Rua Albert Einstein")
pizza1 = Pizza(nome="Calabresa", descricao="Massa baixa e borda recheada com catupiry", categoria="Pizza Salgada", preco=27.90)

session.add_all([cliente1, pizza1])
session.commit()
print(cliente1.nome, pizza1.nome)
"""

pedido1 = Pedido(id=1, id_cliente=1, observacao="Substituir o catupiry da borda por queijo tipo reino" , tipo_entrega="Entrega à domicílio, com frete grátis." , preco=27.90 , data_pedido="10-2-2021")
session.add(pedido1)
session.commit()
print(pedido1)
