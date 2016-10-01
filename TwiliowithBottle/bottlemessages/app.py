
from bottle import (post, request, response, route, run, )
from twilio.rest import TwilioRestClient


# copy in your Twilio Account SID and Auth Token from Twilio Console
client = TwilioRestClient("account sid", "auth token")

@route('/')
def check_app():
    # returns a simple string stating the app is working
    return "Bottle web app up and running!"


@route('/send-sms/<to_number>/<from_number>/<message_body>/')
def outbound_sms(to_number, from_number, message_body):
    # use the Twilio helper library to send an outbound SMS
    # via the REST API
    client.messages.create(to=to_number, from_=from_number,
                           body=message_body)
    # this response is sent back to the web browser client
    return "SMS sent to " + to_number


if __name__ == '__main__':
    # use the Bottle framework run function to start the development server
    run(host='127.0.0.1', port=5000, debug=True, reloader=True)
