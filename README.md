
# 📊 Script de Relatório de Vendas por Loja

Este script em Python tem como objetivo gerar um relatório de vendas a partir de uma planilha do Excel e enviá-lo via e-mail para a diretoria.

## 🚀 Funcionalidades
- Importa uma base de dados do Excel.
- Processa os dados para calcular:
  - Faturamento por loja.
  - Quantidade de produtos vendidos por loja.
  - Ticket médio dos produtos vendidos em cada loja.
- Gera um e-mail estruturado com os dados formatados em tabelas HTML.
- Envia o e-mail automaticamente usando a biblioteca `yagmail`.

---
## 🛠️ Requisitos
Antes de executar o script, certifique-se de ter instalado as seguintes dependências:

```bash
pip install pandas yagmail python-dotenv openpyxl
```

Também é necessário configurar uma senha de aplicativo para uso com o Gmail.

---
## 📂 Estrutura do Projeto
```
/
|-- .env
|-- Vendas.xlsx
|-- main.py
|-- README.md
```

### 📌 Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto para armazenar as credenciais de e-mail e o caminho do arquivo Excel:

```
EMAIL_USER=seuemail@gmail.com
EMAIL_PASSWORD=sua_senha_de_aplicativo
VENDAS_FILE_PATH=Vendas.xlsx
```

> **Nota:** Nunca compartilhe sua senha real. Sempre use App Passwords!

---
## 📝 Como Executar o Script
1. **Configure o ambiente**
   - Instale as dependências com `pip install -r requirements.txt` (se tiver um `requirements.txt`).
   - Configure o arquivo `.env` corretamente.
   - Certifique-se de que o arquivo `Vendas.xlsx` esteja no local correto.

2. **Execute o script**
   ```bash
   python main.py
   ```

3. **Verifique o console**
   Se tudo estiver correto, você verá a mensagem:
   ```
   E-mail enviado com sucesso!
   ```

---
## 🏗️ Como o Script Funciona
1. **Carrega a base de dados** do Excel.
2. **Configura a exibição dos dados** para evitar limitação de colunas.
3. **Calcula**:
   - O faturamento por loja.
   - A quantidade de produtos vendidos.
   - O ticket médio por loja.
4. **Carrega as credenciais** do arquivo `.env`.
5. **Gera um e-mail HTML** formatado com as informações.
6. **Envia o e-mail** automaticamente.

---
## 📧 Exemplo de E-mail Gerado

O e-mail enviado contém tabelas bem formatadas com os dados de faturamento, quantidade vendida e ticket médio, como no exemplo abaixo:

---
**Assunto:** Relatório de Vendas por Loja

Prezados,

Segue o relatório de vendas por cada loja:

**Faturamento:**

| ID Loja | Valor Final |
|---------|------------|
| Loja A  | USD$10,000.00 |
| Loja B  | USD$8,500.00 |

**Quantidade de produtos vendidos:**

| ID Loja | Quantidade |
|---------|------------|
| Loja A  | 1,200 |
| Loja B  | 950 |

**Ticket médio dos produtos em cada loja:**

| ID Loja | Ticket Médio |
|---------|------------|
| Loja A  | USD$8.33 |
| Loja B  | USD$8.95 |

Qualquer dúvida, estou à disposição.

Atenciosamente,
**Francisco Bowe**

---

## ⚠️ Observação Importante
- Se for compartilhar seu código no GitHub, adicione o `.env` ao `.gitignore` para evitar expor suas credenciais.

Exemplo de `.gitignore`:
```
.env
*.xlsx
```

---
## 📌 Melhorias Futuras
- Adicionar logging para monitorar envios.
- Permitir escolha do destinatário via entrada do usuário.
- Melhorar formatação das tabelas HTML.

---
## 📞 Dúvidas?
Caso tenha alguma dúvida ou sugestão, fique à vontade para entrar em contato!

😊🚀

