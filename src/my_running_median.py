# example of running median program
import sys, inout
import reservoir


def countWordPerLine(line):
    return len(line.split())



ins = inout.input(sys.argv[1])
outs = inout.output(sys.argv[2])
res = reservoir.reservoir()

for line in ins.getLine():
    num = countWordPerLine(line)
    outs.writeline([num, res.getRunningMedian(num)])
