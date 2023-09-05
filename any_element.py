numbers_count = int(input())
all_numbers = input().split()
print(all(int(num) > 0 for num in all_numbers) and any(num == num[::-1] for num in all_numbers))