# Find the average of the numbers in this list
nums = [-34, -13, 28, -34, 17, 43, -11, -25, 16, -35, 129, 30, 120, 10, 40, -5, 51, 32, 134, 36, 81, 87, 26, 49, 67, 36, 137, 29, 108, 58, 30]

# Initialize a variable to store the total sum
total = 0

# Loop through each number in the list
for num in nums:
    total += num

# Get the number of elements in the list
#count = len(nums)

# Calculate the average
average = total / len(nums)

# Print the result
print(f"{average:.3f}")
