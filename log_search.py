import re
import json

class LogSearch:
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_entries = []
        self.prs_log_file()

    def prs_log_file(self):
        '''Split file on each row, from each row create dictionery and store the dict in the list'''
        
        with open(self.log_file, errors='ignore') as file:
            for line in file:
                match = re.search(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3} \+\d{2}:\d{2})\s\[(?P<level>\w+)\]\s\{(?P<app_id>[\w-]+)\}\s\[(?P<module>.*)\]\s(?P<message>.*)", line)
                                            
                log_entry = {
                                'timestamp' : match.group('timestamp'),
                                'level'     : match.group('level'),
                                'app_id'    : match.group('app_id'),
                                'module'    : match.group('module'),
                                'message'   : match.group('message')
                            }
                
                self.log_entries.append(log_entry)
                    
                
    def search(self, key, value, limit=None):
        '''Search method for searching parameters'''
        
        filtered_log_entries = [dict for dict in self.log_entries if dict[key] == value]
        
        if filtered_log_entries:
            filtered_log_entries = filtered_log_entries[:limit]
            
            return json.dumps(filtered_log_entries, indent=4)
        
        if filtered_log_entries:
            return json.dumps(filtered_log_entries, indent=4)
        
        else:
            return "Not Found"


if __name__ == '__main__':
    
    log_search = LogSearch(r"FILE_PATH")     
    filtered = log_search.search("KEY","VALUE", 5)
    print(filtered)
