#coding:utf-8

from settings import FILETYPES

def judge_file_type(filepath):    
    # assert
    assert isinstance(filepath, str)
    filetype = filepath.split(".")[-1]
    if filetype not in FILETYPES:
        return None
    return filetype

# 简单观察你的数据
def check(filepath):
    pass