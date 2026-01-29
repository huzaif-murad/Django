
def checkLine(str):
    word=str
    data =True
    with open("sample.txt","r") as f:
        line_no=1
        while data:
            data=f.readline()
            if(word in data):
                print("word is present at line : ",line_no)
            line_no+=1
    return -1


str="learning"
checkLine(str)