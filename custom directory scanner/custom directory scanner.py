#!/usr/bin/python

import os.path
import sys
import time

#check for valid arguments, if so take in directory location
try:
    directory = sys.argv[1]
#walk through directory and subdirectories given argument
    for root, dirs, files in os.walk(directory):
        #print header for output
        print('Directory <'+os.path.join(root)+'>')
        print("%4s %1s %18s" % ('SIZE', '| LAST MODIFIED','| NAME'))
        print('-----------------------------------------')
        info = []
        for name in files:
            #store information on each files path, size, and time last modified in current directory
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            lastmod = time.ctime(os.path.getmtime(path))
            info.append([size, lastmod, name])
            #sort stored file info by size
            info.sort()
        #if file information was recorded, output it.  Else display no files message
        if len(info) == 0:
            print('NO FILES')
        else:
            for i in info:
                print("%4s %2s %9s" % (str(i[0]), str(i[1]),str(i[2])))
        print('\n')
except IndexError as e:
    print('Please enter a valid directory')
