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
        body=f'Olá, {key}. Funcionou esta porra!',
        from_=f'whatsapp:{number}',
        to=f'whatsapp:{value}'
        )

    print(msg.sid)


msg_sender()
