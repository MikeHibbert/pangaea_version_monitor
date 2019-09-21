import time
import settings
from helpers import *
   
def compare_files(current_files, new_files):
    changed_files = []
    added_files = []
    
    for new_file in new_files:
        not_found = True        
        for current_file in current_files:
        
            if current_file['name'] == new_file['name']:
                not_found = False
                if current_file['last_modified'] != new_file['last_modified']:
                    changed_files.append(new_file)
                    
        if not_found:
            added_files.append(new_file)
            
    return changed_files, added_files

                
if __name__ == "__main__":
    try:
        current_status_files = read_status_file()
    except StatusFileNotFoundException:
        current_status_files = get_current_files()        
        write_status_file(current_status_files)
        
    while True:
        new_status_files = get_current_files()
        
        changed, added = compare_files(current_status_files, new_status_files)
        
        if len(changed) > 0:
            process_changed(changed)
            
        time.sleep(settings.POLLING_FREQUENCY)
        
    