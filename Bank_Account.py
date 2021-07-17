blist = []
import random
import string

class BankAccount:

    def __init__(s, id='', name='', email='', contact=0, bal=0, acc_no=0, password='', dep=0, wdr=0):
        s.id = id
        s.name = name
        s.email = email
        s.contact = contact
        s.bal = bal
        s.acc_no = acc_no
        s.password = password
        s.dep = dep
        s.wdr = wdr


    def __str__(s):
        return '{} {} {} {} {} {} {} {} {}'.format(s.id,'',s.name,'',s.email,'',s.contact,'', s.bal,'', s.acc_no,'', s.password,'',s.dep,'',s.wdr)
   

    def register(s):
        print('--- REGISTER YOUR ACCOUNT ---'.center(60,' '))
  
        s.id = input('User ID : ')
        s.name = input('Name : ')
        s.email = input('E-mail ID : ')
        s.contact = int(input('Contact : +91 '))
        s.bal = int(input('Initial Amount : Rs. '))
        s.acc_no = ''.join(random.choices(string.digits, k=14))
        char = string.ascii_letters + string.digits
        s.password = ''.join(random.choices(char, k=8))
 
        
        print('--- REGISTRATION SUCCESSFUL ---'.center(60,' '))    
        print('--- PLEASE NOTE YOUR ACCOUNT NO. & PASSWORD ---'.center(60,' '))
                    
        print(f'{s.name},\tYour Account No.: ', s.acc_no)
        print('\tPassword : ', s.password)

        b = BankAccount(s.id, s.name, s.email, s.contact, s.bal, s.acc_no, s.password)
        blist.append(b)


    def login(s):
        print('--- LOGIN YOUR ACCOUNT ---'.center(60,' '))
            
        acc = int(input('Account No.: '))
        pwd = input('Password : ')
        for i in blist:
            if acc == i.acc_no or pwd == i.password:
                print('--- LOGIN SUCCESSFUL ---'.center(60,' '))
                s.transfer()
            else:
                print('--- ENTER VALID ACCOUNT NO. & PASSWORD ---'.center(60,' '))


    def customer_details(s):
        print('USER ID\tNAME\tEMAIL\tCONTACT\tBALANCE')
        for i in blist:
            print(i)


    def deposit(s):
        ac = input('Account No.: ')
        s.dep = int(input('Deposit Amount : Rs. '))
        for i in blist:
            if ac == i.acc_no:
                i.bal = int(i.bal) + s.dep
                print('Balance After Deposit : Rs. ', i.bal)

                print('--- AMOUNT DEPOSITED ---'.center(60,' '))


    def withdraw(s):
        ac = input('Account No.: ')
        s.wdr = int(input('Withdraw Amount : Rs. '))
        for i in blist:
            if ac == i.acc_no:
                if i.bal > s.wdr:
                    i.bal = int(i.bal) - s.wdr
                    print('Balance After Withdraw : Rs. ', i.bal)
                    
                    print('--- AMOUNT WITHDRAWED ---'.center(60,' '))
                    
                else:
                    print('--- INSUFFICIENT BALANCE ---'.center(60,' '))


    def check_balance(s):
       ac = input('Account No.: ')
       for i in blist:
           if i.acc_no == ac:
               print(f'Total Amount in {i.acc_no} : Rs. ', i.bal)


    def transfer(s):
        ch = 0
        while (ch!=5):
            try:
                print('(1) >> View Customer Details')
                print('(2) >> Deposit Amount')
                print('(3) >> Withdraw Amount')
                print('(4) >> Check Balance')
                print('(5) >> Logout')
                ch = int(input('Select : '))

            except:
                print('Invalid Choice')                
                
            if ch ==1:
                s.customer_details()
                    
            elif ch == 2:
                s.deposit()
                    
            elif ch ==3:
                s.withdraw()
                    
            elif ch == 4:
                s.check_balance()
                
            else:
                print('--- SESSION EXPIRED-LOGIN AGAIN ---'.center(60,' '))
                

                   
def bank_operation():
    b = BankAccount()
    sel = 0
    
    while (sel!=3):
        try:
            print('(1) >> Register')
            print('(2) >> Login')
            print('(3) >> Exit')
            sel = int(input('Select : '))

        except:
            print('Invalid Choice')
        
        if sel == 1:
            b.register()
            
        elif sel == 2:
            b.login()

        else:
            print('--- REGISTER AN ACCOUNT ---'.center(60,' '))


bank_operation()
