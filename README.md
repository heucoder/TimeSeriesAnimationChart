# TimeSeriesAnimationChart
## 什么是TimeSeriesAnimationChart
- TimeSeriesAnimationChart是一个用于可视化时间序列数据的python工具，其可以用**动态的**柱形图、折线图、饼图三种方式直观生动的表示时间序列数据

  ![柱形图](/img/bar.png)

  ![折线图](/img/line.png)

  ![饼图](/img/pie.png)

- 支持json\xlsx\csv三种文件格式输入，动态图可以保存为gif格式

## 使用环境
- uubuntu18.04
- python3

## 如何使用
1. 安装

   进入pipfile所在目录下运行

   `pipenv install`(如果安装了pipenv模块)

   或者

   `pip install requirements.txt`

2. 命令行使用

   - 命令行格式：

   `TimeSeriesAnimationChart.py (bar | line | pie) <file_path> <val> <time> <name> [--bar_display_num=<bar_display_num>] [--selected=<selectd>] [--title=<title>] [--save=<save>]` 

   - 例如：

   `python TimeSeriesAnimationChart.py bar example/population_data.csv val year country --save=true`

   ![动态的柱形图](/img/chart-bar.gif)

   - 见example文件夹

## 仍需改进
- 添加更多种类的图形
- 可以保存为mp4格式