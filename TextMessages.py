from twilio.rest import Client

account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)


call = client.messages.create(
    to="",
    from_="+48732168727",
    body="message"
)
