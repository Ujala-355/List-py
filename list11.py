list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
i=0
x=[]
while i<len(list2):
	if list1[i] not  in list2:
		x.append(list1[i])
	i=i+1
print(x)