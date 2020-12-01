def swapdata():
    file1name=input("enter the name of 1st file")
    file1=open(file1name,"r")
    print(file1.read()+"\n\n This is the text in the file")
    wantappend=input("Do you want to append text in this file")
    if(wantappend=="yes"):
        texta1=input("Enter text you want to append")
        file1=open(file1name,"a")
        file1.write(texta1)

    file2name = input("enter the name of 2st file")
    file2 = open(file2name, "r")
    print(file2.read() + "\n\n This is the text in the file")
    wantappend = input("Do you want to append text in this file")
    if (wantappend == "yes"):
        texta2 = input("Enter text you want to append")
        file2 = open(file2name, "a")
        file2.write(texta2)
    wavicever= input("Wants to viceversa the text of both files")
    if(wavicever=="yes"):
        file1=open(file1name,"r")
        file2=open(file2name, "r")
        txtfile1=file1.read()
        txtfile2=file2.read()
        file1 = open(file1name, "w")
        file2 = open(file2name, "w")
        file1.write(txtfile2)
        file2.write(txtfile1)
        print("Text viceversa successfull")

swapdata()