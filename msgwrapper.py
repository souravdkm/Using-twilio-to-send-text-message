
# check if twilio is working
#import twilio
#print twilio.__version__

# authorization
from twilio.rest import TwilioRestClient
ACCOUNT_SID = 'AC5d92565cxxxxxxxf06da80f4d483'
AUTH_TOKEN = '0e6f40cxxxcc6ca04xxxxxx9942'

# creating a client which will handle all operations
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

totalBreaks = 3
breakCount = 0


def alertNotifydrinkwatertextreminder():
    # twilio sending sms
    client.messages.create(to='+19799xxxxx1', from_='+1979xxxxx2x', body='Drink some water and take a break',)


def alertNotifyvoicereminder():
    # twilio calling service
    call = client.calls.create(to="+19799xxxxx1", from_="+1979xxxxx2x", url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    print call.length
    print call.sid


while(breakCount < totalBreaks):
    time.sleep(500)
    if(breakCount%2 == 0):
        alertNotifydrinkwatertextreminder()
    else:
        alertNotifyvoicereminder()
    breakCount += 1



