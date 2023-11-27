print("digite apenas 1 vez com SIM ou NÃO, blz?:")
loop = True
while loop:
  concord = input()
  if concord == "blz" or concord == "ok" or concord == "sim":
    loop2 = True
    print("você é gay?")
    resposta1 = input()
    while loop2:
      if resposta1 == "sim":
        print("você está mentindo?")
        resposta2 = input()
        if resposta2 == "não":
          print('parabêns, você é assumiu que é GAY!!!')
          loop2 = False
          loop = False
        else:
          if resposta2 == 'sim':
            print('incorreto!, não pode repetir a palavra "sim"')
          else:
            print(f'incorreto!, a palavra "{resposta2}" é inválida')
      elif resposta1 == "não":
        print("você está mentindo?")
        resposta2 = input()
        if resposta2 == "sim":
          print('parabêns, você é assumiu que é GAY!!!')
          loop2 = False
          loop = False
        else:
          if resposta2 == 'não':
            print('incorreto!, não pode repetir a palavra "não"')
          else:
            print(f'incorreto!, a palavra "{resposta2}" é inválida')
  else: 
    print("blz?")
    loop = True