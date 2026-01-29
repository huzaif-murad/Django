
with open("sample.txt","w") as f:
    f.write("hi everyone\nwe are learning file I/O\n")
    f.write("using Java.\nI like programming in Java")


with open("sample.txt","r") as f:
    data = f.read()

new_data=data.replace("Java","Python")

with open("sample.txt","w") as f:
    f.write(new_data)


with open("sample.txt","r") as f:
    data=f.read()
    if(data.find("learning")!=-1):
        print("the word exist")
