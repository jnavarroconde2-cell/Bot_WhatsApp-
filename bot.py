from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def bot():
    mensaje = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    if 'hola' in mensaje:
        msg.body('Hola bro! Soy tu bot 🤖 activo desde GitHub')
    else:
        msg.body(f'Recibí: {mensaje}')
    
    return str(resp)

if __name__ == "__main__":
    app.run()
