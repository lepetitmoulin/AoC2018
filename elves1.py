with open('input01.txt', 'r') as f:
	res = 0
	for line in f:
		num = int(line)
		res+=num
print(res)

# changes = [int(n.strip()) for n in data.split() if n.strip()]
# print(sum(changes))
#solution : 510
#solved : saturday 1 decembre 2018
#time : 0.209s