import os
os.system('cls')
while True:
    print('- - - - ' * 5)
    print('Escolha uma das opções abaixo:')
    print('[D] Dados do projeto\n[1] Binário\n[2] Octal\n[3] Hexadecimal\n[x] Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao in "d,D":
        print('Curso: Análise e Desenvolvimento de Sistemas\n Responsáveis pelo projeto:\n Antonio Marley 32593775;\n Isaque Gonçalves 33032955;\n Lucas Gonçalves 32766068;\n Luiz Felipe Silva 32654545;\n Nicolas Eeisuke 32654073.\n Diciplinas Envolvidas:\n Programação de Computadores: prof. Marco Antonio Sanches Anastacio \n Organização e Arquitetura de Computadores: prof. Thier Roberto Zarsa Alarcon de Oliveira \n Versão: 1.4')
    elif opcao in "x,X":
        print('Programa encerrado!')
        input('Pressione "enter" para contiuar...')
        break
    elif opcao in "1, 2, 3":
        n = int(input('Digite um número: '))
        if opcao == '1':
            binario = ''
            while n > 0:
                resto = n % 2
                binario = str(resto) + binario
                n = n // 2
            print(f'O resultado da converção do número digitado é: {binario}')
        elif opcao == '2':
            octa = ''
            while n > 0:
                resto = n % 8
                octa = str(resto) + octa
                n = n // 8
            print(f'O resultado da converção do número digitado é: {octa}')

        elif opcao == '3':
            hexa = ''
            while n > 0:
                resto = n % 16
                if resto == 10:
                    resto = 'A'
                if resto == 11:
                    resto = 'B'
                if resto == 12:
                    resto = 'C'
                if resto == 13:
                    resto = 'D'
                if resto == 14:
                    resto = 'E'
                if resto == 15:
                    resto = 'F'
                hexa = str(resto) + hexa
                n = n // 16

            print(f'O resultado da converção do número digitado é: {hexa}')
        else:
            print('Opção invalida!')
    else:
        print('Opção invalida!')