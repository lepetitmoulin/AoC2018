with open('input01.txt', 'r') as f:
	res = 0
	seen = {0:0}
	while seen[res]==0:
		for line in f:
			num = int(line)
			res+=num
			if res not in seen:
				seen[res]=0
			else:
				seen[res]+=1
				break
		f.seek(0)
	print(res)

#solution : 69074
#solved : saturday 1 decembre 2018
#time : 0.348s