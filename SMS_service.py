import requests
from twilio.rest import Client

account_sid = 'AC253934cc1acc7abc5b22adc6fbea1eff'
auth_token = 'b59a266c0c80a5e9405b8eb314b8ea83'
client = Client(account_sid, auth_token)
message = client.messages.create(
  messaging_service_sid='MGc41f0341ba72658184e36ef50be77457',
  body='TEST MESSAGE FROM PYTHON',
  from_='+18159498288',
  to='+61420226498'
)
print(message.status)