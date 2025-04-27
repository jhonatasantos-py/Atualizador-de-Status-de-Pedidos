#usar a api de subir status no order e criar aqui pra fazer de forma massiva 

import requests

from dotenv import load_dotenv
import os
load_dotenv()


lista_consigment = [

'5554290830001'
]

url = os.getenv("ORDER_API_URL")

headers = {
    "Content-Type" : "application/json",
    "Authorization": os.getenv("CAMUNDA_AUTHORIZATION")

}



for consigment in lista_consigment: 
   
    pedido = consigment[:-4]

    body = {
    "orderEntries": [
        {
        "codigo_pedido": pedido,
        "codigo_entrega": consigment,
        "codigo_status": "CAR"
        }
    ]
    }

    try:

        solicitacao = requests.post(url, headers=headers, json=body )

        if solicitacao.status_code == 200:
            print(f'status do pedido: {pedido} atualizado com sucesso')

        else:
            print(f' ERRO AO ATUALIZAR STATUS DO PEDIDO {pedido} = {solicitacao.status_code} - {solicitacao.text}')


    except requests.exceptions.RequestException as erro:
        print(f" Erro de conexão ao enviar o pedido {pedido}: {erro}")

