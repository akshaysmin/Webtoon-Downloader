import os
from pprint import pprint

def word_as_list(word):
	s = 0
	maxlen = len(word)
	word_as_list = []
	while True:
		if s>=maxlen:
			break
		if word[s].isdigit():
			#print('isdigit')
			i = 1
			while word[s:s+i].isdigit() and s+i<=maxlen:
				i+=1
			word_as_list.append(word[s:s+i-1])
			s+=i-1
		elif word[s].isalpha():
			#print('isalpha')
			i = 1
			while word[s:s+i].isalpha() and s+i<=maxlen:
				i+=1
			word_as_list.append(word[s:s+i-1])
			s+=i-1
		else:
			#print('other')
			word_as_list.append(word[s])
			s+=1
	return word_as_list

def compare(word1,word2):
	wlist1 = word_as_list(word1)
	wlist2 = word_as_list(word2)
	#print(wlist1)
	#print(wlist2)
	if len(wlist1)<len(wlist2):
		wlists = wlist1
		wlistl = wlist2
	else:
		wlists = wlist2
		wlistl = wlist1
	i=0
	#print(wlists)
	#print(wlistl)
	while  i<len(wlists) and wlists[i]==wlistl[i]:#chooses position i where elements are different
		#print(f'wlists[{i}]=wlistl[{i}]')
		i+=1

	if i==len(wlists):
		return wlists==wlist1

	w1 = wlist1[i]
	w2 = wlist2[i]

	if w1.isdigit() and not w2.isdigit():
		return True			#i decided to go with number<non-number
	elif not w1.isdigit() and w2.isdigit():
		return False

	#now the only possibility is both are not digits or both are digits
	if w1.isdigit():
		w1 = float(w1)
		w2 = float(w2)

	if w1<w2:#means word1<word2
		return True
	else:#means word1>word2, word1==word2 not possible by definition of i
		return False

def smallest(word1,word2):
	a = compare(word1,word2)
	if a is True:
		return word1
	else: #ie, a is False(word1>word2), or a is None(word1=word2)
		return word2

def sensible_sort(wordlist):
	sorted_list = []
	bucket = wordlist[:]
	j=0
	while len(bucket)>0:
		chibi = bucket[0]
		i=0
		for word in bucket:
			chibi = smallest(chibi,word)
			i+=1
		sorted_list.append(chibi)
		bucket.remove(chibi)
		if j%50==0:
			print(f'{i} comparisons for adding {j}th element')
		j+=1
	return sorted_list

if __name__=="__main__":
	
	imgnames = [i for i in os.listdir() if i.endswith('.jpg')]
	#imgnames = ['im1s1e1_0.jpg','im10s1e10_18.jpg','im0s1e0_6.jpg','im0s1e0_1.jpg']
	#pprint(imgnames)
	
	#print('len(imgnames) = ',len(imgnames))
	
	system_sorted_imgnames = sorted(imgnames)
	sorted_imgnames = sensible_sort(imgnames)
	
	#print('len(imgnames) = ',len(imgnames))
	
	with open('sort_stats.csv','w') as f:
		f.write('before_sorting,system_sorting,my_sorting\n')
		for i,j,k in zip(imgnames,system_sorted_imgnames,sorted_imgnames):
			f.write(i+','+j+','+k+'\n')

	print('DONE :)')





