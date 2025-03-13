import os
import pandas as pd


#importar Base Dados
# Get the file path from an environment variable
file_path = os.getenv('VENDAS_FILE_PATH', 'Vendas.xlsx')
tabela_vendas = pd.read_excel(file_path)
print(tabela_vendas)

#visualizar a base de dados
pd.set_option('display.max_columns', None)
#print(tabela_vendas)

#faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
#print(faturamento)
#quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
#print(quantidade)
#ticket médio por produto em cada loja
media_ticket = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
media_ticket = media_ticket.rename(columns={0: 'Ticket Médio'})
#print(media_ticket)

#enviar e-mail para diretoria com resumo do faturamento por loja

email = input('Qual o seu e-mail?')
