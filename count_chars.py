userinput=str(input("write soemthing: "))

words=userinput.split(" ")

storage={}

for i in words:
    storage[i]=len(i)

print (storage)