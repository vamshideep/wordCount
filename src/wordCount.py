import os

path = './'

#Input directory
sub_dir = 'wc_input/'
file_location = path + sub_dir

#Output directory
op_dir = 'wc_output/'
op_location = path + op_dir

#Output Files
wc_result = op_location+'wc_result.txt'
med_result = op_location+'med_result.txt'

#Initializing the arrays
wordCountPerLine = []
medianCount = []
words={}
totWords ={}
totMedian = []

#List of punctuations to ignore
punc=set(",./;'?&\'\"-[]{}|_+=()!@#$%^&*0123456789")

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return float(sortedLst[index])
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

def median_count(text_data, wordFreq, punc):
    '''
    text_data - list of strings
    wordFreq  - list with frequent words to exclude
    punc      - string with punctuation to exclude
    '''
    #words={} 
    #medianCount = []
    
    for line in text_data:
        splited = line.split()
        lineCount = 0
        for ww in splited:
            lineCount = lineCount+1
            word = ww.lower()
            word = ''.join((x for x in word if x not in punc))
        
            popWords= word in wordFreq
            if popWords == False:
                if words.has_key(word):
                    words[word]=words[word]+1
                else:
                    words[word]=1
        wordCountPerLine.append(lineCount)
        medianCount.append(median(wordCountPerLine))
        #totWords= dict(totWords.items()+words.items())
        #totMedian.extend(medianCount)    
    return words,medianCount

#For each file in the directory, calculate word count and median count
for filename in os.listdir(file_location):
    #print filename
    fw1 = open(file_location+filename)
    text_data=fw1.readlines()
    k,l = median_count(text_data,"",punc)

#print k
#print l

def writeDict1(dict, filename):
    with open(filename, "a") as f:
        for key in sorted(dict):            
            f.write('%-15s %s\n' % (key,dict[key]))

#Write wordcount dictionary to a file named wc_result.txt
writeDict1(k,wc_result)

#Write median count list to a file named med_result.txt
with open(med_result, "a") as f:
    f.writelines( "%s\n" % item for item in l )