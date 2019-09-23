#coding=utf-8

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import pandas as pd

from settings import AllColors

# use class
class AnimationBarChart():

    def __init__(self, datasets, val, key, name, contents):
        self._datasets = datasets
        self._val = val
        self._key = key
        self._name = name
        self._contents = contents
        self._colors = self._colorsDict()
        self._fig, self._ax = plt.subplots(figsize = (15, 8))
        self.animator=None
    
    def _colorsDict(self):
        name_list = list(set(self._datasets[self._name].values))
        # print(name_list)
        color_list = AllColors[:len(name_list)]
        return dict(zip(name_list, color_list))

    def _drawBarChart(self, k):
        dff = self._datasets[self._datasets[self._key].eq(k)].sort_values(by=self._val, ascending=True).tail(10)
        self._ax.clear()
        self._ax.barh(dff[self._name], dff[self._val], color = [self._colors[x] for x in dff[self._name]])

        dx = dff[self._val].max() / 200  # need fixed
        for i, (value, name) in enumerate(zip(dff[self._val], dff[self._name])):
            self._ax.text(value - dx, i, name, size = 14, weight = 600, ha = 'right', va='bottom')
            self._ax.text(value - dx, i-0.25, 'c', size=10, color='#444444', ha = 'right', va = 'baseline')
            self._ax.text(value + dx, i, f'{value:,.0f}', size=14, ha = 'left', va='center')

        self._ax.text(1, 0.4, k, transform=self._ax.transAxes, color='#777777', size=46, ha='right', weight=800)
        self._ax.text(0, 1.06, "values(thousands)", transform=self._ax.transAxes, size=12, color='#777777')
        self._ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        self._ax.xaxis.set_ticks_position('top')
        self._ax.tick_params(axis='x', colors='#777777', labelsize=12)
        self._ax.set_yticks([])
        self._ax.margins(0, 0.01)
        self._ax.grid(which='major', axis='x', linestyle='-')
        self._ax.set_axisbelow(True)
        self._ax.text(0, 1.12, '2016-2019', transform = self._ax.transAxes, size = 24, weight = 600, ha='left')

        plt.box(False)  

    def animation(self):
        self.animator = animation.FuncAnimation(self._fig, self._drawBarChart, frames=range(2016,2020))
        plt.show()
    def savemovie(self):
    	self.animator.save('resetvalue.gif', writer='imagemagick')




# colors = dict(zip(['beijing', 'shanghai', 'tianjin', 'guangzhou'],
#                 ['#adb0ff', '#ffb3ff', '#90d595', '#e48381']))

# 
def load_datasets():
    data = [['beijing', 'china', 2016, 10], ['beijing', 'china', 2017, 12], ['beijing', 'china', 2018, 14], ['beijing', 'china', 2019, 19],
            ['shanghai', 'china', 2016, 8], ['shanghai', 'china', 2017, 16], ['shanghai', 'china', 2018, 32], ['shanghai', 'china', 2019, 36],
            ['tianjin', 'china', 2016, 5], ['tianjin', 'china', 2017, 10], ['tianjin', 'china', 2018, 15], ['tianjin', 'china', 2019, 20],
            ['guangzhou', 'china', 2016, 7], ['guangzhou', 'china', 2017, 12], ['guangzhou', 'china', 2018, 24], ['guangzhou', 'china', 2019, 30]]
    datasets = pd.DataFrame(data = data,
                            columns = ['city', 'country', 'year', 'values'])
    return datasets

# datasets = load_datasets()

# fig,ax = plt.subplots(figsize=(15, 8))
# def draw_barchart(year):
#     dff = datasets[datasets['year'].eq(year)].sort_values(by='values', ascending=True).tail(10)
#     ax.clear()
#     ax.barh(dff['city'], dff['values'], color = [colors[x] for x in dff['city']])
#     dx = dff['values'].max() / 200
#     for i, (value, name) in enumerate(zip(dff['values'], dff['city'])):
#         ax.text(value - dx, i, name, size = 14, weight = 600, ha = 'right', va='bottom')
#         ax.text(value - dx, i-0.25, 'china',size=10, color='#444444', ha = 'right', va = 'baseline')
#         ax.text(value + dx, i, f'{value:,.0f}', size=14, ha = 'left', va='center')
    
#     ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
#     ax.text(0, 1.06, "values(thousands)", transform=ax.transAxes, size=12, color='#777777')
#     ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
#     ax.xaxis.set_ticks_position('top')
#     ax.tick_params(axis='x', colors='#777777', labelsize=12)
#     ax.set_yticks([])
#     ax.margins(0, 0.01)
#     ax.grid(which='major', axis='x', linestyle='-')
#     ax.set_axisbelow(True)
#     ax.text(0, 1.12, '2016-2019', transform = ax.transAxes, size = 24, weight = 600, ha='left')

#     plt.box(False)

# def static_draw():
#     datasets = load_datasets()
#     # print(datasets)
#     curr_year = 2018
#     datasets = datasets[datasets['year'] == 2018]

#     colors = dict(zip(['beijing', 'shanghai', 'tianjin', 'guangzhou'],
#                     ['#adb0ff', '#ffb3ff', '#90d595', '#e48381']))
    
#     fig, ax = plt.subplots(figsize=(15, 8))
#     ax.barh(datasets['city'], 
#             datasets['values'], 
#             color = [colors[x] for x in datasets['city']])

#     for i, (value, name) in enumerate(zip(datasets['values'], datasets['city'])):
#         ax.text(value, i, name, ha = 'right')
#         ax.text(value, i-0.25, 'china', ha = 'right')
#         ax.text(value, i, value, ha = 'left')
    
#     ax.text(1, 0.4, curr_year, transform=ax.transAxes, size=46, ha='right')
#     plt.show()

if __name__ == "__main__":
    # draw_barchart(2018)
    # animator = animation.FuncAnimation(fig, draw_barchart, frames=range(2016,2020))
    # plt.show()
    datasets = load_datasets()
    b = AnimationBarChart(datasets, 'values', 'year', 'city', 'country')
    b.animation()
    b.savemovie()
