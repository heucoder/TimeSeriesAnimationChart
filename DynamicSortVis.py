#coding=utf-8

# plot animation
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import pandas as pd

from matplotlib.font_manager import FontProperties
from functools import cmp_to_key

# unused
from IPython.display import HTML

# logging
import logging

# 
from config import AllColors, MARKERS, FONT_PATH
from utils import FileType2

# support Chinese
font1 = FontProperties(fname=FONT_PATH, size = 14, weight=600)
font2 = FontProperties(fname=FONT_PATH, size = 12, weight=600)
'''
core class AnimationBarChart
'''


class AnimationBarChart():

    def __init__(self, datasets, val, key, name, contents = "", selected = None):
        self._datasets = datasets
        self._val = val
        self._key = key
        self._name = name
        self._contents = contents
        self._selected = selected
        self._colors = None
        self._fig = None
        self._ax = None
        self._animator = None
    
    def _loadcolors(self):
        # need to update
        name_list = list(set(self._datasets[self._name].values))
        color_list = AllColors[:len(name_list)]
        return dict(zip(name_list, color_list))

    def _loadmarkers(self):
        name_list = list(set(self._datasets[self._name].values))
        marker_list = MARKERS[:len(name_list)]
        return dict(zip(name_list, marker_list))
    
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
        # values must float or xxx,xxx,xxx
        if isinstance(self._datasets[self._val][0], str):
            self._datasets[self._val] = self._datasets[self._val].apply(lambda x: eval(x.replace(',','')))

        return 0 

    def _make_frame(self, cmp = None, reverse = False):
        keys = list(set(self._datasets[self._key].values))
        if cmp != None:
            cmp = cmp_to_key(cmp)
        keys.sort(key = cmp, reverse=reverse)
        print(keys)
        return keys

    def _drawBarChart(self, k):
        # need to update
        dff = self._datasets[self._datasets[self._key].eq(k)].sort_values(by=self._val, ascending=True).tail(self._display_num)
        self._ax.clear()
        self._ax.barh(dff[self._name], dff[self._val], color = [self._colors[x] for x in dff[self._name]])

        dx = 0.01
        for i, (value, name) in enumerate(zip(dff[self._val], dff[self._name])):
            self._ax.text(value*(1-dx), i, name, size = 14, weight = 600, color='#242424', ha = 'right', va='bottom', fontproperties=font1)
            self._ax.text(value*(1+dx), i-0.25, '', size=10, color='#444444', ha = 'right', va = 'baseline', fontproperties=font2)
            self._ax.text(value*(1+dx), i, f'{value:,.0f}', size=14, ha = 'left', va='center')
        
        self._ax.text(1, 0.25, k, transform=self._ax.transAxes, color='#777777', size=46, ha='right', weight=800)
        self._ax.text(0, 1.05, "{}".format(self._val), transform=self._ax.transAxes, size=12, color='#777777')
        self._ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        self._ax.xaxis.set_ticks_position('top')
        self._ax.tick_params(axis='x', colors='#777777', labelsize=12)
        self._ax.set_yticks([])
        self._ax.margins(0, 0.01)
        self._ax.grid(which='major', axis='x', linestyle='-')
        self._ax.set_axisbelow(True)
        self._ax.text(0, 1.10, '{}-{}'.format(self._frameMin, self._frameMax), transform = self._ax.transAxes, size = 24, weight = 600, ha='left')
        plt.box(False)  

    def _drawPieChart(self, k):
        # 分为selected和未selected两部分
        dff = self._datasets[self._datasets[self._key].eq(k)]
        otherdff = self._otherdf[self._otherdf[self._key].eq(k)]
        dff = pd.concat([dff, otherdff], axis = 0)

        self._ax.clear()

        self._ax.pie(x = dff[self._val], labels = dff[self._name], autopct='%1.2f%%', center=(8,6), radius = 1, labeldistance = 1.1,
                    textprops=dict(fontproperties=font1))
        
        # 饼图似乎有点问题
        # plt.legend(title = '{}'.format(self._name), loc="center right", bbox_to_anchor=(1, 0, 0.5, 1))
        self._ax.set_xlabel('{}'.format(k), size = 24, color = '#777777', weight = 600)
    
    def _drawLineChart(self, k):
        dff = self._datasets[self._datasets[self._key].le(k)]
        df = dff[dff[self._key].eq(k)]
        self._ax.clear()
        for name in df[self._name]:
            item = dff[dff[self._name].eq(name)]
            self._ax.plot(item[self._key], item[self._val],c = self._colors[name], marker = self._markers[name], lw = 2.5, ms = 9, label = name)
        
        dx = 0.03
        for _, (value, key, name) in enumerate(zip(df[self._val], df[self._key], df[self._name])):
            self._ax.text(key, value*(1+dx), name, size = 10, weight=400, va='bottom', color = '#444444', fontproperties=font1)
            self._ax.text(key, value*(1+dx), f'{value:,.0f}', size = 12, weight=400, va='top', color = '#444433')           

        self._ax.grid(which = 'major', axis = 'y', color='c', linestyle='--', linewidth=1, alpha=0.3)  
        self._ax.set_xlabel('{}'.format(self._key), size = 20, color = '#777777', weight = 400)
        self._ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        self._ax.set_ylabel('{}'.format(self._val), size = 20, color = '#777777', weight = 400)
        self._ax.spines['top'].set_visible(False) # 去掉上边框
        self._ax.spines['right'].set_visible(False) # 去掉上边框
        # self._ax.legend(fontproperties=font2) # 
        
    def animation(self, chart_type = 'line', display_num = 10, interval = 200, repeat = True, frames = None, cmp=None, reverse = False, saveflag = False):
        #need to update
        self._display_num = display_num
        # check
        if self._checkdataset():
            logging.error("file check error")
            return 
        
        # load_colors, maekers
        self._colors = self._loadcolors()
        self._markers = self._loadmarkers()
        #make frame
        if(frames == None):
            frames = self._make_frame(cmp, reverse)
        self._frames = frames
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
        
        #
        if self._selected != None:
            df_tmp = self._datasets[~self._datasets[self._name].isin(self._selected)]
            df = df_tmp[self._val].groupby(df_tmp[self._key]).sum()
            self._otherdf = pd.DataFrame()

            self._otherdf['year'] = df.index
            self._otherdf['val'] = df.values
            self._otherdf['country'] = 'others'
            self._otherdf['states'] = 'others'

            self._datasets = self._datasets[self._datasets[self._name].isin(self._selected)]

        # make animator 
        self._fig, self._ax = plt.subplots(figsize = (15, 8))
        animator = animation.FuncAnimation(self._fig, drawFunc, frames=frames, interval = interval ,repeat = repeat)
        if saveflag:
            animator.save('resetvalue.gif', writer='imagemagick')
        plt.show()

if __name__ == "__main__":
    # datasets = load_datasets()
    path = 'population_data.csv'
    datasets = FileType2.load_file(path)
    selected = ['中国', '美国', '印度']
    b = AnimationBarChart(datasets, 'val', 'year', 'country', 'states', selected=selected)
    b.animation(chart_type = 'pie', display_num=5)


    # datasets['val'] = datasets['val'].apply(lambda x: eval(x.replace(',','')))
    # df = datasets['val'].groupby(datasets['year']).sum()
    # print(df.index)
    # dff = pd.DataFrame()
    # datasets['year'] = df.index
    # datasets['val'] = df.values
    # datasets['country'] = 'others'
    # datasets['states'] = 'others'
    # print(datasets.head())



    # print(type(datasets['val'][0]))
    # datasets['val'] = datasets['val'].apply(lambda x: eval(x.replace(',','')))
    # print(datasets['val'])
    # print(isinstance(int, object))