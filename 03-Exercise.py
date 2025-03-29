'''
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''

def func(x):					#This function calculates the key and value pairs for updating the dictionary
	'''
	This is a function
	'''
	result = {}
	if x == 0:
		return 1
	for i in range(1,x+1):
		result.update({i:i*i})
	return result

dic = int(input("Enter the number for updating the Dictionary: "))
print(f'The dictionary with the keys and values upto {dic} is = {func(dic)}')


