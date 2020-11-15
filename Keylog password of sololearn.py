from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory, PNOperationType
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'sub-c-816d3006-ece3-11ea-a728-4ec3aefbf636'
pnconfig.publish_key = 'pub-c-296527a6-0830-4283-bc36-fb341a33917f'
pnconfig.uuid = 'myUniqueUUID'
pubnub = PubNub(pnconfig)


def my_publish_callback(envelope, status):
    
    if not status.is_error():
        pass
    else:
        print("YAY")


class MySubscribeCallback( SubscribeCallback ):
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data

    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            print("oof")  # This event happens when radio / connectivity is lost

        elif status.category == PNStatusCategory.PNConnectedCategory:
            print("conn")
            
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            print("donn")
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.
    def message(self, pubnub, message):
        # Handle new message stored in message.message
        print(message.message['such'])

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('MultiplayerGame').execute()

while True:
    pass
