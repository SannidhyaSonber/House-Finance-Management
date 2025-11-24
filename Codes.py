 #system settings & creadentials


def newuser():
    time.sleep(1.5)
    print('\nGet started\n\tCreate new account  .  ')
    time.sleep(1.5)
    username = str(input('Enter new username \t:\t'))
    time.sleep(1.5)
    try:
        f = open('Data Base\\'+username + ' credential.txt','r')
        r = f.readlines()
        time.sleep(1.5)
        print('This user name already exist ! ! ! ! \Try another')            
        f.close()
    except IOError :
        create_password(username)
        nexperma(username)
        newtemp(username)
    balance(username)
    return username

    
def create_password(username):
    #from getpass import getpass
    time.sleep(1.5)
    print('\tCreate Password\nMinimum length of password is 4')
    time.sleep(1.5)
    pwd1 = str(input('Enter New Password\t:\t'))
    time.sleep(1.5)
    x = len(pwd1)
    while x < 4 :
        print('Minimum length of password is 4')
        time.sleep(1.5)
        pwd1 = str(input('Enter New Password\t:\t'))
        time.sleep(1.5)
        x = len(pwd1)
    pwd2 = str(input('Conform Password           \t:\t'))
    time.sleep(1.5)
    while pwd1!=pwd2:
        print('Password entered don',"'",'t match')
        time.sleep(1.5)
        pwd1 = str(input('Enter New Password\t:\t'))
        time.sleep(1.5)
        x = len(pwd1)
        while x < 4 :
            print('Minimum length of password is 4')
            time.sleep(1.5)
            pwd1 = str(input('EnterPassword\t:\t'))
            time.sleep(1.5)
            x = len(pwd1)
        pwd2 = str(input('Conform Password           \t:\t'))
        time.sleep(1.5)
    print('Password created sucessfully   #\n\n')
    time.sleep(1.5)
    data = open('Data Base\\'+username + ' credential.txt','w')
    data.write(str(pwd1))
    data.close()


def password() :
    time.sleep(1.5)
    username = str(input('Enter username\t\t:\t'))
    time.sleep(1.5)
    x = False
    while x != True:
        try:
            file = open('Data Base\\'+username + ' credential.txt','r')
            pwd1 = file.readline()
            if pwd1 == '' :
                create_password(username)
                file = open('Data Base\\'+username + ' credential.txt','r')
                pwd1 = file.readline()
            pwd2 = input('Enter your password\t:\t ')
            time.sleep(1.5)
            while pwd1!=pwd2:
                print('\n\n\t\tExcess Denied>>>\n\n')
                time.sleep(1.5)
                pwd2 = str(input('Re-enter Password   :    '))
                time.sleep(1.5)
            print('\n\t\tLogged in sucessfully>>> \n')
            time.sleep(1.5)
            x = True
            file.close()
        except IOError:
            print('Username not found')
            time.sleep(1.5)
            choice = input('Enter (yes) to create new account\t:\t')
            time.sleep(1.5)
            if choice == 'yes' or choice == 'Yes' or choice == 'y' :
                newuser()
                x = True
            else :
                time.sleep(1.5)
                username = str(input('Re-enter username\t\t:\t'))
    return username

def change_password(username) :
    time.sleep(1.5)
    c = input('Press (yes) to change password | Press (no) to return\t:\t')
    if c == 'yes' or choice == 'Yes' or choice == 'y'  :
        password()
        create_password(username)

def monthname(username):                       #Global Naming Of File
    month = ['Jan','Feb','March','April','May','June','July',
          'Aug','Sept','Oct','Nov','Dec']
    time.sleep(1.5)
    mo = int(input('Enter the Month (XX) \t:\t'))
    time.sleep(1.5)
    while mo<1 or mo > 12 :
        print('! ! ! Error_ ',mo,'  month not exist ' )
        time.sleep(1.5)
        mo = int(input('Enter the Month (XX)\t:\t'))
        time.sleep(1.5)
    month = month[mo-1]
    print('\t\t\t\t\t',month)
    time.sleep(1.5)
    year = int(input('Enter the Year(XXXX) \t:\t'))
    time.sleep(1.5)
    if year<100 :
        year += 2000
    location = 'Data Base\\'  + month  +str(year) + username
    #print ('file location\t;\t', location)
    return location




#----------------------------------------------------------------------------------------
#functions

#earnings
def input_earning(username) :
    location = monthname(username)
    try:
        file = open(location+' Earning.txt' , 'r')
        rec = file.readline()
        time.sleep(1.5)
        print('\n\n', rec)
        time.sleep(1.5)
        print('File already Exists\n')
        time.sleep(1.5)
        choice = input('Enter (yes) to change the value else (no) to continue\t:\t')
        time.sleep(1.5)
        if choice == 'yes' or choice == 'Yes' or choice == 'y' :
            inp = int(input('Enter new amount of earning\t:\t'))
            time.sleep(1.5)
            file.close()
            file = open(location+' Earning.txt' , 'w')
            file.write('Earning'+'\t'+str(inp))
    except IOError:
        inp = int(input('Enter amount of earning\t:\t'))
        time.sleep(1.5)
        file = open(location+' Earning.txt' , 'w')
        file.write('Earning'+'\t'+str(inp))
    file.close()

def display_earning(username) :
    location = monthname(username)
    try:
        file = open(location+' Earning.txt' , 'r')
        x = file.readline()
        y = x.split()
        a = int(y[-1])
        time.sleep(1.5)
        print('Entered earning was\t:\t',a)
        time.sleep(1.5)
        file.close()
    except IOError:
        time.sleep(1.5)
        print('No record found')
        time.sleep(1.5)
        choice = input('Press (yes) to enter the record \t:\t')
        if choice == 'yes' or choice == 'Yes' or choice == 'y' :
            input_earning(username)




#permanent expanditure
def newpermaexp(username)  :
    file = open('Data Base\Recent_Permanent '+username+'.txt','w+')
    time.sleep(1.5)
    print('Enter name and amount of permanent expanditure\n\tExample;\
House rent,EMI,School fees, gas cylinder etc')
    time.sleep(1.5)
    choice = 'yes'
    total = 0
    while choice == 'yes' or choice == 'Yes' or choice == 'y' :
        name = input('Enter name of expanditure\t\t:\t')
        value = input('Enter value\t\t\t:\t')
        time.sleep(1.5)
        file.write(name+'\t'+ value +'\r')
        total += int(value)
        choice = input('Enter (yes) to input more records else(no)\t:\t')
        time.sleep(1.5)
    file.write('Total'+'\t'+str(total))
    file.close()

def displaypermaexp(username):
    try :
        file = open('Data Base\Recent_Permanent '+username+'.txt','r')
        time.sleep(1.5)
        print('-'*100,'\nName\t\tExpanditure\n','-'*100)
        time.sleep(1.5)
        total = 0
        y = file.readline()
        x = y.split()
        while str(x[0]) != 'Total' :
            for i in range(0,len(x)-1) :
                print(x[i],end =' ')
                time.sleep(.3)
            print('\t',x[-1],'\t')
            time.sleep(.3)
            total += int(x[-1])
            y = file.readline()
            x = y.split()
        time.sleep(1.5)
        print('-'*100,'\nTotal Expanditure\t:\t', x[-1] , '\n','-'*100)      #displays total
        time.sleep(1.5)
        file.close()
        return total
    except IOError:
        time.sleep(1.5)
        print('\nNo File Found\n\n')
        newpermaexp(username)

def permaexpeditor(username):
    import os
    pexp= 'Data Base\Recent_Permanent '+username+'.txt'
    file = open(pexp,'r+')
    tran = open('Data Base\Replace.txt','w')
    y = file.readline()
    x = y.split()
    total = 0
    while x[0] != 'Total' :
        print(x[0] ,'\t:\t' , x[-1])
        time.sleep(1.5)
        choice  = input('Enter (yes) to continue else (no) to change value \t:\t')
        if choice == 'no' :
            x[-1] = input('Enter new value\t:\t')
        tran.write(x[0]+'\t'+ str(x[-1])+'\r')
        total += int(x[-1])
        y = file.readline()
        x = y.split()
    tran.write('Total'+'\t'+str(total))
    file.close()
    tran.close()
    os.remove(pexp)
    os.rename('Data Base\Replace.txt',pexp)
    return total

def permaexp(username):
    location = monthname(username)
    file = open (  location + ' Perma_Exp.txt' , 'w' )
    total = displaypermaexp(username)
    time.sleep(1.5)
    choice = input('Enter (yes) to continue else (no) to change values  \t:\t')
    if choice == 'no':
        total = permaexpeditor(username)
    file.write(str(total))





#temporary expanditure
def newtempexp(username):
    file = open ( 'Data Base\\'+username + ' Temp_Exp.txt' , 'w' )    #To read no. of records
    time.sleep(1.5)
    print('\n\t\tTemporary Expanditure\nDescription ; \n\tYou can add categories of records\
of the expanditure which you make other then permanent expenditure whick are not fix\n\
For Example; Electricity , Fuel , Medicine , Ration and \
others categories.')
    time.sleep(1.5)
    choice = 'yes'
    while choice != 'no' and choice == 'yes'  or choice == 'Yes' or choice == 'y' :
        time.sleep(1.5)
        cat = input ('Enter name of expanditure\t:\t')
        time.sleep(1.5)
        file.write(cat  + '\r')
        choice = input('Press (yes) if you want to enter more catogaries else (no)    :    ')
    file.close()


# noinspection PyUnreachableCode
def addrec_tempexp(username) :
    try :
        f = open ( 'Data Base\\'+username + ' Temp_Exp.txt' , 'r' )    
        location = monthname(username)+ ' Temp_Exp'
        file = open ( location +'.txt','w' )
        total =  0
        b = f.readline()
        a = b.split()
        if b == '':
            newtempexp(username)
            b = f.readline()
            a = b.split()
        while a  :
            time.sleep(1.5)
            print( 'Enter ',a[0],' expanditure\t:',end='\t')
            time.sleep(1.5)
            b = int(input())
            file.write(str(a[0])+'\t'+str(b) +'\r')
            total += b
            b = f.readline()
            a = b.split()
        time.sleep(1.5)
        print('Total Temporary expanditure\t:\t',total)
        time.sleep(1.5)
        file.write('Total'+ '\t' + str(total))
        return total
        f.close()
    except IOError:
        time.sleep(1.5)
        print('No category of expanditure found')
        newtempexp(username)

def heading(username,type):
    try :
        f = open ('Data Base\\'+username + type +'.txt' , 'r' )
        time.sleep(1.5)
        print('-'*100,end = '\nMonth\t\t')
        rec = f.readline()
        rec = rec.split()
        while rec :
            print(rec[0],end='\t')
            rec = f.readline()
            rec = rec.split()
        print('Total\n','-'*100)
        f.close()
    except IOError:
        time.sleep(1.5)
        print('No category of expanditure found')
        time.sleep(1.5)
        newtempexp(username)


def display_tempexp_month(username):
    time.sleep(1.5)
    print('Display record of month')
    time.sleep(1.5)
    location = monthname(username)
    try :
        file = open ( location  + ' Temp_Exp.txt','r' )
        x =slice(10,-1,1)
        name = location[x]
        heading(username,' Temp_Exp')
        print( name, end ='\t')
        rec = file.readline()
        x= rec.split()
        while rec :
            print (x[-1],end = '\t')
            rec = file.readline()
            x= rec.split()
        print('\n','-'*100)
        file.close()
    except IOError :
        time.sleep(1.5)
        print('No record found')
        time.sleep(1.5)
    
def display_tempexp_all(username) :
    data = open('Data Base\Temp_Exp '+username+'.txt','w')
    mo = ['Jan','Feb','March','April','May','June','July',
          'Aug','Sept','Oct','Nov','Dec']
    time.sleep(1.5)
    print('\n\n\tData Fetching in Progress\n\
Wait > It Might Take Few Seconds\n\n')
    time.sleep(1.5)
    print('DISPLAY ALL RECORDS')
    time.sleep(1.5)
    year = 2000
    while year!= 2200 :
        for j in mo :
            na = str(j)+str(year) 
            f = 'Data Base\\'+na + username + ' Temp_Exp.txt'
            try:
                file = open(f,'r')
                #graph()
                print(na)
                data.write(na + '\t')
                rec = file.readline()
                x = rec.split()
                while rec :
                    data.write(x[-1]+ '\t')
                    rec = file.readline()
                    x= rec.split()
                data.write('\r')
                file.close()
            except IOError:
                io = 'IOE'
        year+=1
    data.close()
    
    #display
    heading(username,' Temp_Exp')
    data = open('Data Base\Temp_Exp '+username+'.txt','r')
    rec = data.readline()
    while rec :
        x = rec.split()
        for i in x :
            print(i,end = '\t')
        print('\n')
        rec = data.readline()
    print('\n',"_"*100)
    data.close()




#Savings and planed expanditure
def savings(username):
    time.sleep(1.5)
    print('enter family time expanditures of this month, if any\n\
for example; F.D.  Family Trip, Festival, Function and many more categories')
    location = monthname(username) + ' Planed_Exp.txt'
    file = open(location , 'w' )
    total = 0
    choice = 'yes'
    while choice == 'yes' or choice == 'Yes' or choice == 'y' :
        time.sleep(1.5)
        a = input('Enter category of expanditure\t:\t')
        time.sleep(1.5)
        b = int(input('Enter amount\t:\t'))
        file.write(a + '\t' + str(b) + '\r')
        time.sleep(1.5)
        choice = input('Press (yes) if you want to enter more categories, else (no)\t:\t')
        total += b
    file.write('Total'+'\t'+str(total))
    time.sleep(1.5)
    print ('Total Planned Expanditure\t:\t',total)
    file.close()

def display_savings(username) :
    time.sleep(1.5)
    print('Saved and Planned Expanditure')
    location = monthname(username) + ' Planed_Exp.txt'
    file = open(location , 'r' )
    rec = file.readline()
    while rec:
        print(rec,end='\n')
        time.sleep(1.5)
        rec = file.readline()
    file.close()

#_________________________________________________________________________________________
#Analysis
def create_record(username) :
    data = open('Data Base\All Records '+username+'.txt','w')
    ext = [' Earning.txt',' Perma_Exp.txt',' Temp_Exp.txt',' Planed_Exp.txt']
    mo = ['Jan','Feb','March','April','May','June','July',
          'Aug','Sept','Oct','Nov','Dec']
    time.sleep(1.5)
    print('\n\n\tData Fetching in Progress\n\
Wait > It Might Take Few Seconds\n\n')
    time.sleep(1.5)
    print('FETCHING ALL RECORDS')
    time.sleep(1.5)
    try :
        bank = open('Data Base\Initial Balance '+username+'.txt','r')
        A = bank.readline()
        balance = A.split()
        left = int(balance[0])
        bank.close()
    except IOError :
        time.sleep(1.5)
        print('No bank balance found')
        balance(username)
    year = 2000
    while year!= 2051 :
        for j in mo :
            na = str(j)+str(year)
            data.write(na +'\t')
            for type in ext :
                try:
                    file = 'Data Base\\'+na + str(username) + type
                    f = open(file,'r')
                    ##print('\n\n\Type   ', type)
                    rec = f.readline()
                    ##print('rec   ',rec)
                    x = rec.split()
                    ##print('x   ',x)
                    if rec == '':
                        break
                    else:
                        while rec:                              #to reach last term
                            y = x
                            rec = f.readline()
                            ##print('rec   ',rec)
                            x = rec.split()
                            ##print('x   ',y)
                        ##print('x last',y[-1],len(y))
                        x = y
                        if len(x) != 0 :
                            data.write(str(x[-1])+'\t')
                            ##print(x[-1])
                            if type == ext[0]:
                                left += int(x[-1])
                            else :
                                left -= int(x[-1])
                    f.close()
                except IOError:
                    io = None
                    data.write(str(0) + '\t')
            data.write(str(left) + '\r')
        year+=1
        bank.close()
    data.close()
    bank = open('Data Base\Balance '+username+'.txt','w')
    bank.write(str(left))
    bank.close()
    time.sleep(1.5)
    print('\tRecord created sucessfully!!!\n\n')
    time.sleep(1.5)
    print('Balance left in your account\t:\t',left)


def analysis(username):
    create_record(username)
    time.sleep(1.5)
    print('DISPLAY ALL RECORDS')
    time.sleep(1.5)
    file = open('Data Base\All Records '+username+'.txt','r')
    year = int(input('Enter year to show analysis\t:\t'))
    time.sleep(1.5)
    if year< 100 :
        year += 2000
    mo = ['Jan','Feb','March','April','May','June','July',
          'Aug','Sept','Oct','Nov','Dec']
    print( '-'*110,'\nMonth\t\tEarning\tTemp Exp\tPerma Exp\tPlanned Exp\tBalance Left\n','-'*110)
    time.sleep(1.5)
    earning, expanditure , balance = [] , [] , []
    for month in mo :
        na = month +str(year)
        line = file.readline()
        word = line.split()
        print(month,end= '\t\t')
        x = False
        while x != True :
            if word[0] == na :
                for i in range(5):
                    print(word[i+1],end = '\t\t')
                earning.append(int(word[1]))
                expanditure.append(int(word[2]) + int(word[3]) + int(word[4]))
                balance.append(int(word[5]))             
                print('\n')
                x = True
            else :
                line = file.readline()
                word = line.split()
    file.close()
    print('-'*110)
    time.sleep(1.5)
    graph('Earning Graph '+ str(year) , mo, earning)
    time.sleep(1.5)
    graph('Expanditure Graph '+str(year) , mo , expanditure)
    time.sleep(1.5)
    graph('Balance Variation Graph '+str(year), mo , balance)



def graph ( title , x , y ) :
    import matplotlib.pyplot as plt
    plt.plot(x,y,marker = 'D')
    plt.title(title)
    plt.xlabel('Month')
    plt.ylabel('Amount')
    for i in range(len(x)):
        # I rounded the y values as string and used the same x and y coords as the locations
        # next we can give a constant offset points to offset the annotation from each value
        # here I used (-20,20) as the offset values
        plt.annotate(f"{str(round((y[i])))}",(x[i],y[i]),xycoords='data',
                     xytext=(-20,20), textcoords='offset points')
    plt.show()

def balance(username) :
    file = open('Data Base\Initial Balance '+username+'.txt','w')
    time.sleep(1.5)
    bal = int(input('Enter you total bank Balance\t:\t'))
    file.write(str(bal))
    file.close()


#---------------------------------------------------------------------------------------
def system(username) :
    time.sleep(1.5)
    print('\n\tSystem Menu\n\
Switch User------------1\n\
Change Password------2\n\
Delete Account--------3')
    time.sleep(1.5)
    choice = int(input('Enter your choice\t:\t'))
    time.sleep(1.5)
    if choice == 1 :
        password()
    elif choice == 2 :
        create_password(username)
    elif choice ==3 :
        choice = input('Enter (yes) to continue deleting your account \t:\t')
        if choice == 'yes' or choice == 'Yes' :
            username = password()
            factoryreset(username)

def factoryreset(username):
    import os
    files = ['Data Base\\'+username + ' credential.txt',
             'Data Base\Recent_Permanent '+username+'.txt',
             'Data Base\\'+username + ' Temp_Exp.txt',
             'Data Base\Temp_Exp '+username+'.txt',
             'Data Base\Initial Balance '+username+'.txt',
             'Data Base\Balance '+username+'.txt',
             'Data Base\All Records '+username+'.txt']
    time.sleep(3)
    print('\n\n\tData Fetching in Progress\n\
Wait > It Might Take Few Seconds\n\n')
    time.sleep(3)
    print('DELETING ALL RECORDS')
    time.sleep(1.5)
    print('-'*60,'\n\tFiles Removed\n','-'*60)
    time.sleep(1.5)
    for x in files :
        try :
            f = open(x,'r')
            print(x)
            time.sleep(.25)
            f.close()
            os.remove(x)
        except IOError :
            IO = None
    ext = [' Earning.txt',' Perma_Exp.txt',' Temp_Exp.txt',' Planed_Exp.txt']
    mo = ['Jan','Feb','March','April','May','June','July',
          'Aug','Sept','Oct','Nov','Dec']
    year = 2000
    while year!= 2200 :
        for j in mo :
            na = str(j)+str(year)
            for type in ext :
                file = 'Data Base\\'+na + str(username) + type
                try :
                    f =open(file,'r')
                    print(file)
                    time.sleep(.25)
                    f.close()
                    os.remove(file)
                except IOError :
                    IO = None
        year +=1
    time.sleep(1.5)
    print('Account Deleated Sucessfully')
    done(username)


             
    

#----------------------------------------------------------------------------------------
def Add_Rec(username):
    time.sleep(1.5)
    dict2 = {1 : input_earning, 2 : permaexp ,
             3 : addrec_tempexp , 4 : savings  }
    choice = -1
    if choice != 0 :
        print('\n\tAdd Records\n\
Earning----------------------1\n\
Permanent Expanditure------2\n\
Temporary Expanditure------3\n\
Planned Expanditure---------4')
        time.sleep(1.5)
        choice = int(input('Enter your choice\t:\t'))
        time.sleep(1.5)
        dict2.get(choice)(username)

def Display_Rec(username) :
    dict3 = { 1 : display_earning, 2 : displaypermaexp  , 3 : display_tempexp_month ,
              4 : display_tempexp_all , 5 : display_savings }
    choice = -1
    if choice != 0 :
        time.sleep(1.5)
        print('\n\tDisplay Records\n\
Earning of a month------------------1\n\
Currenet Permanent Expanditure----2\n\
Temporary Expanditure(by Month)---3\n\
Temporary Expanditure(all Month)---4\n\
Planned Expanditure-----------------5')
        time.sleep(1.5)
        choice = int(input('Enter your choice\t:\t'))
        time.sleep(1.5)
        dict3.get(choice)(username)

def done(username) :
    time.sleep(1.5)
    print('Have a good day ',username)
    time.sleep(1.5)
    quit()

#________________________________MAIN MENU____________________________________________
import time
time.sleep(1.5)
print('  \n\t\t\t Welcome to House Management  \n\t')
time.sleep(1.5)
username = password()
dict1 = { 0 : done , 1 : Add_Rec , 2 : Display_Rec, 3 : analysis , 4 : system}
choice = -1
while choice != 0 :
    print('\n\tMain Menu\n\
Quit-------------------------0\n\
Add Records-----------------1\n\
Display Records--------------2\n\
Complete Analysis-----------3\n\
System Settings--------------4')
    time.sleep(1.5)
    choice = int(input('Enter your choice\t:\t'))
    dict1.get(choice)(username)
