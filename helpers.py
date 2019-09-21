import boto3
import settings
import json
import os
import arrow


def get_s3_bucket():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(settings.HARMONY_BUCKET)
    
    return bucket

def get_current_files():
    bucket = get_s3_bucket()
    
    files = []    
    for obj in bucket.objects.all():
        files.append(
            {
                "name": obj.key,
                "size": obj.size,
                "last_modified": obj.last_modified
            }
        )   
        
    return files