
def readFile(time,code):
    import os 
    rootDir = 'C:\XX\workspace\DZH-SH201404-TXT'
    filePath=os.listdir(rootDir)
    if time not in filePath:
        print('no such file!')    
    subpath = os.path.join(rootDir,time)
    codePath = os.listdir(subpath)
    filename = code+'_'+time+'.txt'
    if filename not in codePath:
        print('no such file')
    filePath = os.path.join(subpath,filename)
    f = open(filePath)
    file = f.read()
    f.close()
    return file
'''    

rootDir = 'C:\XX\workspace\DZH-SH201404-TXT'
a=os.listdir(rootDir)
time = '20140401'
code = '000001'
if time in a:
    ind = a.index(time)
else:
    print('no such file!')
path1 = os.path.join(rootDir,a[ind])
codePath = os.listdir(path1)
filename = code+'_'+time+'.txt'
print(filename)
print(path1)
filePath = os.path.join(path1,filename)
print(filePath)
f= open(filePath)
file = f.read()

#c,d=os.path.split(path1)
'''
time = '20140409'
code = '000001'
file = readFile(time,code)
print(file)