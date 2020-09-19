for i in range(1,13):
    print("NO. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3)) # ** is exponent operator
print()

for i in range(1,13):
    print("NO. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3)) #the less than (<) will left align the formatting and the ^ will center
print()

print("Pi is approx. {0:12}".format(22/7)) #
print("Pi is approx. {0:12f}".format(22/7)) #default float value will give us 6 points after decimal
print("Pi is approx. {0:12.50f}".format(22/7)) #will give us 50 points after the decimal
print("Pi is approx. {0:52.50f}".format(22/7)) #
print("Pi is approx. {0:62.50f}".format(22/7)) #
print("Pi is approx. {0:<72.50f}".format(22/7)) #
print("Pi is approx. {0:<72.54f}".format(22/7))
print()

for i in range(1,13):
    print("NO. {:2} squared is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))