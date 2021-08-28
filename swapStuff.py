def swapStuffPlease():
    file1 = input("Enter File To Modify (And Hopefully Not Eat) ")
    file2 = input("Enter Another File (Which May Or May Not Be Eaten) ")
    with open(file1, 'r') as info1:
        realInfo1 = info1.read()
    with open(file2, 'w') as info2:
        info2.write(realInfo1)
        
    with open(file2, 'r') as info3:
        realInfo3 = info3.read()
    with open(file1, 'w') as info4:
        info4.write(realInfo3)
    
swapStuffPlease()