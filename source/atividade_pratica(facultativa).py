#importar biblioteca sqlite3
import sqlite3

# caminho do arquivo
path = r'F:/Users/marba/Documents/IFRN programador de sistemas/banco de dados/'

# conexão com o banco
banco = sqlite3.connect(path + r'/perfumaria.db')

# permissão para fazer alterações nas tabelas do banco
cursor = banco.cursor()

# executar comandos sql
cursor.execute("CREATE TABLE Marcas (id integer not null primary key autoincrement,nome varchar(100))")
cursor.execute("CREATE TABLE Fixacoes (id integer not null primary key autoincrement, nome varchar(100))")
cursor.execute("CREATE TABLE Volumes (id integer not null primary key autoincrement, nome varchar(100))")
cursor.execute("CREATE TABLE Essencias (id integer not null primary key autoincrement, nome varchar(100))")

cursor.execute("CREATE TABLE Perfumes (id integer not null primary key autoincrement, nome varchar(100) ,quantidade integer, \
                id_volume_FK integer not null, id_marca_FK integer not null, id_fixacao_FK integer not null, \
                CONSTRAINT volume_FK FOREIGN KEY (id_volume_FK) REFERENCES Volume (id), \
                CONSTRAINT marca_FK FOREIGN KEY (id_marca_FK) REFERENCES Marcas (id), \
                CONSTRAINT fixacoes_FK FOREIGN KEY (id_fixacao_FK) REFERENCES Fixacoes (id))")

cursor.execute("CREATE TABLE Essencia_Perfume (id_essencia_FK integer not null, id_perfume_FK integer not null, \
                PRIMARY KEY (id_essencia_FK, id_perfume_FK), \
                CONSTRAINT essencia_FK FOREIGN KEY (id_essencia_FK) REFERENCES Essencias (id), \
                CONSTRAINT perfume_FK FOREIGN KEY (id_perfume_FK) REFERENCES Perfurmes (id))")
