# example of word_count program
import sys, inout
import operator

def wordcount(dirname, filename):
    ins = inout.input(dirname)
    outs = inout.output(filename, '\t')
    
    wordcount={}
    for line in ins.getLine():
        for word in line.split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    
    wordcount = sorted(wordcount.items(),
                       key = operator.itemgetter(1),
                       reverse = True)
    for (key,value) in wordcount:
        outs.writeline([key, value])



wc(sys.argv[1], sys.argv[2])