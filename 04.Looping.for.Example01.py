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

print(f'Sum of numbers is {sum_nums}')


# the for loop from line 28 wants to iterate/loop for every "num" or item
# in list () nums and what does it iterate : 
# it iterates the sum_nums which start at 0, and for every item it 
# adds num to sum_nums so e.g; sum_nums = 0 +1 = 1
# the next iteration is sum_nums= 1+2 = 3
# sum_nums = 3 + 3 = 6
# sum_nums= 6 +4
# sum_nums = 10, this is the last iteration, the for loop stops
# then print() starts with the final sum_nums, which is 10. 
# it prints 


# the next for loops is called a NESTED FOR LOOP, 
# this is when you want to loop for every item in a list, the individual
# letters of the item e.g.:

words = ["Apple", "Banana", "Car", "Dolphin" ]
for word in words: 
	# this loop fetches every word in the list and then ;
	print ("The following lines will print each letter of " +word)
	for letter in word:
		# this loop fetches every letter of a word: 
		print(letter)
	print("")	# prints a blank line



# 4 
# FOR LOOP with RANGE() function
# Range