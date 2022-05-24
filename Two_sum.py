s_list = [3,5,9,24,33,45,64,88]
tar = 42

sam=[]
for i in range(0, len(s_list)):
    x = tar-s_list[i]
    if x in sam:
        print(sam.index(x),i)
    else:
        sam.append(s_list[i])
