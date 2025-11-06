import json
import datetime
import os
import libCore.utils_class as utils

class jsons_utils:


    def pipe_output (self, feed_formated):
        list_key = list(feed_formated.keys())
        check_handle = self.utils_.check_file_exist("output/")
        if check_handle ==  False:
            self.utils_.error_with_reason("Output dir not exist!", True)
        date = datetime.datetime.now()
        day_dir_title = self.utils_.string_formated_name_file(str(date.year)+ " "+ str(date.month) + " " + str(date.day))
        check_handle = self.utils_.check_file_exist(f"output/{day_dir_title}/")
        print(check_handle)
        if check_handle == False:
            os.mkdir(f"output/{day_dir_title}/")
        for one_key in list_key:
            print(one_key)
        title_formated = self.utils_.string_formated_name_file("test,cest.oe;zpozs!")
        return title_formated

    def __init__(self):
        self.utils_ = utils.utils()