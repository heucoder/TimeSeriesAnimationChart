# AnimationChart
## 什么是AnimationChart
- AnimationChart是一个用于可视化时间序列数据的python工具，其可以用柱状图、折线图、饼图三种方式直观生动的表示时间序列数据。
- 支持json\xlsx\csv三种文件格式输入，图片可以保存为gif格式

## 使用环境
- uubuntu18.04
- python3

## 如何使用
- command命令格式如下：

`python AnimationChart.py (bar | line | pie) <file_path> <val> <key> <name> [--contents=<contents>] [--bar_display_num=<bar_display_num>] [--selected=<selectd>] [--title=<title>]`

- 例如：

`python AnimationChart.py bar example/population_data.csv val year country `
![Bar](/example/各国人口数目-bar.gif)

`python AnimationChart.py line example/population_data.csv val year country --selected="中国 美国 印度" --title="population"`
![Line](/example/各国人口数目-line.gif)

`python AnimationChart.py pie example/population_data.csv val year country --selected="中国 美国 印度" --title="population"`
![Pie](/example/各国人口比例-pie.gif)

- 也可见example文件夹下的例子

## 仍需改进
- 添加更多种类的图形
- 可以保存为mp4格式