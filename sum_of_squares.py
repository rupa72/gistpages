# Reading the number of test cases
N = int(input())

# List to hold results for all test cases
results = []

# Process each test case
for _ in range(N):
    # Read the number of integers (not really needed)
    X = int(input())
    
    # Read the space-separated integers
    integers = list(map(int, input().split()))
    
    # Calculate the sum of squares of non-negative integers
    sum_of_squares = sum(x ** 2 for x in integers if x >= 0)
    
    # Store the result
    results.append(sum_of_squares)

# Output all the results for the test cases, without any extra blank lines
for result in results:
    print(result)
