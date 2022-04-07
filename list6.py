n=[50,40,23,70,56,12,5,10,7]
maxm=0
i=0
while i<len(n):
	if n[i]>maxm:
		maxm=n[i]
	i=i+1
print(maxm)