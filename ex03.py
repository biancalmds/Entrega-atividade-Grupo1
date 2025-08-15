nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media <= 10 and media >= 9:
    print(f'Nota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: A')
    print('Aprovado')

elif media < 9 and media >= 7.5:
    print(f'Nota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: B')
    print('Aprovado')

elif media < 7.5 and media >= 6:
    print(f'Nota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: C')
    print('Aprovado')

elif media < 6 and media >= 4:
    print(f'Nota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: D')
    print('Reprovado')

elif media < 4 and media >= 0:
    print(f'Nota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print(f'Média: {media}')
    print(f'Conceito: E')
    print('Reprovado')