import json
import boto3
import base64

s3_client = boto3.client('s3')

def lambda_handler(event, context):
     
     print("******event********")
     print("*******************")
     print(event)
    
    
     print("******context********")
     print("*******************")
     print(context)
    
     print("*********Begin**********")
     print("*******************")
     file_content = event["body"]
     decoded_file = base64.b64decode(file_content)
     s3_upload = s3_client.put_object(Bucket="demo-2020-berguiga",Key ='image1.jpeg', Body=decoded_file)
     print("*********End**********")
     print("*******************")
    

     return {
             'statusCode': 200,
             'headers': {
                 'Content-Type': 'application/json'
             },
             'body': json.dumps({
                 'success': True
             }),
             "isBase64Encoded": False
         }
