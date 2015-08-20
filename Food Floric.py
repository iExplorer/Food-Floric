def Morning():
	Item_morning=dict()
	Item_morning={1:10,2:7,3:5,4:12,5:15,6:10,7:14,8:20,9:25}
	names={1:"Coffee",2:"Tea",3:"Milk",4:"Aloo Kulcha",5:"MasalaDosa",6:"Paneer Paratha ",7:"Chapati Rolls ",8:"Paneer Sandwich ",9:"Oats with Banana"}
	amount=0
	list1=list()
	pair={"Coffee":0,"Tea":0,"Milk":0,"Aloo Kulcha":0,"MasalaDosa":0,"Paneer Paratha ":0,"Chapati Rolls ":0,"Paneer Sandwich ":0,"Oats with Banana":0}
	
	print("\n\t\t\t\tGood morning user")
	print("\nThe items available are\n")
	while True:
		print("\nItems\t\t\tAmount in Rupees")
		print("\n\n1.Coffee\t\t\t10\n2.Tea\t\t\t\t7\n3.Milk\t\t\t\t5\n4.Aloo Kulcha\t\t\t12\n5.MasalaDosa\t\t\t15\n6.Paneer Paratha \t\t10\n7.Chapati Rolls \t\t14\n8.Paneer Sandwich \t\t20\n9.Oats with Banana\t\t25\nExit\n\n")
		print("\nPlease Enter your choices user or Type 'exit' to Exit:-")
	
		try:
			choice=(input())
			err=choice.find('0')
			if choice=='0':
				print("Invalid choice")
			elif  choice=="exit" or choice=="Exit" or choice=="EXIT":	
				if amount==0:
					return
				file1=open("Amount.txt","a+")
				amount=str(amount)+"\n"
				file1.write(amount)
				file1.close()
				bill(list1,pair)
				return
			elif err!=-1:
				print("Invalid choice")	
			else:	
				length=len(choice)
				for i in range(0,length):
					index=int(choice[i])
					amount=amount+Item_morning[index]
					list1.append(names[index])
					
		except ValueError:
			print("\nInvalid choice entered\n")			
	
def Afternoon():
	Item_aft=dict()
	Item_aft={1:10,2:7,3:20,4:65,5:105}
	amount=0
	names={1:"Coffee",2:"Tea",3:"Cooldrinks",4:"Protein Shake",5:"Cheese Cake"}
	list1=list()
	pair={"Coffee":0,"Tea":0,"Cooldrinks":0,"Protein Shake":0,"Cheese Cake":0}
	
	print("\n\t\t\t\tGood Afternoon user")
	print("\nThe items available are\n")
	while True:
		print("\nItems\t\t\tAmount in Rupees")
		print("\n\n1.Coffee\t\t\t10\n2.Tea\t\t\t\t7\n3.Cooldrinks\t\t\t20\n4.Protein Shake\t\t\t65\n5.Cheese Cake\t\t       105\nExit\n\n")
		print("\nPlease Enter your choices user or Type 'exit' to Exit:-")
	
		try:
			choice=(input())
			choice=choice.replace("6","0")
			choice=choice.replace("7","0")
			choice=choice.replace("8","0")
			choice=choice.replace("9","0")
			err=choice.find('0')
			if choice=='0':
				print("Invalid choice")
			elif choice=="exit" or choice=="Exit":
				if amount==0:
					return
				file1=open("Amount.txt","a+")
				amount=str(amount)+"\n"
				file1.write(amount)
				file1.close()
				bill(list1,pair)
				return
			elif err!=-1:
				print("\nInvalid choice\n")	
			else:	
				length=len(choice)
				for i in range(0,length):
					index=int(choice[i])
					amount=amount+Item_aft[index]
					list1.append(names[index])
		except ValueError:
			print("\nInvalid choice entered\n")		
	
def Evening():
	Item_evn=dict()
	Item_evn={1:10,2:7,3:20,4:25,5:30,6:30,7:25}
	amount=0
	names={1:"Coffee",2:"Tea",3:"Cooldrinks",4:"Pizza",5:"Bhelpuri",6:"Banana Shake",7:"Panipuri"}
	list1=list()
	pair={"Coffee":0,"Tea":0,"Cooldrinks":0,"Pizza":0,"Bhelpuri":0,"Banana Shake":0,"Panipuri":0}
	
	print("\n\t\t\t\tGood Evening user")
	print("\nThe items available are\n")
	while True:
		print("\nItems\t\t\tAmount in Rupees")
		print("\n\n1.Coffee\t\t\t10\n2.Tea\t\t\t\t7\n3.Cooldrinks\t\t\t20\n4.Pizza\t\t\t\t25\n5.Bhel Puri\t\t\t30\n6.Banana Shake\t\t\t30\n7.Pani Puri\t\t\t25\nExit\n\n")
		print("\nPlease Enter your choices user or Type 'exit' to Exit:-")
	
		try:
			choice=(input())
			choice=choice.replace("8","0")
			choice=choice.replace("9","0")
			err=choice.find('0')
			if choice=='0':
				print("Invalid choice")
			elif choice=="exit" or choice=="Exit" or choice=="EXIT":
				if amount==0:
					return
				file1=open("Amount.txt","a+")
				amount=str(amount)+"\n"
				file1.write(amount)
				file1.close()
				bill(list1,pair)
				return
			elif err!=-1:
				print("Invalid choice")	
			else:	
				length=len(choice)
				for i in range(0,length):
					index=int(choice[i])
					amount=amount+Item_evn[index]
					list1.append(names[index])
		except ValueError:
			print("\nInvalid choice entered\n")					
	
def Night():
	Item_nit=dict()
	Item_nit={1:10,2:7,3:20,4:65,5:105}
	amount=0
	names={1:"Coffee",2:"Tea",3:"Cooldrinks",4:"South Indian Meal",5:"North Indian Meal"}
	list1=list()
	pair={"Coffee":0,"Tea":0,"Cooldrinks":0,"South Indian Meal":0,"North Indian Meal":0}
	
	print("\nThe items available are\n")
	while True:
		print("\nItems\t\t\tAmount in Rupees")
		print("\n\n1.Coffee\t\t\t20\n2.Tea\t\t\t\t15\n3.Cooldrinks\t\t\t20\n4.South Indian Meals\t\t65\n5.North Indian meals\t       105\nExit\n\n")
		print("\nPlease Enter your choices user or Type 'exit' to Exit:-")
	
		try:
			choice=(input())
			choice=choice.replace("6","0")
			choice=choice.replace("7","0")
			choice=choice.replace("8","0")
			choice=choice.replace("9","0")
			err=choice.find('0')
			if choice=='0':
				print("Invalid choice")
			elif choice=="EXIT" or choice=="exit" or choice=="Exit":
				if amount==0:
					return
				file1=open("Amount.txt","a+")
				amount=str(amount)+"\n"
				file1.write(amount)
				file1.close()
				bill(list1,pair)
				return
			elif err!=-1:
				print("\nInvalid choice\n")	
			else:	
				length=len(choice)
				for i in range(0,length):
					index=int(choice[i])
					amount=amount+Item_nit[index]
					list1.append(names[index])
		except ValueError:
			print("\nInvalid choice entered\n")		

def AdminLogin(count):
	import os
	username="nikhil"
	password="password"
	total=0
	count=count+1
	uname=input("\nEnter the username:")
	if uname==username:
		os.system("stty -echo")
		pw=input("\nEnter the password:")
		os.system("stty echo")
		print("\n")
		if pw==password:
			file1=open("Amount.txt","r")
			for line in file1:
				line=int(line)
				total=line+total
			grandtot=total+(total*14)/100	
			file1.close()
			file1=open("Bill.txt","r")
			print("\n\t\t\t\tAmount Vat and Net Paid is in Rs.\n")
			string="slno"+"\t\t\tAmount\t\t\tVat\t\t\tNet Paid\n"
			print(string)
			for line in file1:
				print(line,"\n")
			file1.close()
			print("\n\nTotal amount without vat=",total)	
			print("\nTotal Amount incl. of all taxes=",grandtot)
		else:
			print("\nInvalid password\n")
	else:			
		print("\nInvalid Username\n")
	return count
	
def bill(list1,pair):
	global slno
	slno=slno+1
	import time
	amount={"Coffee":10,"Tea":7,"Cooldrinks":20,"Aloo Kulcha":12,"MasalaDosa":15,"Paneer Paratha":10,"Chapati Rolls":14,"Paneer Sandwich":20,
        "Oats with Banana":25,"South Indian Meal":65,"North Indian Meal":105,"Pizza":25,"Bhelpuri":30,"Banana Shake":30,"Panipuri":25,"Protein Shake":65,"Cheese Cake":105}

	tot=0
	for i in range(0,len(list1)):
		pair[list1[i]]=pair[list1[i]]+1
	list1=set(list1)
	list1=list(list1)
	file1=open("Bill.txt","a+")
	print("\n\nYour Bill\t\t\t\t\t\tTime-",time.strftime("%I:%M:%S"),"\n\t\t\t\t\t\t\tDate-",time.strftime("%d/%m/%Y"))
	print("{0:.<26}{1:.<15}{2:.>10}".format("Item","Quantity","Amount"))
	for i in range(len(list1)):
		am=pair[list1[i]]*amount[list1[i]]
		tot=tot+am
		print("{0:.<30}{1:.<10}{2:.>10}".format(list1[i],pair[list1[i]],am))
	print("\n\n{0:-<45}{1:->5}".format("Total",tot))
	print("{0:-<45}{1:->5}".format("VAT","14%"))
	totwithvat=float(tot+(tot*14)/100)
	vatam=(tot*14/100)
	print("{0:-<45}{1:->5}".format("Net Payable",totwithvat))
	print("\t\t\t\tThank you,Please come again")
	tot=str(tot)
	totwithvat=str(totwithvat)
	vatam=str(vatam)
	slno1=str(slno)
	file1.write(slno1)
	tot="  \t\t\t"+tot
	file1.write(tot)
	vatam="   \t\t\t"+vatam
	file1.write(vatam)
	totwithvat="  \t\t\t"+totwithvat+"\n"
	file1.write(totwithvat)
	file1.close()
	return
		
def main():
	print("\n\n\t\t\t   Welcome to the Food Floric\n")
	count=0
	while True:
		if count>=3:
			print("Warning!!!!! Menu locked due to Invalid Login access\nWait for 5 sec")
			for i in range(0,5):
				print(5-i)
				time.sleep(1)
			count=0
		print("\n\n\t\t\t\t1.Morning\n\t\t\t\t2.Afternoon\n\t\t\t\t3.Evening\n\t\t\t\t4.Night\n\t\t\t\t5.AdminLogin\n\t\t\t\t6.Exit\n\n")
		print("\nPlease Enter your choice user:-")
	
		try:
			choice=int(input())
			if choice==1:
				Morning()
			elif choice==2:
				Afternoon()
			elif choice==3:
				Evening()
			elif choice==4:
				Night()
			elif choice==5:
				count=AdminLogin(count)
			elif choice==6:
				exit()	
			else:	
				print("Invalid Choice\n")				
		except ValueError:
			print("\nInvalid choice entered\n")	
			
import time
slno=0
main()	












	                        
