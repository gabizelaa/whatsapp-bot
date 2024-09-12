# WhatsApp Bot 📱
Este projeto é um bot para enviar e gerenciar mensagens do WhatsApp usando a API do Twilio. Ele permite enviar mensagens automáticas e registrar respostas em um banco de dados SQLite.
Com esse projeto desenvolvi habilidades como o uso de: variáveis de ambiente, bibliotecas, acesso à API do Whatsapp, banco de dados SQLite e entre outros.

## Funcionalidades 
- Envio de mensagens para números de WhatsApp usando Twilio.

- Registro de contatos que respondem positivamente em um banco de dados SQLite.

- Simulação de respostas dos usuários para testes.

## Requisitos 💻
- Python 3.x 

- Bibliotecas Python: **twilio, python-dotenv, sqlite3**

- Conta Twilio com acesso à API do WhatsApp

## Uso
1. Certifique-se de que o arquivo responses.db não existe ou está vazio. O script criará a tabela saved_contacts se não existir.

2. Execute o script no terminal: <br>
```
python bot.py
```
3. O script enviará uma mensagem inicial para os números listados e solicitará uma resposta simulada (Yes ou No) para cada número.

4. Se a resposta for Yes, o número será salvo no banco de dados SQLite. Caso contrário, o ciclo de mensagens para aquele número será encerrado.
