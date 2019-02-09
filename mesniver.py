meses = ('Janeiro','Fevereio', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

data_nasc = input('Data de nascimento: DD-MM-AAAA ')
data = int(data_nasc[3:5])-1
msg = 'Voce nasceu no mes de'
print(msg, meses[data])
