'''
Created on Oct 22, 2019

@author: hlubyluk
'''
from sys import argv
from os import walk
from os.path import abspath, expanduser, splitext

if __name__ == '__main__':
    tif_dir_set = set()

    arg = argv[1]
    passed_arg = abspath(expanduser(arg))
    walked = walk(passed_arg, followlinks=True)
    for current, directories, files in walked:
        for f in files:
            if splitext(f)[1] == ".tif":
                tif_dir_set.add(current)

    for d in sorted(tif_dir_set):
        print(d)
