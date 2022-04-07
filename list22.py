a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
sum=0
n=[]
while i<len(a):
	j=0
	c=[]
	while j<len(a[i]):
		sum=a[j][i]
		c.append(sum)
		j+=1
	i+=1
	n.append(c)
print(n)