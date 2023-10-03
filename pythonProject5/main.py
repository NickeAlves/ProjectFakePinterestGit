import pandas as pd

lista_meses = ['Teste python']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 50).any:
        Vendedor = tabela_vendas['Vendas'] > 50,'Nome'.values[0]
        Vendas = tabela_vendas['Vendas'] > 50, 'Valor'.values[0]
        print('Alguém alcançou a meta. Nome: {Nome} Valor: {Valor}')













