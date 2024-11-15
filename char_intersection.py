
input1=input(str())
input2=input(str())

c = set(input1).intersection(set(input2))

s = "".join(c)
print(s)