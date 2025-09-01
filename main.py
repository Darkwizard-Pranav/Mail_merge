r=open("Input/starting_letter.txt","r")
invi=open("Input/invited_names.txt")
name=(invi.readlines())
print(name)
k=r.read()
for i in range(0,len(name)):
    n=name[i]
    n=n.strip()
    writ=open(f"Output/{n}.txt","a")
    j=k.replace("[name]",n)
    writ.write(j)
