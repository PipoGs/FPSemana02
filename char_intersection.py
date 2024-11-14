firstinput=input("first word: ")
secondinput=input("second word: ")

mix=set(firstinput) and set(secondinput)
resultmix=""


for wrd in firstinput:
    if wrd in mix and wrd not in resultmix:
        resultmix+=wrd

print(resultmix)
