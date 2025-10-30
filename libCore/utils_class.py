import pathlib
import sys


class util :

    def check_file_exist(self, link):
        handle = pathlib.Path(link)
        return handle.exists()
    
    def error_with_reason(self, reason, to_break = False, code = 1000):
        print("Stop Reason: " + reason)
        if to_break == True:
            sys.exit(code)

    def file_open(self, link, mode = "r"):
        handle = open(link, mode)
        return handle
    
    def order_dict(self, items_add_dict, organiser_element, dict_orderized, tick ):
        if tick == 0 :
            dict_orderized[organiser_element] = [items_add_dict]
            return dict_orderized
        
        list_key = list(dict_orderized.keys())
        if organiser_element in list_key :
            dict_orderized[organiser_element].append(items_add_dict)
        else: 
             dict_orderized[organiser_element] = [items_add_dict]
        return dict_orderized

        
        
