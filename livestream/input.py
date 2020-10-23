import boto3
from authentication import aws_authentication as auth

class create_medialive_input:

    def __init__(self, stream_key, input_name):
        self.stream_key = stream_key
        self.input_name = input_name

    def create(self):

        #get medialive authentication
        client = boto3.client('medialive', config=auth.my_config)

        # creating input
        input = client.create_input(
            Destinations=[
                {
                    'StreamName': self.stream_key,
                },
            ],
            InputSecurityGroups=[
                security_input,
            ],
            Name = self.input_name,
            Type='RTMP_PUSH',

        )

        input_id = input['Input']['Id']
        input_name = input['Input']['Name']
        input_url = input['Input']['Destinations'][0]['Url']

        return input_id, input_name, input_url
