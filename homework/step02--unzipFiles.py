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


def unzipFile(unzipPath, fname):
    data = gzip.GzipFile(fname, 'rb').read()
    open(unzipPath + "\\" + fname.split("\\")[-1][:-3], 'wb').write(data)

def main():
    downloadPath = r"D:\R_log\download"
    unzipPath = r"D:\R_log\unzipped"

    fnames = glob.glob(downloadPath + r'\**\*.gz', recursive=True)
    for fname in fnames:
        print('{} is unzipping...'.format(fname), end='\r')
        unzipFile(unzipPath, fname)


if __name__ == "__main__":
    print("【開始時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))
    main()
    print("【結束時間】{}".format(time.strftime("%Y/%m/%d %H:%M:%S")))