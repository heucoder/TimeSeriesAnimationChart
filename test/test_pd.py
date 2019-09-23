import pandas as pd

def func1(path, *arg, **kw):
    print(arg)
    print(kw)
    data = pd.read_csv(path, *arg, **kw)
    print(data)
    # pd.read_csv(path, index_col=)

def func2(path, *arg, **kw):
    print(arg)
    print(kw)
    data = pd.read_excel(path, *arg, **kw)
    print(data)

if __name__ == "__main__":
    # path = "../data1.csv"
    # func1(path, sep = ',')
    path = "../data1.xlsx"
    func2(path)