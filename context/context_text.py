# -*- coding:utf-8 -*-

import contextlib


class MyOpen(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_handler = None
        return

    def __enter__(self):
        print("enter:", self.file_name)
        self.file_handler = open(self.file_name, "r", encoding='utf-8')
        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit:", exc_type, exc_val, exc_tb)
        if self.file_handler:
            self.file_handler.close()
        return True


with MyOpen(r"C:\Users\bobo\Desktop\Learning\dict_and_set\dictcomp.py") as file_in:
    for line in file_in:
        print(line)
        # raise ZeroDivisionError

