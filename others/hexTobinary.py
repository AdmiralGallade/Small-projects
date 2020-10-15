print("hello world")
s = input("input a hex num(in format of 0xXXX) :  ")
h = hex(s)
l = len(h) * 4 - 8
spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=l, type='b')
print(format(s, spec))
