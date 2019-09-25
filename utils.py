#coding:utf-8
import pandas as pd
import logging
'''
support some funcs for AnimationBarChart
'''

class FileType2():
    # filetype to func
    __FILETYPES = ['csv', 'json', 'xlsx']
    __LOADFILEFUNCS = [pd.read_csv, pd.read_json, pd.read_excel]
    __FILETYPES_2_FUNCS = dict(zip(__FILETYPES, __LOADFILEFUNCS))

    def __init__(self):
        pass
    
    @classmethod
    def bind(cls, filetype, loadfileFunc):
        cls.__FILETYPES.append(filetype)
        cls.__LOADFILEFUNCS.append(loadfileFunc)
        cls.__FILETYPES_2_FUNCS[filetype] = loadfileFunc

    @classmethod
    def get(cls, filetype):
        return cls.__FILETYPES_2_FUNCS.get(filetype, None)

    @classmethod
    def judge_file_type(cls, filepath):    
        # assert
        assert isinstance(filepath, str)
        filetype = filepath.split(".")[-1]
        if filetype not in cls.__FILETYPES:
            return None
        return filetype
    
    @classmethod
    def load_file(cls, filepath, filetype = None, **kw):
        if(filetype == None):
            filetype = cls.judge_file_type(filepath)
        if(filetype == None):
            logging.error("filename error !")
            return None
        
        # need fixed
        loadfunc = cls.get(filetype)
        datasets = loadfunc(filepath, **kw)
        return datasets
        
    @classmethod
    def load_test_datasets(cls):
        data = [['beijing', 'china', 2016, 10], ['beijing', 'china', 2017, 12], ['beijing', 'china', 2018, 14], ['beijing', 'china', 2019, 19],
                ['shanghai', 'china', 2016, 8], ['shanghai', 'china', 2017, 16], ['shanghai', 'china', 2018, 32], ['shanghai', 'china', 2019, 36],
                ['tianjin', 'china', 2016, 5], ['tianjin', 'china', 2017, 10], ['tianjin', 'china', 2018, 15], ['tianjin', 'china', 2019, 20],
                ['guangzhou', 'china', 2016, 7], ['guangzhou', 'china', 2017, 12], ['guangzhou', 'china', 2018, 24], ['guangzhou', 'china', 2019, 30]]
        datasets = pd.DataFrame(data = data,
                                columns = ['city', 'country', 'year', 'values'])
        return datasets