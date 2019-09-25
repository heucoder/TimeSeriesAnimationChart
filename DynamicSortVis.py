#coding=utf-8

# plot animation
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import pandas as pd

from functools import cmp_to_key

# unused
from IPython.display import HTML

# logging
import logging

# 
from config import AllColors
from utils import FileType2

'''
core class AnimationBarChart
'''

class AnimationBarChart():

    def __init__(self, datasets, val, key, name, contents = ""):
        self._datasets = datasets
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

    def _checkdataset(self):
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
                logging.warning('{} has null val!'.format(col))
        return 0 

    def _make_frame(self, cmp = None, reverse = False):
        keys = list(set(self._datasets[self._key].values))
        keys.sort(key = cmp_to_key(cmp), reverse=reverse)
        print(keys)

        return keys

    def _drawBarChart(self, k):
        # need to update
        dff = self._datasets[self._datasets[self._key].eq(k)].sort_values(by=self._val, ascending=True).tail(self._display_num)
        self._ax.clear()
        self._ax.barh(dff[self._name], dff[self._val], color = [self._colors[x] for x in dff[self._name]])

        dx = dff[self._val].min() / 100  # need fixed
        for i, (value, name) in enumerate(zip(dff[self._val], dff[self._name])):
            self._ax.text(value - dx, i, name, size = 14, weight = 600, ha = 'right', va='bottom')
            self._ax.text(value - dx, i-0.25, 'china', size=10, color='#444444', ha = 'right', va = 'baseline')
            self._ax.text(value + dx, i, f'{value:,.0f}', size=14, ha = 'left', va='center')

        self._ax.text(1, 0.25, k, transform=self._ax.transAxes, color='#777777', size=46, ha='right', weight=800)
        self._ax.text(0, 1.05, "{}(thousands)".format(self._val), transform=self._ax.transAxes, size=12, color='#777777')
        self._ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        self._ax.xaxis.set_ticks_position('top')
        self._ax.tick_params(axis='x', colors='#777777', labelsize=12)
        # self._ax.set_yticks([])
        self._ax.margins(0, 0.01)
        self._ax.grid(which='major', axis='x', linestyle='-')
        self._ax.set_axisbelow(True)
        self._ax.text(0, 1.10, '{}-{}'.format(self._frameMin, self._frameMax), transform = self._ax.transAxes, size = 24, weight = 600, ha='left')
        plt.box(False)  

    def _drawPieChart(self, k):
        pass
    
    def _drawLineChart(self, k):
        pass

    def animation(self, chart_type = 'bar', display_num = 10, interval = 200, repeat = True, frames = None, cmp=None, reverse = False, saveflag = False):
        #need to update
        self._display_num = display_num
        # check
        if self._checkdataset():
            logging.error("file check error")
            return 
        
        # load_colors
        self._colors = self._loadcolors()

        #make frame
        if(frames == None):
            frames = self._make_frame(cmp, reverse)
        self._frameMax = frames[-1]
        self._frameMin = frames[0]
        # select chart_type
        drawFunc = None
        if chart_type == 'bar':
            drawFunc = self._drawBarChart
        if chart_type == 'pie':
            drawFunc = self._drawPieChart
        if chart_type == 'line':
            drawFunc = self._drawLineChart

        if drawFunc == None:
            logging.error("select right draw funcs")
            return 
        
        # make animator 
        self._fig, self._ax = plt.subplots(figsize = (15, 8))
        animator = animation.FuncAnimation(self._fig, drawFunc, frames=frames, interval = interval ,repeat = repeat)
        if saveflag:
            animator.save('resetvalue.gif', writer='imagemagick')
        plt.show()

# def cmp(x, y):
#     return y - x

if __name__ == "__main__":
    # datasets = load_datasets()
    path = 'data1.csv'
    datasets = FileType2.load_file(path)
    b = AnimationBarChart(datasets, 'values', 'year', 'city', 'country')
    b.animation()
