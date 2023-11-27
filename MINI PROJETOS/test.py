tupla = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco']


i = int(input('Digite um número: '))
ext = tupla[i]
print(f'Você digitou o número {ext}')
opcao = str(input('Quer continuar a ler os números por extenso? [S/N] ')).upper().strip()
while opcao == 'S':
    num = int(input('Então digita outro número: '))
    ext = tupla[num]
    print(f'Você digitou o número {ext}')
    opcao = str(input('Quer continuar a ler os números por extenso? [S/N] ')).upper().strip()
    while opcao == 'N':
      exit('Obrigado por usar nosso programa.')