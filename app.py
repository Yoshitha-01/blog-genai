import boto3
import botocore.config
import json
from datetime import datetime
#import response
def blog_generate_using_bedrock(blogtopic:str)->str:
    prompt=f"""<s>[INST]Huma Write a 200 words blog on the topic {blogtopic}
Assistant:[/INST]
"""
    body= {
        "inputs":prompt,
        "max_new_tokens":512,
        "temperature":0.5,
        "top_p":0.9
    }

    try:
        bedrock=boto3.client("bedrock-runtime",region_name='us-east-1', 
                             config=botocore.config.Config(read_timeout=300,connect_timeout=300,retries={'max_attempts':0}))
        
        response=bedrock.invoke_model(body=json.dumps(body),modelId="meta.llama3-2-11b-instruct-v1:0")
        response_content=response.get('body').read()
        response_data=json.loads(response_content)
        print(response_data)

        blog_details=response_data['generation']
        return blog_details
    
    except Exception as e:
        print("Error is",e)
        return None
    

def save_blog_details_s3(s3_key,s3_bucket,generate_blog):
    s3=boto3.client('S3')
    try:
        s3.put_object(Key=s3_key,  Bucket=s3_bucket,Body=generate_blog)
        print("Blog details saved to S3")
    except Exception as e:
        print(e)
        return None

def lambda_handler(event, context):
    event=json.loads(event['body'])
    blogtopic=event['blog_topic']

    generate_blog=blog_generate_using_bedrock(blogtopic)

    if generate_blog:
        current_time=datetime.now().strftime('%H%M%S')
        s3_key=f"blogoutputfolder/{current_time}.txt"
        s3_bucket='aws-bedrock-course1-yoshitha'
        save_blog_details_s3(s3_key, s3_bucket, generate_blog)
    else:
        print("No blog generated")

    return {
        'statusCode':200,
        'body':json.dumps('Blog generated successfully')
    }
    


