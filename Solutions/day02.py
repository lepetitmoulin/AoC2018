###Part One###

with open('input02.txt') as f:
	count2, count3 = 0,0
	for line in f:
		hash_table = {}
		for ch in line:
			if ch in hash_table:
				hash_table[ch]+=1
			else:
				hash_table[ch]=1
		if 2 in hash_table.values():
			count2+=1
		if 3 in hash_table.values():
			count3+=1

print(count2*count3)

#solution : 7350
#solved : 2 decembre 2018
#time : 0.145s

###Part Two###

with open('input02.txt') as f:
	lst =[]
	for line in f:
		lst.append(line.strip())

def diff_by_one(s1,s2):
	'''
	s1,s2: strings of the same length
	returns: bool, whether the strings are the same except for one character in one position
	'''
	diff = 0
	i = 0
	while i<len(s1):
		if s1[i]!=s2[i]:
			diff+=1
		if diff>1:
			return False
		i+=1
	return True

def get_sames(s1,s2):
	'''
	s1,s2: strings of the same length
	returns: string of the same characters in same positions for s1 and s2
	'''
	i = 0
	s=''
	while i<len(s1):
		if s1[i]==s2[i]:
			s+=s1[i]
		i+=1
	return s

def find_diff_one(lst):
  '''
  lst: list with two or more strings
  returns: string of shared characters of two strings in the list that differ by exactly one character
  '''
	i=1
	for id in lst:
		for id2 in lst[i:]:
			if (diff_by_one(id,id2)):
				return (get_sames(id, id2))
		i+=1

print(find_diff_one(lst))

#solution : wmlnjevbfodamyiqpucrhsukg
#solved : saturday 2 decembre 2018
#time : 0.269s
