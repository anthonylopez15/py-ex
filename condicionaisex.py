nome = input('Nome: ')

valideNota = False
while valideNota == False:

    nota1 = input('Nota 1: ')
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print('Nota 1 inválida. Valor deve ser entre 0 e 10.')
        else:
            valideNota = True
    except:
        print('Entrada errada para nota. Deve ser decimais com ponto. (Ex: 9.3)')

valideNota = False
while valideNota == False:

    nota2 = input('Nota 2: ')
    try:
        nota2 = float(nota2)
        if nota2 < 0 or nota2 > 10:
            print('Nota 2 inválida. Valor deve ser entre 0 e 10.')
        else:
            valideNota = True
    except:
        print('Entrada errada para nota. Deve ser decimais com ponto. (Ex: 9.3)')

validaFalta = False
while validaFalta == False:
    faltas = input('Quantidade de faltas: ')
    try:
        faltas = float(faltas)
        if faltas < 0 or faltas > 20:
            print('Faltas devem ser entre 0 e 20')
        else:
            validaFalta = True
    except:
        print('Nota invalida. Use apenas números e separe os decimais com ponto.')
        
media = (nota1 + nota2)/2
assid = (20 - faltas)/20
print('entrou no else')
if media >= 6 and assid >= 0.7:
    resultado = 'Arpovado'
elif media < 6 and assid < 0.7:
    resultado = 'Reprovadopor nota e por falta'
elif media < 6:
    resultado = 'Reprovado por nota'
elif assid < 0.7:
    resultado = 'Reprovado por falta'
else:
    resultado = 'Erro'
    
print('saiu do while')
print()
print('Nome:', nome)
print('Media:', media)
print('Assiduidade: ', assid*100, '%')
print('Resutado:', resultado)



