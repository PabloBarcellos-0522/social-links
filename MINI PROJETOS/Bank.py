import time
import sqlite3
import os
import pdb

# conexao = sqlite3.connect('./MINI PROJETOS/bancodedados.db')
conexao = sqlite3.connect('c:\\Users\\pablo\\OneDrive\\Desktop\\Programação\\social-links\\Projetos\\MINI PROJETOS\\bancodedados.db')
cursor = conexao.cursor()

#ID_senhas: 1, usuario: pablo, senha: 123 

#ID_senhas: 2, usuario: Pablo2, senha: 0522 

#ID_senhas: 3, usuario: pablao, senha: 052204

#comando = "CREATE TABLE senhas (ID INTEGER PRIMARY KEY, usuario VARCHAR(100), senha VARCHAR(140), idade VARCHAR(100), saldo VARCHAR(100))" #<---NA PARTE DE VIDEOS, COLOQUE O NOME DA TABELA
#cursor.execute(comando)

#cursor.execute("INSERT INTO senhas VALUES(1, 'pablo', '123', '20', 0)")#<---NA PARTE DE VIDEOS, COLOQUE O NOME DA TABELA
#conexao.commit()

#cursor.execute("INSERT INTO senhas VALUES(2, 'Pablo2', '0522')")#<---NA PARTE DE VIDEOS, COLOQUE O NOME DA TABELA
#conexao.commit()

#cursor.execute("INSERT INTO senhas VALUES(3, 'pablao', '052204', '20')")#<---NA PARTE DE VIDEOS, COLOQUE O NOME DA TABELA
#conexao.commit()

#cursor.execute("DELETE FROM senhas WHERE ID = 3")#<---- id do registro
#conexao.commit()

#comando = 'select * from senhas'#<---NOME DA TABELA
#cursor.execute(comando)
#dados = cursor.fetchall()
#for linha in dados:
 # print('ID_senhas: %d, usuario: %s, senha: %s, idade: %s, saldo: %s \n' % linha)

print("Bem vindo ao BANK-Pablo!")
print("Você já tem um cadastro?")
cadastro = input()


if cadastro == "não" or cadastro == "Não" or cadastro == "n" or cadastro == "N":
  print("vamos iniciar seu cadastro:")
  time.sleep(0.5)
  print('crie seu nome de usuário:')
  nome = input()
  print("digite sua idade:")
  idade_cliente = int(input ())


  if idade_cliente < 18:
    print("digite o primeiro nome do seu responsável:")
    responsável = input()
    print("digite a idade numérica do seu responsável:")
    idade_resp = int(input())
    print("seu responsavel é seu pai sua mãe ou outro?")
    pai_mãe = input()
    diferença = idade_resp - idade_cliente

    if pai_mãe == "pai" or pai_mãe == "mãe":
      if pai_mãe == "pai":
        genero = "seu"

      else:
        genero = "sua"
      print(f"voçê é {diferença} anos mais novo que {genero} {pai_mãe}")

    else:
      if pai_mãe != "pai" and "mãe":
        print(f"voçê é {diferença} anos mais novo que seu Responsável")

  comando = 'select * from senhas'#<---NOME DA TABELA
  cursor.execute(comando)
  dados = cursor.fetchall()
  for linha in dados:
    linha
  id = list((linha))[0] + 1

  print("OK!, vamos criar sua senha:")
  time.sleep(0.5)
  print("crie sua senha:")
  senha = input()
  comando = 'INSERT INTO senhas VALUES(?, ?, ?, ?, ?)'
  registros = [('{}'.format(id), '{}'.format(nome), '{}'.format(senha), '{}'.format(idade_cliente), 0)]
  for registro in registros:
    cursor.execute(comando, registro)
    conexao.commit()

else:
  print('qual seu nome de usuário?')
  nome = input()



print("prontinho, agora é só logar na sua conta!")

def ler_registros():
  cursor.execute("SELECT * FROM senhas WHERE usuario = '{}'".format(nome))
  for linha in cursor.fetchall():
    return list(linha)[2]

execucao = True
while execucao:
  print("coloque sua senha:")
  password = input()

  if (password == ler_registros()):
    print("quer depositar ou sacar?")
    dep = input()

    if dep == "depositar":
      print("quanto?")
      valores = input()

      def id():
        cursor.execute("SELECT * FROM senhas WHERE usuario = '{}'".format(nome))
        for linha in cursor.fetchall():
          return list(linha)[0]
      def saldo():
        cursor.execute("SELECT * FROM senhas WHERE usuario = '{}'".format(nome))
        for linha in cursor.fetchall():
          return list(linha)[4]
    

      saldo_total= int(saldo()) + int(valores)
      

      cursor.execute("UPDATE senhas SET saldo = {} WHERE ID = {}".format(saldo_total, id()))
      conexao.commit()

      time.sleep(1.5)
      print(f"\n {valores} depositados com sucesso!!!, seu saldo agora é de: {saldo_total} reias.")
      time.sleep(2)
      

      print('\nquer continuar utilizando o BANK-Pablo?')
      continuar = input()
      if continuar == "sim" or continuar == "Sim" or continuar == "s" or continuar == "S":
        execucao = True
      else:
        execucao = False

    elif dep == "sacar":
      print("quanto?")
      valores = input()

      def id():
        cursor.execute("SELECT * FROM senhas WHERE usuario = '{}'".format(nome))
        for linha in cursor.fetchall():
          return list(linha)[0]
      def saldo():
        cursor.execute("SELECT * FROM senhas WHERE usuario = '{}'".format(nome))
        for linha in cursor.fetchall():
          return list(linha)[4]
      
      if int(saldo()) > int(valores):

        saldo_total = int(saldo()) - int(valores)
        
        cursor.execute("UPDATE senhas SET saldo = {} WHERE ID = {}".format(saldo_total, id()))
        conexao.commit()
      print('loading...')

      time.sleep(1.5)
      print(f"\n {valores} reais sacados com sucesso!!!, seu saldo agora é de: {saldo_total} reias.")
      time.sleep(2)

      print('\n quer continuar utilizando o BANK-Pablo?')
      continuar = input()
      if continuar == "sim" or continuar == "Sim" or continuar == "s" or continuar == "S":
        execucao = True
      else:
        execucao = False
    else:
      print("não entendi sua solicitação :/ ")
      execucao = True
  else:
    print("senha incorreta!!!")
    execucao = True
else:
  print('obrigado por usar nosso programa ;)')