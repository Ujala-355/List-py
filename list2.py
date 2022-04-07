s_marks=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,87,9]
l_length=len(s_marks)
index=0
less_50=0
more_50=0
while index<l_length:
	marks=s_marks[index]
	if marks<50:
		less_50+=1
	else:
		more_50+=1
	index+=1
print('marks more than='+str(more_50))
print('marks more than='+str(less_50))