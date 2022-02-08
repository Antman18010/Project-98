def swapFileData():
    file1=input("Enter the name of the first file.")
    file2=input("Enter the name of the second file.")
    f1=open(file1,"r")
    data_a=f1.read()
    f2=open(file2,"r")
    data_b=f2.read()
    f1w=open(file1,"w")
    f1w.write(data_b)
    f2w=open(file2,"w")
    f2w.write(data_a)
    print("The data of the files has been swapped.")

swapFileData()