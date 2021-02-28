# -*- coding: utf-8 -*-
from platform import python_version
import os, time, glob, pickle, socket
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import urllib
from urllib.request import urlretrieve
import wget
import gzip

print("【日期時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))
print("【工作目錄】{}".format(os.getcwd()))
print("【主機名稱】{} ({})".format(socket.gethostname(),socket.gethostbyname(socket.gethostname())))
print("【Python】{}".format(python_version()))


def getDatelist(start_date,end_date):
    return pd.date_range(start=start_date, end=end_date)

def downloadFile(path, date_):
    if not os.path.exists(path) :
        os.makedirs(path)
    print('{} is donwloading...'.format(date_[:10]), end='\r')
    urlretrieve("http://cran-logs.rstudio.com/{}/{}.csv.gz".format(date_[:4], date_[:10]), 
                path + "/{}.csv.gz".format(date_[:10]))

def main():
    date_list = getDatelist("2020-10-01","2020-12-31")
    downloadPath = r"D:\R_log\download"

    for date_ in date_list:
        path = downloadPath + '/{}/{}'.format(str(date_)[:4], str(date_)[5:7])
        downloadFile(path, str(date_))
    


if __name__ == "__main__":
    print("【開始時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))
    main()
    print("【結束時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))