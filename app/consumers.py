import json
from channels.generic.websocket import WebsocketConsumer

class YourConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        checking_message = {
            'message': 'Magandang Pasko sa inyu!'
            }
        self.send(text_data=json.dumps(checking_message))

    def receive(self, text_data):
        try:
            
            text_data_json = json.loads(text_data)
            """
                text_data_json = {
                    'action': 'location',
                    ...
                }
            """
            
            data_action = text_data.get('action' , None)
            
            if data_action == 'location':
                lat = text_data_json.get('lat' , None)
                long = text_data_json.get('long' , None)
                if lat and long:
                    # TODO: Check if the user is near on the tree
                    pass
            
            
            
        except Exception as e:
            # TODO: Log the error
            self.send(text_data=json.dumps({'error': str(e)}))
            print(e)
        
        

    def disconnect(self, close_code):
        pass
