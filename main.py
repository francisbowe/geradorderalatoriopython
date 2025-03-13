import os
import pandas as pd
import yagmail
from dotenv import load_dotenv


#importar Base Dados
# Get the file path from an environment variable
file_path = os.getenv('VENDAS_FILE_PATH', 'Vendas.xlsx')
tabela_vendas = pd.read_excel(file_path)
#print(tabela_vendas)

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
load_dotenv ()

# Obtém credenciais do ambiente
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Verifica se as credenciais foram carregadas
if not EMAIL_USER or not EMAIL_PASSWORD:
    raise ValueError("Erro: EMAIL_USER ou EMAIL_PASSWORD não definidos corretamente!")

# Configura o yagmail
yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASSWORD)

# Envia e-mail
yag.send(
    to="franciscobowe10@gmail.com",
    subject="Teste de E-mail",
    contents="Este é um teste de envio de e-mail usando yagmail no macOS!"
)

print("E-mail enviado com sucesso!")
