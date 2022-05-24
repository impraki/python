a = int(input("Enter the Number"))
sam = 0
x =a 
while x!=0:
    b= x%10
    x = x//10
    if sam != 10:
        sam = sam*10
        sam = sam +b
    else:
        sam = b

if a == sam:
    print(True)
else:
    print(False)