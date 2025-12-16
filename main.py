c=1
while True:
    print("enter your problem")
    print("1  to water problem , 2 to electricity problem , 3 to road problem , 4 to sewerage problem , 0 to quit")
    userchoice=int(input("enter your problem"))

    match userchoice:
        case 1:
            bla=input("enter your name")
            sheeesh=input("enter your address")
            print("ok weee willl work on your area")
            with open("problem.txt" , "a") as f:
                f.write(f" ({c}) problem is water \nby:{bla}\naddress:{sheeesh}")
                c+=1
                f.close()
        case 2:
            bla=input("enter your name")
            sheeesh=input("enter your address")
            print("ok weee willl work on your area")
            with open("problem.txt" , "a") as f:
                f.write(f" ({c}) problem is electricity \nby:{bla}\naddress:{sheeesh}")
                c+=1
                f.close()
        case 3:
            bla=input("enter your name")
            sheeesh=input("enter your address")
            print("ok weee willl work on your area")
            with open("problem.txt" , "a") as f:
                f.write(f" ({c}) problem is road \nby:{bla}\naddress:{sheeesh}")
                c+=1
                f.close()
        case 4:
            bla=input("enter your name")
            sheeesh=input("enter your address")
            print("ok weee willl work on your area")
            with open("problem.txt" , "a") as f:
                f.write(f" ({c}) problem is sewerage \nby:{bla}\naddress:{sheeesh}")
                c+=1
                f.close()
        case 0:
            break
        case _:
            print("wrong number")
            
