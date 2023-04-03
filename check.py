with open("requirements.txt","r") as f:
    r=f.readlines()
    print(r)
    r=[ i.replace("\n","") for i in r ]
    print(r)