'''
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

li = []
num = int(input("How many numbers do you want to enter?: "))
for i in range(1,num+1):
	x1 = input("Enter the number: ")
	li.append(x1)


t = tuple(li)
print(li)
print(t)


#Simple solution
values = input()
l = values.split(",")
li = list(l)
t = tuple(l)
print(li)
print(t)


