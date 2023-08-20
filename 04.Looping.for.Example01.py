# 1
#Python STRING is a sequence of characters. If within any of your
# programming applications you need to go over the characters of 
# a string individually, you can use the FOR LOOP.


word="anaconda"
for letter in word:
	print (letter)
	
# The reason why this loop works is
#  because Python considers a “string” as a sequence of characters
#  instead of looking at the string as a whole.

# 2. 
# Lists and Tuples are iterable objects. ex. list

words=["Amsterdam", "Berlin", "Copenhagen", "Dublin", "Everton", "Hamburg"]
for i in words:
	print(i)



# Ex Tuples

nums=(1,2,3,4)
sum_nums=0
for num in nums:
	sum_nums = sum_nums + num

print(f'Sum of numbers is{sum_nums}')