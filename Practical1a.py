import datetime
name=input("Hello! Please enter your name:")
print("Hello "+name)
age=int(input("enter your age:"))
year_now = datetime.datetime.now()
#print (year_now.year)
print("you will turn 100 in " + str(int(100-age) + int(year_now.year)))
