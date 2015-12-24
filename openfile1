'''
def readFile(location,date,code):
    import os 
    import datetime
    time=date.strftime("%Y%m%d")
    ym = date.strftime("%Y%m")
    rootDir = 'C:\XX\workspace\DZH-'+location+ym+'-TXT'
    if 'DZH-'+location+ym+'-TXT' not in os.listdir('C:\XX\workspace'):
        raise Exception('no such folder')
    filePath=os.listdir(rootDir)
    if time not in filePath:
        raise Except('no such file!')    
    subpath = os.path.join(rootDir,time)
    codePath = os.listdir(subpath)
    filename = code+'_'+time+'.txt'
    if filename not in codePath:
        raise Exception('no such file')
    filePath = os.path.join(subpath,filename)
    file = open(filePath).read()
    return file


import datetime
location = 'SH' 
date=datetime.date(2014, 3, 5)
code = '000001'
file = readFile(location,date,code)
print(file)
'''
def readFile(location,date,code):
    import os,datetime,zipfile 
    time=date.strftime("%Y%m%d")
    ym = date.strftime("%Y%m")
    rootDir = 'C:/XX/workspace/DZH-'+location+ym+'-TXT'
    if 'DZH-'+location+ym+'-TXT.zip'  not in os.listdir('C:/XX/workspace'):
        raise Exception('no such folder')
    filename = code+'_'+time+'.txt'
    wholepath = 'DZH-'+location+ym+'-TXT'+'/'+time+'/'+filename
    z = zipfile.ZipFile(rootDir+'.zip')
    fileList=z.namelist()
    if wholepath not in fileList:
        raise Exception('no such file')    
    file = z.read(wholepath)
    return file.decode('gbk')

import zipfile
import datetime
import os
location = 'SZ' 
date=datetime.date(2014, 2, 7)
code = '000001'

file = readFile(location,date,code)
print(file)
