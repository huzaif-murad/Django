
with open("practice.txt","r") as f:
    data =f.read()
    print(data)

    num=""
    evenCount=0
    oddCount=0
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            if(int(num)%2==0):
                evenCount+=1
            else:
                oddCount+=1
            num=""
        else:
            num+=data[i]
    print("Even number : ",evenCount)
    print("Odd number : ",oddCount)


     