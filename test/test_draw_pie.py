#coding=utf-8

# plot animation
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import pandas as pd

fig, ax = plt.subplots(figsize = (15, 8))
citys = ['beijing', 'shanghai', 'tianjin', 'guangzhou']
AllColors = ['#adb0ff', '#ffb3ff', '#90d595', '#e48381']
m = ['p', '>', 'o', '*']
city2m = dict(zip(citys, m))
city2c = dict(zip(citys, AllColors))
def load_test_datasets():
    data = [['beijing', 'china', 2016, 10], ['beijing', 'china', 2017, 12], ['beijing', 'china', 2018, 14], ['beijing', 'china', 2019, 19],
            ['shanghai', 'china', 2016, 8], ['shanghai', 'china', 2017, 16], ['shanghai', 'china', 2018, 32], ['shanghai', 'china', 2019, 36],
            ['tianjin', 'china', 2016, 5], ['tianjin', 'china', 2017, 10], ['tianjin', 'china', 2018, 15], ['tianjin', 'china', 2019, 20],
            ['guangzhou', 'china', 2016, 7], ['guangzhou', 'china', 2017, 12], ['guangzhou', 'china', 2018, 24], ['guangzhou', 'china', 2019, 30]]
    datasets = pd.DataFrame(data = data,
                            columns = ['city', 'country', 'year', 'values'])
    return datasets

def draw_pie(datasets):
    df =datasets[datasets['year'].eq(2017)]
    ax.pie(x = df['values'], labels = df['city'])
    plt.show()

if __name__ == "__main__":
    datasets = load_test_datasets()
    draw_pie(datasets)