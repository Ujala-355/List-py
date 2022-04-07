l=[23,14,56,12,19,9,15,25,31,42,43]
i=0
c=0
c1=0
total_c=0
sum=0
sum1=0
while i<len(l):
	total_c+=l[i]
	if l[i]%2==0:
		sum+=l[i]
		c+=1
	if l[i]%2!=0:
		sum1+=l[i]
		c1+=1
	i+=1
print('even',c)
print('odd',c1)
print(sum)
print(sum1)
print('even sum',sum//c)
print('odd sum',sum1//c1)
print((sum+sum1)//total_c)