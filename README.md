word count and running median program
===========================================================
The structure in the src files is

my_running_median.py ---> inout.py ---> reservoir.py--heap.py

my_word_count.py ---> inout.py

The input class transfers the input files into preprocessed lines.
The output class write each output line to the output files.

To count the word, I simply use the dictionary in Python.
To find the running median, I use the reservoir sampling to choose a set of input numbers, while the size of the set has a limit. Then I use a min heap and a max heap to strore this set of numbers. The median is determined by the two top numbers of the two heaps. The reservoir algorithm will give an approximate of the median in the case that the incoming numbers will fill up the memory.


