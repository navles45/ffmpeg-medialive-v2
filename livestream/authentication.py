import boto3
from botocore.config import Config
# Configuration setup for AWS services


class aws_authentication:

	my_config = Config(region_name = region_name,
    	signature_version = 'v4',
   		retries = {
	        'max_attempts' : 10,
	        'mode' : 'standard'
   		 	}
    	)
