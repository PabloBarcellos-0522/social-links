#importação e atribuições:
import sqlite3
conexao = sqlite3.connect('./MINI PROJETOS/bancodedados.db')
cursor = conexao.cursor()



#criação de tabela/instrução/comando sql:
comando = "CREATE TABLE VIDEOS (ID INTEGER PRIMARY KEY, TITULO VARCHAR(100), CATEGORIA VARCHAR(140))" #<---NA PARTE DE VIDEOS, COLOQUE O NOME DA TABELA
cursor.execute(comando)



#inserir informações, forma 1:
cursor.execute("INSERT INTO VIDEOS VALUES(1, 'Banco de Dados SQlite', 'Banco de Dados')")#<---NA PARTE DE VIDEOS, COLOQUE O NOME DA TABELA
conexao.commit()



#inserir informações, forma 2:
comando = 'INSERT INTO VIDEOS VALUES(?, ?, ?)'
registros = [(2, '123', 'senha')]#<---- escreva todos os registros separados por virgula
for registro in registros:
  cursor.execute(comando, registro)
conexao.commit()



#ler registros (TODOS):
comando = 'select * from videos'#<---NOME DA TABELA
cursor.execute(comando)
dados = cursor.fetchall()
for linha in dados:
  print('ID_VIDEO: %d, Titulo: %s, Categoria: %s \n' % linha)



#ler registros (ESPECÍFICOS):
def ler_registros():
  cursor.execute("SELECT * FROM VIDEOS WHERE CATEGORIA = 'senha'")#<---- categoria do registro
  for linha in cursor.fetchall():
    #a = list(linha)[1]
    a = list(linha)
    print(f"\n\n{a}")
ler_registros()



#update registros:
cursor.execute("UPDATE VIDEOS SET TITULO = '123' WHERE ID = 2")#<---- id do registro
conexao.commit()



#delete registros:
cursor.execute("DELETE FROM VIDEOS WHERE ID = 2")#<---- id do registro
conexao.commit()