# importando biblioteca sqlite3
import sqlite3

# conexão com o banco.
path = r'F:/Users/marba/Documents/IFRN programador de sistemas/banco de dados/'
banco = sqlite3.connect(path + r'/perfumaria.db')
cursor = banco.cursor()

# inserindo valores nas tabelas.
cursor.execute(f"INSERT INTO Marcas (nome) VALUES ('Boticário')")
cursor.execute(f"INSERT INTO Marcas (nome) VALUES ('Natura')")
cursor.execute(f"INSERT INTO Volumes (nome) VALUES (115)")
cursor.execute(f"INSERT INTO Volumes (nome) VALUES (115)")
cursor.execute(f"INSERT INTO Essencias (nome) VALUES ('Flores')")
cursor.execute(f"INSERT INTO Essencias (nome) VALUES ('Mel')")
cursor.execute(f"INSERT INTO Fixacoes (nome) VALUES ('24H')")
cursor.execute(f"INSERT INTO Fixacoes (nome) VALUES ('48H')")
# inserindo valores para campos especificados.
cursor.execute(f"INSERT INTO Perfumes (nome, quantidade,id_volume_FK,id_marca_FK,id_fixacao_FK) VALUES ('Malbec',5,1,1,1)")
cursor.execute(f"INSERT INTO Perfumes (nome, quantidade,id_volume_FK,id_marca_FK,id_fixacao_FK) VALUES ('Kaiak',10,2,2,2)")
cursor.execute(f"INSERT INTO Essencia_Perfume (id_essencia_FK,id_perfume_FK) VALUES (1,1)")
cursor.execute(f"INSERT INTO Essencia_Perfume (id_essencia_FK,id_perfume_FK) VALUES (2,2)")
banco.commit()