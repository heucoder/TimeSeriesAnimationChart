#coding=utf-8
import sys
sys.path.append('..')

from TimeSeriesAnimationChart import TimeSeriesAnimationChart
from utils import FileType2

def example_bar():
    path = 'population_data.csv'
    datasets = FileType2.load_file(path)
    b = TimeSeriesAnimationChart(datasets, 'val', 'year', 'country')
    b.animation(chart_type = 'bar', title = '各国人口数目')

if __name__ == "__main__":
    example_bar()