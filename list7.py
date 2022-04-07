n=[50,40,23,70,56,12,5,10,7]
max=0
i=0
while i<len(n):
	if n[i]>max:
		max=n[i]
	i=i+1
j=0
max_second=0
while j<len(n):
	if n[j]>max_second:
		if n[j]<max:
			max_second=n[j]
	j+=1
s=0
max_third=0
while s<len(n):
	if n[s]>max_third:
		if n[s]<max_second:
			max_third=n[s]
	s+=1
print('maxmum',max)
print('second maxmum',max_second)
print('third maxmum',max_third)