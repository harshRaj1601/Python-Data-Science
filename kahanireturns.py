kahani = ""
while True:
    data = input('enter a story --')
    if len(data)==0:
        print("end")
        break
    kahani += data + "\n"

with open("kahani.txt","a") as f:
    f.write(kahani)
