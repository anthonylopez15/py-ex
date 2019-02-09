pesonota1 = int(input('Qual o peso da nota 1 = '))
pesonota2 = int(input('Qual o peso da nota 2 = '))
nota1 = float(input('Insira a nota 1 = '))
nota2 = float(input('Insira a nota 2 = '))

resultado = ((nota1 * pesonota1) + (nota2 * pesonota2))/(pesonota1 + pesonota2)

print('Nota do aluno', resultado)


