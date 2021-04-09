# SDK PYTHON
SDK de integração IFood em python
## Introdução
Criação de sdk com intuito de aprendizado próprio na geração de pacotes opensource

Para que você possa realizar os testes crie sua conta de desenvolvedor no novo portal do desenvolvedor do IFood

<a href="https://developer.ifood.com.br/sign-in">Clique aqui para acessar o portal do Dev do IFood</a>

# Instalação
Instale a dependência via gerenciador pip
```` commandline
    pip install sdk-ifood
````

```` python

    service = AuthenticationBaseService(client_id='{{client_id}}',
                                        client_secret='{{client_secret}}',
                                        grant_type='client_credentials')
    response = service.execute()
    token = Token.unserialize(response)

````
