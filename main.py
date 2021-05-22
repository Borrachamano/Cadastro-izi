lista = list()

while True:
	try:
		nm = str(input('Nome: '))
		altura = float(input('Altura: '))
		peso = float(input('Peso: kg'))
		imc = peso / (altura * altura)
		lista.append([nm, [altura, peso], imc])
		opc = str(input('Deseja continuar? [S/n]: ')).strip().upper()
		while opc != 'S' and opc != 'N' and opc != '':
			print('Opcao invalida. Tente novamente.')
			opc = str(input('Deseja continuar? [S/n]:|')).strip().upper()
		if opc == 'N':
			break
	except ValueError as erro:
		print(f'Message: {erro}')
	except ZeroDivisionError as erro:
		print(f'Message: {erro}')
	except:
		print('Error.')

print('-' * 40)

print(f'Pos {"Nome":^10} IMC')

print('-' * 40)

for p, i in enumerate(lista):
	print(f'{p} {i[0]:^12} {i[2]:.2f}')

print('-' * 40)

while True:
	try:
		info = int(input('Deseja ver o peso de qual usuario? (999 para sair): '))
		if info == 999:
			break
		if info >= 0 and info < len(lista):
			print(f'Peso de {lista[info][0]}: {lista[info][1]}')
		else:
			print('Esse pessoa não foi cadastrada.')
	except ValueError as erro:
		print(f'Message: {erro}')

print('-' * 40)

print('Programa emcerrado. Volte sempre!')

