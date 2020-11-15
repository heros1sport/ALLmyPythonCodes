import os
import stat
import time
a = input("File name please:  ")
fileStats = os.stat(a)
Size = fileStats[stat.ST_SIZE]
LastModified = time.ctime(fileStats[stat.ST_MTIME])
LastAccessed = time.ctime(fileStats[stat.ST_ATIME])
CreationTime = time.ctime(fileStats[stat.ST_CTIME])
print('Creation time: ' + CreationTime)
print('Last accesed: ' + LastAccessed)
print('Last modified: ' + LastModified)
print('Size: ' + str(Size)+ " bytes")
input("Press Enter to Finish")

