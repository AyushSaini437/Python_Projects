# Addition of two numbers using function
# def add_num(a,b):
#     sum = a+b
#     return sum

# num1 = 55
# num2 = 25
# print("this is sum of two number is", add_num(num1,num2))

## Maximum between 3 numbers
# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))

# if a>=b and a>=c:
#     print("First number in greatest")
# elif b>=a and b>=c:
#     print("Second number in greatest")
# else:
#     print("Third number in greatest")

# Swaping of two numbers
# w = int(input("Enter first value: "))
# z = int(input("Enter second value: "))

# print("Before swaping: {}".format(w))
# print("Before swaping: {}".format(z))

# temp = w
# w = z
# z = temp
# print("After swaping: {}".format(w))
# print("After swaping: {}".format(z))

# Fibonacci sequence
     # Starting of sequence
# n = 10
# n1 = 0
# n2 = 1
# next_term = n2
# count = 1
# while count <= n:
#     print(next_term, end = " ")
#     count += 1
#     n1, n2 = n2, next_term
#     next_term = n1 + n2
# print()

# Strings
# str1 = "python"
# str2  = 'JAVATPOINT'
# str3 = '''python
#         programming'''
# print("they said, what's going on")
# print(str2[-10])
# print(str2[-1])
# print(str2[-3])
# print(str2[-2])
# print(str2[-4:-1])

# Program to reverse a string in pyhton
# def reverse(string):
#     string = string[::-1]
#     return string
# s = "Geeks"
# print(s)
# print("The reversed string(using extened slice syntax)is:", end = "")
# print(reverse(s))

# name = "my name is ayush and my age is {}"
# age = 19
# print(name.format(age))
# yello = [0,9,8,7,6,6,4]
# print(yello[:-1])
#
# st = [1,2,3,4,5,6,7]
# print(st[0])
# print(st[1])
# print(st[2])
# print(st[4])
# print(st[0:6])
# print(st[:])
# print(st[2:5])
# print(st[1:6:2])
#
# st2 = [1,2,3,4,5,6,7]
# st.extend(st2)
# print(st)
# st.insert(1,0)
# print(st)
# st.append(8)
# print(st)
# creating an empty list

# Python program to get average of a list
def avg(lst):
	return sum(lst) / len(lst)

# Driver Code
lst = [1,2,3,4,5]
average = avg(lst)

# Printing average of the list
print(f"The average of these list of numbers is: {average}")

my_list = [1, 2, 3, 5, 5, 5, 7, 8, 9, 10]
count = 0
for item in my_list:
	if(item == 5):
		count += 1
print(count)

s = input("Enter a sentence: ")

d, u, l = 0, 0, 0
# l_w = s.split()
# w =  len(l_w)
for c in s:
    if c.isdigit():
        d = d + 1
    elif c.isupper():
        u = u + 1
    elif c.islower():
        l = l + 1

# print ("No of Words: ", w)
print ("No of Digits: ", d)
print ("No of Uppercase letters: ", u)
print ("No of Lowercase letters: ", l)
