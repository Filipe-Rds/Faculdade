fixo = 1000.00
com = 200.00
perc = 5/100

vendedor = input('Nome do vendedor: ')
numcarros = int(input('Número de carros vendidos: '))
totvendas = float(input('Valor total das vendas: R$ '))

salario = fixo + numcarros*com + totvendas*perc

print(f'Salário: R$ {salario:.2f}')