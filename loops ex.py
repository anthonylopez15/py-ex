produtos = []
resposta = 's'
total = 0
valide_preco = False

while resposta == 's':
    produto = input('Nome do produto: ')

    while valide_preco == False:
        preco = input('Digite o preco do produto: ')
        try:
            preco = float(preco)

            if preco <= 0:
                print('O preco precisa ser maior que zero')
            else:
                valide_preco = True
        except:
            print("Formato de preco invalido. Use apenas numeros e separe os centavos com '.'.")
    
    produtos.append([produto, preco])
    total += preco
    valide_preco = False
    resposta = input('Deseja continuar?').lower()

print('Saiu do while')

for i in produtos:
    print(i[0], ':', i[1])

print('Total:', total)
