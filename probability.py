# Read input
n = int(input())
letters = input().split()
k = int(input())

# Count the number of indices that contain 'a'
indices_with_a = sum(1 for letter in letters if letter == 'a')

# Calculate the probability that none of the selected indices contain 'a'
probability_no_a = 1.0
for i in range(k):
    probability_no_a *= (n - indices_with_a - i) / (n - i)

# Calculate the complementary probability
probability_at_least_one_a = 1 - probability_no_a

# Print the result with 4 decimal places
print("{:.4f}".format(probability_at_least_one_a))
