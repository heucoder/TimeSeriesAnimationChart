#coding=utf-8

# plot animation
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import pandas as pd

from IPython.display import HTML

# logging
import logging

# 
from config import AllColors
from utils import load_datasets, FileType2

'''
core class AnimationBarChart
'''

class AnimationBarChart():

    def __init__(self, val, key, name, contents = ""):
        self._datasets = None
        self._val = val
        self._key = key
        self._name = name
        self._contents = contents
        self._colors = None
        self._fig = None
        self._ax = None
        self._animator = None
    
    def _loadcolors(self):
        # need to update
        name_list = list(set(self._datasets[self._name].values))
        color_list = AllColors[:len(name_list)]
        return dict(zip(name_list, color_list))

    def _checkfile(self):
        # need fixd use try .. except ..
        assert isinstance(self._datasets, pd.DataFrame)

        columns = [self._val, self._key, self._name]
        if self._contents != '':
            columns.append(self._contents)
        try:
            df = self._datasets[columns]
        except KeyError:
            logging.error("index error")
            return -1

        # has null 
        for col in columns:
            null_num = df[col].isnull().sum()
            if null_num != 0:
                logging.warning('{} has null val'.format(col))
        return 0 

    def _loadfile(self, filepath, filetype = None, **kw):

        if(filetype == None):
            filetype = FileType2.judge_file_type(filepath)
        if(filetype == None):
            logging.error("filename error !")
            return None
        
        loadfunc = FileType2.get(filetype)
        
        datasets = loadfunc(filepath, **kw)
        return datasets

    def _drawBarChart(self, k):
        # need to update
        dff = self._datasets[self._datasets[self._key].eq(k)].sort_values(by=self._val, ascending=True).tail(10)
        self._ax.clear()
        self._ax.barh(dff[self._name], dff[self._val], color = [self._colors[x] for x in dff[self._name]])

        dx = dff[self._val].max() / 200  # need fixed
        for i, (value, name) in enumerate(zip(dff[self._val], dff[self._name])):
            self._ax.text(value - dx, i, name, size = 14, weight = 600, ha = 'right', va='bottom')
            self._ax.text(value - dx, i-0.25, 'china', size=10, color='#444444', ha = 'right', va = 'baseline')
            self._ax.text(value + dx, i, f'{value:,.0f}', size=14, ha = 'left', va='center')

        self._ax.text(1, 0.5, k, transform=self._ax.transAxes, color='#777777', size=46, ha='right', weight=800)
        self._ax.text(0, 1.05, "{}(thousands)".format(self._val), transform=self._ax.transAxes, size=12, color='#777777')
        self._ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        self._ax.xaxis.set_ticks_position('top')
        self._ax.tick_params(axis='x', colors='#777777', labelsize=12)
        self._ax.set_yticks([])
        self._ax.margins(0, 0.01)
        self._ax.grid(which='major', axis='x', linestyle='-')
        self._ax.set_axisbelow(True)
        self._ax.text(0, 1.10, '2016-2019', transform = self._ax.transAxes, size = 24, weight = 600, ha='left')

        plt.box(False)  

    def animation(self, filepath, filetype = None, saveflag = False, **kw):
        #need to update

        # load file
        self._datasets = self._loadfile(filepath, filetype, **kw)
        # check
        if self._checkfile():
            logging.error("file check error")
            return 
        # load_colors
        self._colors = self._loadcolors()
        # make animator 
        self._fig, self._ax = plt.subplots(figsize = (12, 8))
        animator = animation.FuncAnimation(self._fig, self._drawBarChart, frames=range(2016,2020), interval = 500 ,repeat = True)
        if saveflag:
            animator.save('resetvalue.gif', writer='imagemagick')
        plt.show()
        # HTML(animator.to_jshtml())

        
    # 感觉一般般,先这样把
    def bind(self, filetype, loadfileFunc):
        FileType2.bind(filetype, loadfileFunc)

if __name__ == "__main__":
    # datasets = load_datasets()

    b = AnimationBarChart('values', 'year', 'city', 'country')
    path = 'data1.csv'
    b.animation(path)