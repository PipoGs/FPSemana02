userinput=str(input(""))

words=userinput.split(" ")

storage={}

for i in words:
    storage[i]=len(i)

print (storage)
