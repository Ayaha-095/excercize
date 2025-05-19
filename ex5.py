# (1)
def square(a):
    return a ** 2


print('(1)', square(2))
print('(1)', square(3))


# (2)
def mul(a=1, *args):
    ans = a
    for i in range(len(args)):
        ans = ans * args[i]
    return ans


print('(2)', mul(1, 2))
print('(2)', mul(2, 4, 6))
print('(2)', mul(3, 5, 7, 11))


# (3)
def power(a):
    return lambda x: x ** a


power3 = power(3)
power4 = power(4)

print('(3)', power3(2))
print('(3)', power4(3))

# (4)
s = 0
while True:
    try:
        num = int(input('Please input number:'))
        val = s
        s = num + s
        print(str(val)+'+'+str(num)+'=>'+str(s))
    except ValueError as ex:
        print(ex)
        print('Not a number in inputted. Program exit')
        break


