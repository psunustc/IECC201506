import os, string
from os.path import join, isfile
import csv

class input:
    def __init__(self, InputDir):
        self.filelist = self.parseInputfiles(InputDir)
    
    def parseInputfiles(self, dir):
        return sorted([ join(dir, f) for f in os.listdir(dir) if isfile(join(dir, f))])
    
    def preprocessLine(self, line):
        TranslateTable = string.maketrans('','')
        DeleteChars = string.digits + string.punctuation
        return line.translate(TranslateTable, DeleteChars)
    
    def getLine(self):
        for filename in self.filelist:
            for line in open(filename):
                yield self.preprocessLine(line)


class output:
    def __init__(self, filename, delim = ','):
        self.filename = filename
        self.delim = delim
    
    def writeline(self, line):
        with open(self.filename, "aw") as f:
            csv.writer(f, delimiter = self.delim).writerow(line)