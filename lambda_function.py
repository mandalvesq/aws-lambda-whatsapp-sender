from twilio.rest import Client

# Twilio Informations #
sid = 'AC85077cda3f33094e08c1b629822db34c'
auth_token = 'c697671c0ba463b507d402619b7683c3'
number = '+14155238886'


def msg_sender():
    whatsapp_client = Client(sid, auth_token)
    user = 'amanda'
    user_number = '+5511987814764'

    msg = whatsapp_client.messages.create(
        body=f'Olá, {key}. Funcionou esta porra!',
        from_=f'whatsapp:{number}',
        to=f'whatsapp:{value}'
        )

    print(msg.sid)


msg_sender()
