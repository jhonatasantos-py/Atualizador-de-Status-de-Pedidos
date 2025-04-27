# Atualizador de Status de Pedidos - Script em Python

Este é um script simples em Python para atualização massiva de status de pedidos via API.

## Sobre o Projeto

O script realiza:
- Autenticação via token usando variável de ambiente
- Atualização de status de pedidos em massa
- Tratamento de respostas da API
- Tratamento de erros de conexão

## Como Usar

1. Instale as dependências necessárias:

```bash
pip install requests python-dotenv
```

2. Crie um arquivo .env no seu computador com as seguintes variáveis:

```
CAMUNDA_AUTHORIZATION=seutoken
ORDER_API_URL=https://sua-url-aqui/order-status
```
3. Atualize a lista lista_consigment no código com os pedidos que deseja alterar.

4.Rode o script:
```
python nome_do_seu_script.py
```
## Observação
A URL da API e o token de autorização devem ser armazenados em variáveis de ambiente para manter a segurança.
