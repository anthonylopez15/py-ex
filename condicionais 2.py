idade = int(input('Qual a sua idade: '))
sexo = input('Qual eh seu genero: ').lower()
cidade = input('Qual a sua cidade: ').lower()

if cidade == 'rio' or cidade == 'sao paulo':
    if sexo == 'm':
        if idade < 18:
            print('Homem menor de idade, da regiao sudeste')
        else:
            print('Homem maior de idade, da regiao sudeste')
    elif sexo == 'f':
        if idade < 18:
            print('Mulher menor de idade, da regiao sudeste')
        else:
            print('Mulher maior de idade, da regiao sudeste')
    else:
        print('Erro de entrada de dados')
else:
    print('Teste para a regiao sudeste')
