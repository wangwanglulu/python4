
print("个人财务报告（九月）")
Sept=[]
for date in range(20200901,20200931):
	Sept.append([date,0])
print()

while True:
	option=input("请问要输入几号的开销？如果结束请输入ok: ")
	if option=="ok":
		break
	else:
		day=int(option)-1
		Sept[day][1]=1
		Transportation=[]
		print("请输入每一笔的交通费开销，结束请输入ok")
		n=1
		while n!=0:
			T_expense=input("第"+str(n)+"笔:")
			if T_expense == "ok":
				n=0
			else: 
				Transportation.append(float(T_expense))
				n=n+1
			print("记录成功")
		Food=[]
		print("请输入每一笔的餐饮开销，结束请输入ok")
		m=1
		while m!=0:
			F_expense=input("第"+str(m)+"笔:")
			if F_expense == "ok":
				m=0
			else: 
				Food.append(float(F_expense))
				m=m+1
			print("记录成功")
		Sept[day].append(sum(Transportation))
		Sept[day].append(sum(Food))


Transportation_total=0
Food_total=0
for each_day in Sept:
	if each_day[1]==1:
		Transportation_total=Transportation_total+each_day[2]
		Food_total=Food_total+each_day[3]
print()
print("本月开销汇总报告")
print("交通费："+str(Transportation_total))
print("餐饮费："+str(Food_total))

print()
print("9月具体餐饮开支信息：")
for a_day in Sept:
	if a_day[1]==1:
		print("9-"+str(a_day[0]%10**2)+"  "+str(a_day[2]))








