import json
import datetime
import libCore.utils_class as utils

class jsons_utils:

    def check_handle_exist(self, handle, message, break_ = True) :
        check_handle = self.utils_.check_file_exist(handle)
        if check_handle ==  False:
            if break_ == True:
                self.utils_.error_with_reason(message, True)
            return True

    def manage_day_dir(self):
        self.check_handle_exist(self.utils_.absolute_link("output/"), "Output dir not exist! (please create 'RSSTOJSON/output/')")
        check_handle = self.check_handle_exist(self.utils_.absolute_link(f"output/{self.day_dir_title}/"), "Output dir for day not exist!", False)
        self.utils_.create_dir(self.utils_.absolute_link(f"output/{self.day_dir_title}/"), check_handle)

    def manage_language_sub_dir(self, language):
        check_handle = self.check_handle_exist(self.utils_.absolute_link(f"output/{self.day_dir_title}/{language}"), "Output dir by language for day not exist!", False)
        self.utils_.create_dir(self.utils_.absolute_link(f"output/{self.day_dir_title}/{language}"), check_handle)

    def copy_model_json(self):
        self.check_handle_exist(self.utils_.absolute_link("configFolder/modelOutput.json"), "Model output json file not exist!")
        handle_open = self.utils_.file_open(self.utils_.absolute_link("configFolder/modelOutput.json"))
        return json.load(handle_open)

    def generate_json(self, article_pre_json, worked_json):
        tick = 0
        for one_key in worked_json[0]:
            worked_json[0][one_key] = str(article_pre_json[tick])
            tick += 1
        return worked_json

    def dump_json(self, json_to_dump, title_formated_file, language):
        check_handle = self.check_handle_exist(self.utils_.absolute_link(f"output/{self.day_dir_title}/{language}/{title_formated_file}.json"), f"This json: {title_formated_file}.json already exist!", False)
        if check_handle == True:
            handle = self.utils_.file_open(self.utils_.absolute_link(f"output/{self.day_dir_title}/{language}/{title_formated_file}.json"), "w+")
            self.count_number_article += 1
            json.dump(json_to_dump, handle, indent = 4, ensure_ascii=False)

    def pipe_output (self, feed_formated):
        model_json = self.copy_model_json()
        self.manage_day_dir()
        list_key = list(feed_formated.keys())
        for one_key in list_key:
            self.manage_language_sub_dir(one_key)
            for one_article in feed_formated[one_key]:
                good_for_dump = self.generate_json(one_article, model_json)
                title_formated_file = self.utils_.string_formated_name_file(one_article[0])
                self.dump_json(good_for_dump, title_formated_file, one_key)
        return self.count_number_article
    
    def __init__(self):
        self.count_number_article = 0
        self.utils_ = utils.utils()
        self.date = datetime.datetime.now()
        self.day_dir_title = self.utils_.string_formated_name_file(str(self.date.year)+ " "+ str(self.date.month) + " " + str(self. date.day))