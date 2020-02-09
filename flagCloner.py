#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join, dirname, abspath
import sys
import random

NUM_COPIES = 50
randomChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# if sys.argv[1] is None:
#     print("Usage: flagCloner <flag directory>")
#     exit(1)

path = dirname(abspath(__file__))
# path = sys.argv[1]
files = [file for file in listdir(path) if isfile(join(path, file))]

for filename in files:
    start = filename.find('_') + 1
    end = filename.find('.')
    if start < 1 or end < 0 or start > end:
        continue
    part_to_replace = filename[start:end]
    for i in range(0, NUM_COPIES):
        # generate a random replacement string
        tempFilename = ""
        for j in range(len(part_to_replace)):
            tempFilename += random.choice(randomChars)
        newFileName = filename.replace(part_to_replace, tempFilename)
        # write the new file
        open(newFileName, "w+")


