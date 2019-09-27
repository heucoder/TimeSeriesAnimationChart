#coding=utf-8
import sys
sys.path.append('..')

from AnimationChart import AnimationChart
from utils import FileType2

def example_bar():
    b = AnimationChart(datasets, 'val', 'year', 'country', 'states')
    b.animation(chart_type = 'bar', title = '各国人口数目')

def example_line():
    selected = ['中国', '美国', '印度']
    b = AnimationChart(datasets, 'val', 'year', 'country', 'states',)
    b.animation(chart_type = 'line', title = '各国人口数目', selected=selected)

def example_pie():
    selected = ['中国', '美国', '印度']
    b = AnimationChart(datasets, 'val', 'year', 'country', 'states')
    b.animation(chart_type = 'pie', title = '各国人口比例', selected=selected)

if __name__ == "__main__":
    path = 'population_data.csv'
    datasets = FileType2.load_file(path)
    example_bar()