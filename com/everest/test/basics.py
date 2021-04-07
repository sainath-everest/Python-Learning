# this is single line comment
"""
this is
multiline comment
"""
# conditions
a = 6
if a == 5:
    print("thiis is from if")
elif a > 5:
    print("thiis is from elif")
else:
    print("thiis is from else")

# loops
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)
    if i == 4:
        break
print("end of the loop")

for i in range(10):
    print(i, " ", end='')
print()

# input module
n = int(input("enter value"))
for i in range(2, n, 2):
    print(i)

# start pattern
rows = int(input("Enter number of rown: "))
for i in range(rows + 1):
    for j in range(i):
        print("*", end='')
    print()
