'''
 3. Count how many even numbers
  are between 1 and 100
'''

# Start a counter at 0
count = 0

# Loop through numbers from 1 to 100
for num in range(1, 101):

    # Check if the number is even
    # Even numbers have no remainder when divided by 2
    if num % 2 == 0:

        # Increase the counter by 1
        count = count + 1

# Output the total number of even numbers
print(count)