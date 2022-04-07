a=[4,5,3,8,2,4,9]
i=0
b=a[i]
while i<len(a):
	if a[i]<b:
		b=a[i]
	i+=1
print(b,"minimum")