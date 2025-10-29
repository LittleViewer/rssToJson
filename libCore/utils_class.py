import pathlib
import sys


class util :

    def check_file_exist(self, link):
        handle = pathlib.Path(link)
        return handle.exists()
    
    def stop_with_reason(self, reason):
        print("Stop Reason: " + reason)
        sys.exit(101)

    def file_open(self, link, mode = "r"):
        handle = open(link, mode)
        return handle
