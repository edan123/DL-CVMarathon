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
import multiprocessing as mp
from multiprocessing import Lock, Manager, Queue, Pool

print("【日期時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))
print("【工作目錄】{}".format(os.getcwd()))
print("【主機名稱】{} ({})".format(socket.gethostname(),socket.gethostbyname(socket.gethostname())))
print("【Python】{}".format(python_version()))


downloadPath = r"D:\R_log-2\download"


def getDatelist(start_date,end_date):
    date_list = pd.date_range(start=start_date, end=end_date)
    lst = [str(d)[:10] for d in date_list]
    lst.sort()
    return lst

def downloadFile(path, date_):
    if not os.path.exists(path) :
        os.makedirs(path)
    print('{} is donwloading...'.format(date_[:10]), end='\r')
    urlretrieve("http://cran-logs.rstudio.com/{}/{}.csv.gz".format(date_[:4], date_[:10]), 
                path + "/{}.csv.gz".format(date_[:10]))

def downloader(fname):

    #多人(download)
    global downloadPath
    path = downloadPath + '/{}/{}'.format(fname[:4], fname[5:7])
    downloadFile(path, fname)


def main():

    #單人
    fnames = getDatelist("2020-10-01","2020-12-31")

    cores = min(os.cpu_count(), len(fnames), 8)
    print("【平行運算, 啟動器核心數】{}".format(cores))

    pool = Pool(cores)   #依據核心數來啟動平行處理
    pool.map(downloader, fnames)
    pool.close()


if __name__ == "__main__":
    print("【開始時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))
    main()
    print("【結束時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))