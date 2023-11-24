from twilio.rest import Client
# getting the value of the files
account_sid="ACb237536fe88c90b40654ad223e7d0df4"
auth_token="906038d822f4b3963f55b725066df301"
twilio_number="+12146991967"
my_number="+919691268683"

client=Client(account_sid,auth_token)

# creating the message for the 

def calling():
    message=client.messages.create(
        body="accident at junction",
        to=my_number,
        from_ = twilio_number
    )
    print(message.body)

if __name__== "__main__":
    calling()