# kafka-load-producer

## O que é?
Aplicação para load tests em broker(s) do kafka.

## O que precisa?
Python 3.x (também pode utilizar a pasta `venv` deste projeto)

## Como usar
Utilize o arquivo `.env` para configurar os testes. As vars desse projeto contém as seguintes características:

| **VAR**  | Tipo | Descrição | 
| ------------ | ------------ | ------------ |
| NUMBER_OF_REQUESTS | int  | Quantidade de iterações que serão executadas (de 1 até N) |
| TOPIC | text  | Tópico que será testado |
| BROKER | text  | URL do(s) broker(s) |
| INTERVAL | decimal  | Tempo de espera entre as iterações |
| KAFKA_REQUEST_TIMEOUT_MS | int  | Tempo em milissegundos do timeout na publicação do tópico  |

Após feita essa configuração, coloque o conteúdo do payload no arquivo `payload.txt` para que seja enviado ao tópico configurado. O sistema pode enviar vários payloads em uma única iteração colocando-os em linhas individuais desse arquivo.

Este sistema depende de algumas libs que deverão ser instaladas através do comando abaixo:

`pip install -r requirements.txt`

Para executar o projeto, execute o comando abaixo:

`python3 __init__.py`