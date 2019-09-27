#coding=utf-8
import sys
sys.path.append('..')

from DynamicSortVis import AnimationBarChart
from utils import FileType2

def example_bar():
    b = AnimationBarChart(datasets, 'val', 'year', 'country', 'states')
    b.animation(chart_type = 'bar', title = '各国人口数目')

def example_line():
    selected = ['中国', '美国', '印度']
    b = AnimationBarChart(datasets, 'val', 'year', 'country', 'states', selected=selected)
    b.animation(chart_type = 'line', title = '各国人口数目')

def example_pie():
    selected = ['中国', '美国', '印度']
    b = AnimationBarChart(datasets, 'val', 'year', 'country', 'states', selected=selected)
    b.animation(chart_type = 'pie', title = '各国人口比例')

if __name__ == "__main__":
    path = 'population_data.csv'
    datasets = FileType2.load_file(path)
    example_bar()