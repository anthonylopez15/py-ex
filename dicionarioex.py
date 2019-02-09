cores = {'vermelho':'red', 'azul':'blue', 'verde':'green'}
cor = input('Escolha a cor q deseja traduzir: ').lower()
traducao = cores.get(cor, 'Cor nao encontrado no meu dicionario')
print(traducao)
