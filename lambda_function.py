from twilio.rest import Client

# Twilio Informations #
sid = ''
auth_token = ''
number = '+'


def msg_sender():
    whatsapp_client = Client(sid, auth_token)
    user = 'amanda'
    user_number = '+'

    msg = whatsapp_client.messages.create(
        body=f'Olá, {user}. Mensagem enviada através do serviço AWS Lambda',
        from_=f'whatsapp:{number}',
        to=f'whatsapp:{user_number}'
        )

    print(msg.sid)

def lambda_handler(event, context):
    msg_sender()
