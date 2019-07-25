

# Do not use any of the built in array functions for this exercise
class array:
	def __init__(self, capacity):
		# Your code here
		self.capacity = capacity
		self.elements = [None] * capacity

# Double the size of the given array
def resize_array(array):
	new_capacity = array.capacity * 2
	new_elements = [None] * new_capacity
	array.capacity = new_capacity
for x in array:
	new_elements = [n for n in array]
	# Your code here


# Return an element of a given array at a given index
def array_read(array, index):
	# Throw an error if array is out of the current count
	# Your code here
	if not array.elements[index]:
		print("Index out of range.")
	if index >= array.capacity:
		print("Error! index " + str(index) + " out of range")
		return None
	else:
		return array.elements[index]

# Insert an element in a given array at a given index
def array_insert(array, index, value):
	# Throw an error if array is out of the current count

	# Resize the array if the number of elements is over capacity

	# Move the elements to create a space at 'index'
	# Think about where to start!

	# Add the new element to the array and update the count
	pass


# Add an element to the end of the given array
def array_append():

	# Hint, this can be done with one line of code
	# (Without using a built in function)

	# Your code here
	pass


# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove():
	# Your code here
	pass


# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
def array_pop():
	# Throw an error if array is out of the current count
	# Your code here
	pass


# Utility to print an array
def array_print(array):
	string = "["
	for i in range(array.count):
		string += str(array.elements[i])
		if i < array.count - 1:
			string += ", "

	string += "]"
	print(string)


# # Testing
# arr = array(1)

# array_insert(arr, "STRING1", 0)
# array_print(arr)
# array_pop(arr, 0)
# array_print(arr)
# array_insert(arr, "STRING1", 0)
# array_append(arr, "STRING4")
# array_insert(arr, "STRING2", 1)
# array_insert(arr, "STRING3", 2)
# array_print(arr)
