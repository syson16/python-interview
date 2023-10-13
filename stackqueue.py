# initializing list
test_list = [1, 4, 3, 6, 7]
 
# Printing original list
print("Original list is : " + str(test_list))
 
# using pop(0) to perform removal
first_element = test_list.pop(0)
 
# last_element = test_list.pop() pop last element

# Printing modified list
print("Modified list is : " + str(test_list))

test_list.append(first_element)

print(first_element)
print(test_list)
print("Hello World!")