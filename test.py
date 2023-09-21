# Python3 code to demonstrate working of
# Convert Tuple to integer
# Using int() + join() + map()

# initialize tuple
test_tuple = (2,)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Convert Tuple to integer
# Using int() + join() + map()
res = int(''.join(map(str, test_tuple)))

# printing result
print("Tuple to integer conversion : " + str(res))
