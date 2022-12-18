import sys
from twilio.rest import Client

if(len(sys.argv) < 5 or len(sys.argv) > 5):
    print( "[Info] " + sys.argv[0].split("\\")[-1] + " -n [Number] -m [msg]")
    exit()

num = 0
txt = ""

for i in range(1, 5):
    if i%2 == 1:
        match sys.argv[i]:
            case "-n":
                num = sys.argv[i+1]
            case "-m":
                txt = sys.argv[i+1]

print()
print("Mobile No: {}\nMsg: \'{}\'".format(num, txt))

try:
    account_sid = "[ACC_SID]"
    auth_token = "[YOUR_AUTH_TOKEN]"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body=txt,
    from_="+12069446962",
    to=num)

    message.sid
    print("message sent successfully!")

except :
    print("[Info] Please check Your Input fields (or) Network Connection!")