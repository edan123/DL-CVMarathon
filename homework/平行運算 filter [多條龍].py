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
unzipPath = r"D:\R_log\unzipped"
filteredPath = r"D:\R_log-2\filtered"

packs = ['ggplot2', 'plyr', 'dplyr', 'reshape2', 'Rcpp', 
        'digest', 'stringr', 'lubridate', 'knitr', 'shiny']   #有興趣的R套件

def filter(fname):

    global filteredPath, packs
    print('{} is processing...'.format(fname), end='\r')
    df = pd.read_csv(fname, sep=",", encoding="utf-8", engine="python")
    df[df["package"].isin(packs)].to_csv(filteredPath + "\\" + fname.split("\\")[-1], index = False, sep = ",")


def main():

    global unzipPath
    fnames = glob.glob(unzipPath + r'\**\*.csv', recursive=True)
    fnames.sort()

    cores = min(os.cpu_count(), len(fnames), 2)
    print("【平行運算, 啟動器核心數】{}".format(cores))

    pool = Pool(cores)   #依據核心數來啟動平行處理
    pool.map(filter, fnames)
    pool.close()


if __name__ == "__main__":
    print("【開始時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))
    main()
    print("【結束時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))