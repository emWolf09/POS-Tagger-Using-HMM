import nltk
import csv

def count1(tag):
    """ This function counts the number of occurance of a given tag in  corpus"""
    count = 0
    for i in m:
        if i[1] == tag:
            count = count + 1
    return count

def count2(tag1,tag2):
    """This function counts the number of occurance of a given bigram in  corpus"""
    count = 0
    isfirst = 1
    for i in m:
        if isfirst != 1 :
            if prev[1] == tag1 and i[1] == tag2 :
                count = count+1
        else:
            isfirst = 0
        prev = i
    return count

def count3(word,tag):
    """This function counts the number of occurance of a word with particular tag"""
    count = 0
    #isfirst = 1
    for i in m:
        if i[1] == tag and i[0] == word :
            count = count+1      
    return count

def transition_prob():
    """This function calculates and fills transition table"""
    for i in range(12):
        for j in range(12):
            print j
            tag1 = tags[i]
            tag2 = tags[j]
            x = count1(tag2)
            y = count2(tag2,tag1)
            transition_table[i].append(float(y)/float(x))
        writer.writerow(transition_table[i])
    return

def emission_prob():
    """This function calculates and fills emission table"""
    for i in range(vocab_count):
        for j in range(12):
            print j
            tag = tags[j]
            x = count_tag[j]
            y = count3(vocab[i],tag)
            emission_table[i].append(float(y)/float(x))
        writer1.writerow(emission_table[i])
    for i in range(12):
        for j in range(vocab_count):
            emission_table[j][i] = 0

    print "Initialization complete"

    for i in m:
        x = vocab.index(i[0])
        y = tags.index(i[1])
        emission_table[x][y] = emission_table[x][y]  + 1

    print"vocab table partial"

    for i in range(12):
        for j in range(vocab_count):
            emission_table[j][i] = float(emission_table[j][i])/float(count_tag[i])

    return



m = nltk.corpus.brown.tagged_words(tagset = 'universal')

tags = ["NOUN","VERB","DET","ADJ","PRON","PRT","NUM","CONJ","ADV","ADP","X","."]


transition_table[][]
transition_table = []
for i in range(12):
    transition_table.append([])

#emission_table[][]
vocab = []
vocab_count = 0
for i in m :
    if i[0] not in vocab:
        vocab.append(i[0])
        vocab_count = vocab_count + 1



print "asdasd"

emission_table = []
for i in range(vocab_count):
    emission_table.append([0,0,0,0,0,0,0,0,0,0,0,0])

count_tag = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in m:
    c = tags.index(i[1])
    count_tag[c] = count_tag[c] + 1

print "count finish"


bigrams = nltk.bigrams(m)

file_out = open("transition_table.csv","wb")
writer = csv.writer(file_out, delimiter=" ", quotechar='"', quoting=csv.QUOTE_ALL)

file_out1 = open("emission_table.csv","wb")
writer1 = csv.writer(file_out1, delimiter=" ", quotechar='"', quoting=csv.QUOTE_ALL)

file_out2 = open("vocabulary.csv","wb")
writer2 = csv.writer(file_out2, delimiter=" ", quotechar='"', quoting=csv.QUOTE_ALL)

writer2.writerow(vocab)
transition_prob()
emission_prob()
for l in emission_table:
   writer1.writerow(l)
print transition_table
print emission_table

print vocab_count

#calculating start tag probability

list_start_tag=[]
list_start_tag_prob=[]


flag1=0
def start_tag():
    flag = 0
    for i in m:
        if flag!=1:
            #something
            flag =1
            list_start_tag.append(i[1])
        elif prev[0]=="." :
            list_start_tag.append(i[1])
        prev = i

    l = len(list_start_tag)
    for i in tags:
        n = float(list_start_tag.count(i))/float(l)
        list_start_tag_prob.append(n)

print "done start tag"

start_tag()
print list_start_tag_prob
