from flask import Flask, request
from twilio_handler import Twilio
from openai_handler import Openai

# Configurações do Flask
app = Flask(__name__)

history = []

# Rota para receber mensagens via webhook do Twilio
@app.route('/webhook', methods=['POST'])
def webhook():
    global history


    # recebe o texto e o numero do usuario do whatsapp
    incoming_msg = request.values.get('Body', '').lower()
    sender_number = request.values.get('From', '')

    history.append(incoming_msg)
    print(f"history: {history}")


    if incoming_msg:
        # Processa a mensagem de texto normalmente
        response_msg = Openai.send_message_to_openai(incoming_msg, history)
        print(f"Texto recebido. Estamos processando: {response_msg}")
        Twilio.send_message_to_whatsapp(response_msg, sender_number)
        return 'Message sent'
    else:
            print("Não foi recebido nenhuma mensagem de texto.")

if __name__ == '__main__':
    app.run(debug=True)






