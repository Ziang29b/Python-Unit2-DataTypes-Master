list=["TAKE", "TAKE", "SERVE", "TAKE", "CLOSE", "EOF" ]
finish = 0
notserved=0
studentlate=0
read = 0
nextnum =23
while finish == 0:
    for data in range(999):
        if data == "TAKE":
            notserved = notserved+ 1
            studentlate = studentlate +1
            nextnum = nextnum+1
        elif data == "SERVE":
            notserved = notserved - 1
        elif data == "CLOSE":
            print(f"{studentlate} {notserved} {nextnum}")
        elif data == "EOF":
            finish = 1
# print()          