#Word Count and Median Count 

This program is my submission for a coding challenge, it consists of 2 parts.

The first part of the coding challenge is to implement a word count which will count words in all the text files contained in a directory named "wc_input" and output the counts(in alphabetical order) to a file named "wc_result.txt", which is placed in a directory named "wc_output".

The second part of the coding challenge is to implement a running median for the number of words per line of text. Consider each line in a text file as a new stream of words, and find the median number of words per line, up to that point (i.e. the median for that line and all the previous lines) to a file named "med_result.txt",which is placed in a directory named "wc_output".

###How to run the code?

Download the code and run the "run.sh" script in a Linux environment. This code should run without any issues in Python2 or Python3 environments.

I have created a "run.sh" script which will automatically load the python code from the "src" directory. It will then read all text files from "wc_input" directory and then run the analysis and write the output to the files "wc_result.txt" and "med_result.txt" in "wc_output" directory

For any questions, please reach out to me.
Note: Please delete any text files within wc_input and wc_output folders before you start. This will ensure that you don't use any of my test files.

PS: I also have the same code in R Programming using text mining package, I would be happy to share that as well. 
