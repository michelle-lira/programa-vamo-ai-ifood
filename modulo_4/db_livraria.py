"""
Código explicado detalhadamente em aula pela facilitadora
Letícia Silva:

Nessa parte do código, os imports do SQLAlchemy são feitos. 
Perceba que tudo o que está sendo utilizado da biblioteca precisa ser 
importado aqui em cima.
Você pode encontrar mais sobre os imports na documentação.
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Date
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, Session


"""
É onde fica armazenada coleções de objetos do tipo tabela e, normalmente, 
a ligação com a Engine ou Connection.
"""

metadata = MetaData()


"""
Nessa parte do código, a engine é criada. Ela é a responsável, a nível de 
código, pela conexão entre o seu código e o banco de dados.
"""

engine = create_engine(
"postgresql+psycopg2://postgres:12345@localhost/livraria"
)


"""
O declarative_base retorna uma nova classe "base", da qual todas as 
classes mapeadas devem herdar.
Você pode encontrar mais sobre esse comando na documentação.
"""

Base = declarative_base(metadata=metadata)


"""
Nessa parte do código, as tabelas são criadas. A estrutura foi baseada 
na documentação.
"""

books = Table("livros", metadata,
    Column('id', Integer, primary_key=True),
    Column('titulo', String),
    Column('autoria', String)
)

data = Table("dados", metadata,
    Column('lancamentos', Date),
    Column('ISBN', Integer),
    Column('codigo', Integer, primary_key=True)
)


"""
Esse método verifica a existência de cada tabela declarada. 
Se ela não for encontrada, a instrução Create é rodada.
"""

metadata.create_all(engine)


"""
O comando inspector executa, literalmente, a inspeção do esquema do 
banco de dados.
"""

inspector = inspect(engine)
print(inspector.get_columns('livros'))
print(inspector.get_columns('dados'))


"""
Aqui, os dados da tabela são mapeadas no código. 
O mapeamento serve para que você consiga acessar as tabelas pelo seu código, 
fazer consultas e manipulações.
"""

class Livros(Base):
    __tablename__ = 'livros'
    id = Column('id', Integer, primary_key=True)
    _titulo = Column('titulo', String)
    autoria = Column('autoria', String)


"""
Aqui, os dados da tabela são mapeadas no código. 
O mapeamento serve para que você consiga acessar as tabelas pelo seu código, 
fazer consultas e manipulações. Para saber mais, acesse aqui.
"""

class Dados(Base):
    __tablename__ = 'dados'
    lancamentos = Column('lancamentos', Date)
    isbn = Column('ISBN', Integer)
    codigo = Column('codigo', Integer, primary_key=True)


"""
@validates é um dos decorators do SQLAlchemy, utilizado para construir uma validação 
dentro do código. Sua estrutura pode ser encontrada na documentação.
No link, também está disponível um exemplo de declaração de uma função.
raise é um comando muito utilizado para o tratamento de exceções (ou exceptions).
Ele, junto com o ValueError podem ser encontrados na documentação da linguagem.
"""


@validates('isbn')
def validate_ISBN(self, key, isbn):
    print("entrou")
    print(isbn)
    if len(str(isbn)) != 13:
        raise ValueError(
                "O ISBN precisa conter 13 dígitos")
    else:
        print("O ISBN está correto")


"""
O comando session permite que você execute consultas dentro do banco de dados, 
tendo vários módulos podendo ser associados.
"""

with Session(engine) as session:
    dados_do_livro = Dados()
    dados_do_livro.isbn = 12345678901239
    session.add(dados_do_livro)
    session.commit()
