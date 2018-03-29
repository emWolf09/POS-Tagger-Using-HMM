#from collection import OrderedDict 
import csv
import nltk

m = nltk.corpus.brown.tagged_words(tagset = 'universal')
tags = ["NOUN","VERB","DET","ADJ","PRON","PRT","NUM","CONJ","ADV","ADP","X","."]
states = ("NOUN","VERB","DET","ADJ","PRON","PRT","NUM","CONJ","ADV","ADP","X",".")

transition_prob_dic = {}
emission_prob_dic={}
emission_prob_list = []
for i in range(12):
	emission_prob_list.append([])

vocab=[]
with open("vocabulary.csv","rb") as csvfile3:
	spamreader3 = csv.reader(csvfile3,delimiter=" ", quotechar='"')
	for row in spamreader3:
		for t in row:
			vocab.append(t)

i=0

with open("transition_table.csv","rb") as csvfile:
	spamreader = csv.reader(csvfile,delimiter=" ", quotechar='"')
	for row in spamreader:
		x = {tags[j] : row[j]  for j in range(12)}
		#print tags[i]
		#print x
		transition_prob_dic.update({tags[i]:x})
		i=i+1

#print transition_prob_dic


i=0

with open("emission_table.csv","rb") as csvfile2:
	spamreader2 = csv.reader(csvfile2,delimiter=" ", quotechar='"')
	for row in spamreader2:
		k = 0
		for j in row:
			emission_prob_list[k].append(j)
			k = k + 1
#print emission_prob_list

m1=0
for i in emission_prob_list:
	x = {vocab[j]:i[j] for j in range(len(i))}
	# for j in range(len(i)):
	# 	x = {vocab[j]:i[j] for j in range(len(i))}
	# 	#print vocab[j]
	# 	#print i[j]
	# 	x.update({vocab[j]:i[j]})
	emission_prob_dic.update({tags[m1]:x})
	m1=m1+1

print emission_prob_dic


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
list_start_tag_prob_dic = {}
for i in range(12):
	list_start_tag_prob_dic.update({tags[i]:list_start_tag_prob[i]})



def viterbi(obs, states, start_p, trans_p, emit_p):
		V = [{}]
		path = {}
		for y in states:
			print emit_p[y][obs[0]]
			print start_p[y]
			V[0][y] = float(start_p[y]) * float(emit_p[y][obs[0]])	# Initialize base cases (t == 0)
			path[y] = [y]
		for t in range(1,len(obs)):	# Run Viterbi for t > 0
			V.append({})
			newpath = {}
			for y in states:
		
				(prob, state) = max ([  (float(V[t-1][y0]) * float(trans_p[y0][y]) * float(emit_p[y][obs[t]]), y0) for y0 in states ] )
				V[t][y] = prob
				newpath[y] = path[state] + [y]
			path = newpath	# Don't need to remember the old paths

		
		(prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
		return (prob, path[state])

s = raw_input("Eneter the string :")
tok = s.split(' ')
print tok
observations = (tok)
#observations = ("she","results","in","bad","in","morning")

x1= viterbi(observations, states, list_start_tag_prob_dic, transition_prob_dic, emission_prob_dic)
print x1[1]