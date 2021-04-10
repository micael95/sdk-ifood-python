# SDK PYTHON
SDK de integração IFood em python

Quer contribuir ? Envie seu PR <span>&#128526;</span>
## Introdução
Criação de sdk com intuito de aprendizado próprio na geração de pacotes opensource

Para que você possa realizar os testes crie sua conta de desenvolvedor no novo portal do desenvolvedor do IFood

<a href="https://developer.ifood.com.br/sign-in" target="_blank">Clique aqui para acessar o portal do Dev do IFood</a>

### Documentação
As funções são bem intuitivas, basta dar uma breve olhada na documentação da API do IFood e solicitar o desejado no SDK

<a href="https://developer.ifood.com.br/docs/references" target="_blank">Clique aqui para acessar a documentação da API</a>

# Instalação
Instale a dependência via gerenciador pip
```` commandline
pip install sdk-ifood
````

#### Exemplo prático
```` python
from ifood.exception import IfoodException
from ifood.model import Order
from ifood.service import IfoodService

try:
    ifood_service = IfoodService(
        client_id='seu client_id',
        client_secret='seu client_secret',
        grant_type='client_credentials'
    )

    # print(ifood_service.credentials.token)

    # Cada módulo deles são separados no serviço:
    """
      - financial
      - merchant
      - order
      - catalog
    """
    # Buscando os eventos de pedido da sua loja
    event_list = ifood_service.order.get_events_polling()

    for event in event_list:
        # Se o evento for igual a PLACED realize sua regra de negócio
        if event.full_code == 'PLACED':
            # Realize o request dos detalhes, pois se não o IFood não aceitará seu request de confirmação
            order: Order = ifood_service.order.get_order_details(event.order_id)

            # print(order)

            ifood_service.order.post_order_confirm(event.order_id)

        # Realizando o ack do evento
        ifood_service.order.post_events_ack(event)
except IfoodException as ifoodException:
    print(ifoodException.__str__())

````
## Em breve mais módulos e correções...
