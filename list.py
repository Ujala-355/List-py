s_list=[23,45,89,90,56,80]
length=len(s_list)
total_marks=0
index=0
while index<len(s_list):
	total_marks=s_list[index]+total_marks
	index+=1
print('total_marks='+str(total_marks))