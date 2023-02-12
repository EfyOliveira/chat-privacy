# chat-privacy

# Chat privado usando a linguagem de programação Python.

Este código usa um loop while para continuar a escutar por mensagens do cliente até que sejam recebidas a mensagem "exit". Em seguida, a conexão é fechada.


Aqui está um exemplo de como você pode utilizar o script:

Abra o aplicativo Termux em seu dispositivo Android.

Execute o seguinte comando para instalar o Python:
* `pkg install python`

Execute o script com o seguinte comando:
* `python chat_privacy_server.py`

Abra outra janela do Termux e execute o seguinte comando para instalar o netcat:
* `pkg install netcat`

Caso aconteca algum erro no seu terminal ao tentar instalar o netcat use o comando abaixa:
* `pkg install netcat-openbsd`

Conecte-se ao servidor de chat com o seguinte comando:
* `nc 127.0.0.1 12345`

Envie uma mensagem ao servidor de chat e observe a resposta.

Envie a mensagem "exit" para encerrar a conexão.
