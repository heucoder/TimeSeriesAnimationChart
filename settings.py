#coding=utf-8
import pandas as pd
AllColors = ['#adb0ff', '#ffb3ff', '#90d595', '#e48381']

FILETYPES = ['csv', 'json', 'xlsx']
FUNCS = [pd.read_csv, pd.read_json, pd.read_excel]

FILETYPES_2_FUNCS = dict(zip(FILETYPES, FUNCS))

RANGE_LIST = None