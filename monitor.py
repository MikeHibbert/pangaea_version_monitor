import time
import os
import shutil
import difflib
import subprocess
import logging
import settings
from helpers import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

   
def compare_md5_files():
    with open(os.path.join(settings.BASE_DIR, 'md5sum.txt'), 'r') as old_md5:
        old = old_md5.read()
        with open(os.path.join(settings.BASE_DIR, 'md5sum.txt.new'), 'r') as new_md5:
            new = new_md5.read()
            
            diff = difflib.unified_diff(old, new)
            
            lines = [l for l in diff]
            
            if len(lines) > 0:
                logger.debug("md5sum.txt has changed so the code must be updated")
                return False
            
    logger.debug("md5sum.txt has not changed so the code must not be updated")
    return True


def update_node():
    logger.debug("Updating node ...")
    
    stop_node()
    
    download_new_installation()
    
    start_node()

                
if __name__ == "__main__":
    get_md5_checksum()
    
    if not os.path.exists(os.path.join(settings.BASE_DIR, 'md5sum.txt')):
        shutil.copy(os.path.join(settings.BASE_DIR, 'md5sum.txt.new'), os.path.join(settings.BASE_DIR, 'md5sum.txt'))
        os.remove(os.path.join(settings.BASE_DIR, 'md5sum.txt.new'))
        
    while True:
        the_same = compare_md5_files()
        
        if not the_same:
            stop_node()
            time.sleep(10)
            
            download_new_code()
            start_node()
        
        time.sleep(settings.POLLING_FREQUENCY)
        
        get_md5_checksum()
            
        
    