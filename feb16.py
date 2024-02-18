"""
1. Arithmetic Operators: +, -, *, /, %, // (floor division), ** (power)
2. Logical Operators: 
"""
# Write a program that takes days from the user and converts it into year, month & days (consider each month to be of exactly 30 days for sack of simplicity)
# Sample execution:
"""
Case-1:
Enter days: 1200
Output:
3 Years 3 Months 15 days

Case-2:
Enter days: 1100
Output:
3 Years 0 Months 5 days


days = int(input("Enter days: "))   # 1200

years = int(days / 365)
remaining_days = days % 365
months = remaining_days // 30       # same as int(remaining_days / 30) in this case
final_days = remaining_days % 30

print(f"{years} Years, {months} Months, {final_days} Days")
"""
"""
print(5 / 2)        # 2.5
print(5 // 2)       # 2
print(int(5 / 2))   # 2

print("Negative operand:")
print(-5 / 2)        # 2.5
print(-5 // 2)       # Q = -2.5 => floor(Q) = -3
print(int(-5 / 2))   # Q = -2.5 => int(Q) = -2
"""
import math

print(math.floor(3.7))
print(math.ceil(3.7))
print(round(3.7))
print("5 * 7 =", 5 * 7)
print("5 ** 7 = 5^7 =", 5 ** 7)