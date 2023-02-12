# chat-privacy

# Chat privado usando a linguagem de programação Python.

Para usar o script de bate-papo para terminal Linux, você precisa ter o Python instalado em sua máquina. Aqui estão os passos para usar o script:

Execute o seguinte comando para instalar o Python & netcat:
* `pkg install python`
* `pkg install netcat`

Caso aconteca algum erro no seu terminal ao tentar instalar o netcat use o comando abaixa:
* `pkg install netcat-openbsd`

Para baixar o projeto
* `git clone https://github.com/EfyOliveira/chat_privacy_server`

Navegue até o local onde o arquivo está salvo. Execute o script com o seguinte comando:

* `cd chat_privacy_server`
* `python chat_privacy_server.py`

Siga as instruções na tela para escolher se você deseja ser o servidor ou o cliente.
Se você escolher ser o servidor, aguarde a conexão de um cliente. Se você escolher ser o cliente, digite o endereço IP do servidor ao qual deseja se conectar.
Uma vez que a conexão tenha sido estabelecida, você e seu parceiro de bate-papo poderão enviar mensagens para o outro.
