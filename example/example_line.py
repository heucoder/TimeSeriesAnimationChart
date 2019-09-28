import sys
sys.path.append('..')

from TimeSeriesAnimationChart import TimeSeriesAnimationChart
from utils import FileType2

def example_line():
    path = 'population_data.csv'
    datasets = FileType2.load_file(path)
    selected = ['中国', '美国', '印度']
    b = TimeSeriesAnimationChart(datasets, 'val', 'year', 'country')
    b.animation(chart_type = 'line', title = '各国人口数目', selected=selected)

if __name__ == "__main__":
    example_line()