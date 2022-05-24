sam = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}
# print(sam["M"])
inp = input("Enter Roman Value")

num = 0
j = None
for i in range(0,len(inp)):
    if i == j:
        continue
    else:
        if i <= len(inp)-2:
            if sam[inp[i]] < sam[inp[i+1]]:
                num = num + (sam[inp[i+1]] - sam[inp[i]] )
                j = i+1
            else:
                num = num + sam[inp[i]]
        else:
            num = num + sam[inp[i]]

print(num)