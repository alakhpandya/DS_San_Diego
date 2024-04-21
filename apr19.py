# Write a program that takes two numbers in the argument and print thier average.

# def avg(x, y):
#     print(f"Average of {x} & {y} is {(x + y)/2}")
#     return None
    
# avg(10, 20)
# a = float(input("a: "))     # 10
# b = float(input("b: "))     # 20
# avg(a, b)
# x = float(input("x: "))     # 10
# y = float(input("y: "))     # 20
# z = float(input("z: "))     # 30
# avg(y, z)


# Ask 4 numbers from user, call them a, b, c & d. Now find average of a & b as well as average of c & d using avg() function that takes two arguments. Finally, add both the averages and only print the final answer.

a = float(input("a: "))     # 10
b = float(input("b: "))     # 20
c = float(input("c: "))     # 30
d = float(input("d: "))     # 40

# def avg(x, y):
#     average = (x + y)/2
#     print(f"Average of {x} & {y} is {average}")
#     return average

def avg(x, y):
    return (x + y)/2

ans = avg(a, b) + avg(c, d)     # ans = None + None
print("Sum of averages =", ans)

"""
a = 2
b = 3
a! + b! = 2 + 6 = 8

c = 4
d = 5
c! + d! = 24 + 120 = 144

avg. of fact = (8 + 144)/2 = 151

e = 6
avg.of fact + 6! = 151 + 720 = 871
"""