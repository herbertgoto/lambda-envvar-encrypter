import json
import boto3
import base64
from crhelper import CfnResource

client = boto3.client('kms')
helper = CfnResource()

# For the creation event of cloudformation, this function encrypts the text using the kms key
# that are passed as arguments
@helper.create
def encrypter(event, _):
    var = event['ResourceProperties']['varToEncrypt']
    keyKms = event['ResourceProperties']['key']
    
    response = client.encrypt(KeyId=keyKms,Plaintext=str.encode(var))
    encrypted_text = base64.b64encode(response['CiphertextBlob'])
    helper.Data['var'] = str(encrypted_text,'utf-8')

#Does not execute anything on 
@helper.update
@helper.delete
def no_op(_, __):
    pass

def lambda_handler(event, context):
    helper(event, context)