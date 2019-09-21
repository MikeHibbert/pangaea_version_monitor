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
                "last_modified": arrow.get(obj.last_modified).timestamp
            }
        )   
        
    return files

def write_status_file(files):
    with open(os.path.join(settings.BASE_DIR, 'pangaea_version_monitor', 'status.one'), "w") as status_file:
        status_file.write(json.dumps(files))
        
        
        
class StatusFileNotFoundException(Exception):
    message = "Status file {} not found".format(os.path.join(settings.BASE_DIR, 'pangaea_version_monitor', 'status.one'))
    
def read_status_file():
    file_path = os.path.join(settings.BASE_DIR, 'pangaea_version_monitor', 'status.one')
    
    if os.path.exists(file_path):
        with open(os.path.join(settings.BASE_DIR, 'pangaea_version_monitor', 'status.one'), "r") as status_file:
            files = json.loads(status_file.read())
    else:
        raise StatusFileNotFoundException()
    
    return files