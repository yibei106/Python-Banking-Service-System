#ChooYiBei
#TP066534

def loginuser():
    print("*****BANKING SERVICE SYSTEM*****")
    userid=input("Please Enter Your ID: ")
    password=input("Please Enter Your Password: ")
    with open("userpass.txt","r") as fh:
        foundrec = "notfound"
        for recline in fh:
            reclist=recline.strip().split(":")
            if reclist[0] ==userid and reclist[1] ==password:
                foundrec = reclist
                break
        if foundrec == "notfound":
            print("Login Failed...Please Try Again !!!!")
        else :
            print("Login Successful...")
    return foundrec


def superusermenu():
    while True:
        print("\n\n*****SUPER USER MENU******")
        print("="* 27)
        print("\n\n\t1.Add new ADMIN Staff account")
        print("\t2.Display ALL user accounts")
        print("\t3.LOGOUT from the system\n\n")
        ans = input ("Please enter your choice: ")
        if ans == "1":
            addstaff()
        elif ans == "2":
             dispaccs()
        elif ans == "3":
             break
        else:
            print("\n\t !!!!! INVALID VALUE !!!!!")


def addstaff():
    userid = genid("staff")
    userpass = userid
    print("USER ID: " + userid)
    print("USER PASSWORD: "+userpass)
    acctype= "2"
    while True:
        username=input("Enter Name: ")
        if not username.isalpha():
            print("\nAlphabets only!!!!\n\n")
        else:
            break
    with open ("userpass.txt","a") as fh:
        rec = userid+':'+userpass+':'+username.upper()+':'+acctype+'\n'
        fh.write(rec)
    print("\n\n~~~~~Account Created~~~~~")


def genid(perm):
    with open("ID.txt","r") as fh:
        rec = fh.readline()
        reclist=rec.strip().split(":")
    if perm == "staff":
        pref = "STF"
        oldid = reclist[0][3:]
    elif perm == "customer":
        pref = "CUS"
        oldid = reclist [1][3:]
    nextid = int(oldid) + 1
    if len(str(nextid)) == 1:
        newid = "0000" + str(nextid)
    elif len(str(nextid)) ==2:
        newid = "000" + str(nextid)
    elif len(str(nextid)) ==3:
        newid = "00" + str(nextid)
    elif len(str(nextid)) ==4:
        newid = "0" + str(nextid)
    elif len(str(nextid)) ==5:
        newid = str(nextid)
    newid = pref + newid
    if perm == "staff":
        reclist[0] = newid
    else:
        reclist[1] = newid
    rec = ":".join(reclist)
    with open ("ID.txt","w") as fh:
        fh.write(rec)
    return newid


def dispaccs():
    with open("userpass.txt","r") as fh:
        print("*****USER ACCOUNTS LIST*****\n")
        print("=" * 80)
        print("USER ID".center(20)+"|"+"PASSWORD".center(20)+ "|"+"USER NAME".center(20)+"|"+"ACCOUNT TYPE".center(20))
        print("=" * 80)
        for rec in fh:
            reclist = rec.strip().split(":")
            print(reclist[0].ljust(20)+"|"+reclist[1].ljust(20)+"|"+reclist[2].ljust(20)+"|"+reclist[3].ljust(20))
        print("\n\n")
    
            
            
    


def adminmenu(loginstat):
    while True:
        print("\n\n*****ADMIN STAFF MENU FOR "+loginstat[2]+"******")
        print("="* 36)
        print("\n\n\t1.Add new CUSTOMER account")
        print("\t2.Display ALL user accounts")
        print("\t3.Change Password")
        print("\t4.Change Details")
        print("\t5.Customer’s Statement of Account Report")
        print("\t6.LOGOUT from the system\n\n")
        ans = input ("Please enter your choice: ")
        if ans == "1":
            addcustomer()
        elif ans == "2":
             dispaccs()
        elif ans == "3":
             changepass(loginstat)
        elif ans == "4":
            changecusdetails()
        elif ans == "5":
            cusreport()
        elif ans == "6":
            break
        else:
            print("\n\t !!!!! INVALID VALUE !!!!!")


def addcustomer():
    userid = genid("customer")
    password = userid
    print("User ID: "+userid)
    print("Password: "+password)
    while True:
        username = input("Enter name: ")
        if not username.isalpha():
            print("\nAlphabets only!!!!\n\n")
        else:
            break
    acctype = "3"
    contact = input("Enter Contact No.: ")
    address = input("Enter Address: ")
    while True:
        ans = input("This account is for Individual(I) or Bussiness (B): ")
        if ans.upper() == "I":
            bankacc = "Savings"
            break
        elif ans.upper() == "B":
            bankacc = "Current"
            break
        else:
            print("!!! Invalid Value !!!")
    amount = float("0")
    with open("userpass.txt","a") as ufh:
        rec = userid+":"+password+":"+username.upper()+":"+acctype+"\n"
        ufh.write(rec)
    with open("customersaccount.txt","a") as cfh:
        rec = userid+":"+username.upper()+":"+contact+":"+address+":"+acctype+":"+bankacc+":"+str(amount)+"\n"
        cfh.write(rec)
    print("~~~~~Account Created~~~~~")

    
def changepass(loginstat):
    allrec = []
    with open("userpass.txt","r") as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            allrec.append(reclist)
    newpass = input("Please Enter NEW Password: ")
    ind = -1
    nor = len(allrec)
    for cnt in range(0,nor):
        if loginstat[0]== allrec[cnt][0]:
            ind = cnt
            break
    allrec[ind][1] = newpass
    with open("userpass.txt","w") as fh:
        nor = len(allrec)
        for cnt in range(0,nor):
            rec = ":".join(allrec[cnt])+"\n"
            fh.write(rec)
    print("\n!!!!! Password has been changed !!!!!")
           

def changecusdetails():
    allrec = []
    with open("customersaccount.txt","r") as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            allrec.append(reclist)
    cusid = input("Please Enter Customer's ID: ")
    print("\n\t1.Contact Number")
    print("\t2. Address")
    ans = input("Enter your choice: ")
    ind = -1
    nor = len(allrec)
    for cnt in range(0,nor):
        if cusid == allrec[cnt][0]:
            ind = cnt
    while True:
        if ans == "1":
            contact = input("Enter new contact number: ")
            allrec[ind][2] = contact
            break
        elif ans == "2":
            address = input("Enter new address: ")
            allrec[ind][3] = address
            break
        else:
            print("!!!! Invalid Value !!!!")
    with open("customersaccount.txt","w") as fh:
        nor= len(allrec)
        for cnt in range(0,nor):
            rec = ":".join(allrec[cnt])+"\n"
            fh.write(rec)
    print("\n!!! Change Succefull !!!")


    
    
def cusreport():
    with open ("customersaccount.txt","r") as fh:
        for idrec in fh:
            idreclist = idrec.strip().split(":")
            cusid = input("Please Enter Customer ID: ")
            if cusid == idreclist[0]:
                startdate = input("Please Enter Start Date(YearMonthDate, eg:20210106): ")
                enddate = input("Please Enter End Date(YearMonthDate, eg:20210106): ")
                print("\n\n==========================================================================".center(8))
                print("Customer's Statement of Account Report".center(80))
                print("==========================================================================".center(80))
                print("DESCRIPTION".center(20)+"|"+"DATE".center(20)+"|"+"AMOUNT".center(20)+"|"+"AMOUNT BALANCE".center(20))
                with open ("transaction.txt","r") as fh:
                    for rec in fh:
                        reclist = rec.strip().split("|")
                        if cusid == reclist[0]:
                            if int(reclist[3]) >= int(startdate) and int(reclist[3]) <= int(enddate):
                              print(reclist[2].center(20)+"|"+reclist[3].center(20)+"|"+reclist[4].center(20)+"|"+reclist[5].center(20))
                print("==========================================================================".center(80))
                with open("customersaccount.txt","r") as fh:
                    for crec in fh:
                        creclist = crec.strip().split(":")
                        if cusid == creclist[0]:
                            print("TOTAL AMOUNT: ".center(20)+creclist[6].rjust(55))
                            break
                print("==========================================================================".center(80)+"\n\n")
                break
            else:
                print("\n\n !!!!NON-EXISTENT ID!!!!")
                break

            
            
def customermenu(loginstat):
    while True:
        print("\n\n*****Welcome"+loginstat[2]+"*****")
        print("CUSTOMRE MENU".center(20))
        print("=" *21)
        print("\n\t1.DEPOSIT")
        print("\t2.WITHDRAWAL")
        print("\t3.Change Password")
        print("\t4.View Balance")
        print("\t5.LOGOUT FROM THE SYSTEM\n\n")
        ans = input("Please enter your choice: ")
        if ans == "1":
            transaction(loginstat,"deposit","+")
        elif ans == "2":
            withdrawal(loginstat)
        elif ans == "3":
            with open("customersaccount.txt","r") as fh:
                for rec in fh:
                    reclist = rec.strip().split(":")
                    if loginstat[0]== reclist[0] and float(reclist[6]) > 0 :
                        changepass(loginstat)
                        break
                    else:
                        print("\n!!!!! Please Do DEPOSIT first !!!!!\n\n")
        elif ans == "4":
            with open("customersaccount.txt","r") as fh:
                for rec in fh:
                    reclist = rec.strip().split(":")
                    if loginstat[0] == reclist[0]:
                        print("\n\n===============================")
                        print("Total Amount(RM): "+reclist[6]+"")
                        print("===============================\n\n")
        elif ans == "5":
            break
        else:
            print("\n\t !!!!! INVALID VALUE !!!!!")


def withdrawal(loginstat):
    with open("customersaccount.txt","r") as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            if loginstat[0] == reclist[0]:
                if reclist[5] == "Savings" and float(reclist[6]) >= 100.0:
                    transaction(loginstat,"withdrawal","-")
                elif reclist[5] == "Current" and float(reclist[6]) >= 500.0:
                    transaction(loginstat,"withdrawal","-")
                else:
                    print("\n\n!!! Not permitted.... Minumum balance must be RM100 for Savings acc or RM500 for Current acc !!!\n\n")
            
                
                
                
def transaction(loginstat,task,opt):
    allrec=[]
    with open("customersaccount.txt","r") as fh:
        for rec in fh:
            reclist = rec.strip().split(":")
            allrec.append(reclist)
            break
    if task == "deposit":
        try:
            tans = float(input("Please enter your deposit ammount: "))
        except ValueError:
            print("\n\nInvalid Value")
            customermenu(loginstat)
    elif task == "withdrawal":
        try:
            tans = float(input("Please enter your withdrawal ammount: "))
        except ValueError:
            print("\n\nInvalid Value")
            customermenu(loginstat)
    ind = -1
    nor = len(allrec)
    for cnt in range(0,nor):
        if loginstat[0] == allrec[cnt][0]:
            ind = cnt
            break
    oriamount = allrec[ind][6]
    if opt == "+":
        newtotal = float(oriamount) + tans
    elif opt == "-":
        newtotal = float(oriamount) - tans
    allrec[ind][6] = str(newtotal)
    with open("customersaccount.txt","w") as fh:
        nor = len(allrec)
        for cnt in range(0,nor):
            rec = ":".join(allrec[cnt])+"\n"
            fh.write(rec)
            break
    from datetime import datetime
    today = datetime.now()
    transdate = today.strftime("%Y%m%d")
    time = today.strftime("%H:%M:%S")
    print("=============".center(80))
    print("BANK RECEIPT".center(80))
    print("=============".center(80))
    print("\n\nUSER ID: "+ allrec[ind][0])
    print("USER NAME: "+ allrec[ind][1])
    print("\n\n"+"="*80)
    print("Transaction".center(60)+"|"+"Amount".center(20))
    print("\n"+"="*80)
    print("TOTAL AMOUNT".center(60)+"|"+ oriamount.center(20))
    print(task.center(60)+"|" + str(tans).center(20))
    print("===================".rjust(80))
    print("BALANCE".center(60) + str(newtotal).center(22))
    print("="*80)
    print("DATE: "+str(transdate)+"\nTIME: ",time)
    print("\n\n")
    with open("transaction.txt","a") as fh:
        rec = loginstat[0]+"|"+loginstat[2]+"|"+task+"|"+str(transdate)+"|"+str(tans)+"|"+str(newtotal)+"\n"
        fh.write(rec)
    
   
   
    
                
            
            
#Main_Logic
while True:
    loginstat = loginuser()
    if loginstat != "notfound":
        print("Welcome to the System "+loginstat[2])
        if loginstat[3] == "1":
            superusermenu()
        elif loginstat[3] == "2":
            adminmenu(loginstat)
        elif loginstat[3] == "3":
            customermenu(loginstat)
    else:
        print("INVALID LOGIN CREDENTIALS")
    ans = input("Press E to exit...Press ENTER to continue \n")
    if ans.upper() == 'E':
        break
        
