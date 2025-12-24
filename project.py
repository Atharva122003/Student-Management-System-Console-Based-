student_db={101:{'name':'shree ganesh','course':'Data Science','tfees':40000,'pfees':20000,'rfees':20000}}
course_fees={'Data Science':40000,'Web Development':30000,'Aws':20000,'Software testing':15000}
users={'vaibhav':'vaibhav123','sagar':'sagar123','atul':'atul123'}
admins = {'admin123': 'admin@123'}
while True:
    username=input('UserName: ')
    password=input('Password: ')
    if username in users and password==users[username]:
        break
print('Welcome To The Dashboard'.center(100,'-'))
while True :
    print('''
    1.Add Student Data
    2.Display Student Data
    3.Update Student Data
    4.Delete Student Data    
    5.Filter Student Data
    6.admin login      
    7.LogOut
    ''')
    ch=int(input("Enter Your Choice: "))
    if ch==1:
        name=input("Name: ")
        courses=list(course_fees.keys())
        print('Available Courses: ')
        sr=1
        for course in courses:
            print(f'{sr}.{course}')
            sr=sr+1
        ch=int(input("Select Your Course: "))
        index=ch-1
        course=courses[index]
        #var[key]
        fees=course_fees[course]
        print(f'fees for {course} is {fees}')
        dis=eval(input("Discount: "))
        tfees=fees-fees*dis/100
        print(f'fees after {dis}% is {tfees}')
        pfees=eval(input("Enter Pfees: "))
        rfees=tfees-pfees
        print(f'Total Fees: {tfees}\nPaid fees: {pfees}\nRemaining Fees: {rfees}')
        #var[key]=value
        reg=len(student_db)+101
        student_db[reg]={'name':name,'course':course,'tfees':tfees,'pfees':pfees,'rfees':rfees}
        print("Added successfully....")
    elif ch==2:
        print('-'*125)
        print(f'|{'Reg No':^20}|{'StudentName':^20}|{'CourseName':^20}|{'TotalFees':^20}|{'PaidFees':^20}|{'RemainingFees':^20}|')
        print('-'*125)
        for reg in student_db:
            print(f'|{reg:^20}|{student_db[reg]['name']:^20}|{student_db[reg]['course']:^20}|{student_db[reg]['tfees']:^20}|{student_db[reg]['pfees']:^20}|{student_db[reg]['rfees']:^20}|')
            print('-'*125)
    elif ch==3:
        cont=True
        while cont:
            reg=int(input("Reg No: "))
            if reg in student_db:
                cont=False
        print('''
            1.Name
            2.Fees
            3.change Course
        ''')
        ch=int(input("Enter Your Choice: "))
        if ch==1:
            uname=input('Name: ')
            #var[key]=uvalue
            student_db[reg]['name']=uname
            print('Updated successfully')
        elif ch==2:
            print(f'Course Name: {student_db[reg]['course']} \nTotal Fees: {student_db[reg]['tfees']} \nPaid Fees: {student_db[reg]['pfees']} \nRemaining Fees: {student_db[reg]['rfees']}')
            fees=eval(input("enter amount: "))
            student_db[reg]['pfees']=student_db[reg]['pfees']+fees
            student_db[reg]['rfees']=student_db[reg]['rfees']-fees
            print('Thank You')

        elif ch==3:
            pass
        else:
            print('Invalid Input')
    elif ch==4:
        while True:
            reg=int(input("Reg no: "))
            if reg in student_db:
                break
        student_db.pop(reg)
        print(f'deleted successfully..')
    elif ch==5:
        print('''
        1.Course
        2.Remaining Fees
        ''')
        ch=int(input("Filter By: "))
        if ch==1:
            courses=list(course_fees.keys())
            sr=1
            for course in courses:
                print(f'{sr}.{course}')
                sr=sr+1
            ch=int(input("Filter By: "))
            index=ch-1
            course=courses[index]
            print('-'*125)
            print(f'|{'Reg No':^20}|{'StudentName':^20}|{'CourseName':^20}|{'TotalFees':^20}|{'PaidFees':^20}|{'RemainingFees':^20}|')
            print('-'*125)
            for reg in student_db:
                if student_db[reg]['course']==course:
                    print(f'|{reg:^20}|{student_db[reg]['name']:^20}|{student_db[reg]['course']:^20}|{student_db[reg]['tfees']:^20}|{student_db[reg]['pfees']:^20}|{student_db[reg]['rfees']:^20}|')
                    print('-'*125)
        elif ch==2:
            print('-'*125)
            print(f'|{'Reg No':^20}|{'StudentName':^20}|{'CourseName':^20}|{'TotalFees':^20}|{'PaidFees':^20}|{'RemainingFees':^20}|')
            print('-'*125)
            for reg in student_db:
                if student_db[reg]['rfees']>0:
                    print(f'|{reg:^20}|{student_db[reg]['name']:^20}|{student_db[reg]['course']:^20}|{student_db[reg]['tfees']:^20}|{student_db[reg]['pfees']:^20}|{student_db[reg]['rfees']:^20}|')
                    print('-'*125)
        else:
            print('invalid input....')
    elif ch == 6:
        print("------ Admin Login ------")
        admin_user = input("Admin Username: ")
        admin_pass = input("Admin Password: ")
        
        if admin_user in admins and admins[admin_user] == admin_pass:
            print("Admin Login Successful!")
            while True:
                print('''
                ----- Admin Dashboard -----
                1. Add New Course
                2. Add New User
                3. Display All Courses
                4. Access Student Data
                5. Add Another Admin
                6. Back to Main Menu
                ''')
                ach = int(input("Enter Your Choice: "))
                if ach == 1:
                    cname = input("Enter New Course Name: ")
                    fees = eval(input(f"Enter Fees for {cname}: "))
                    course_fees[cname] = fees
                    print(f"Course '{cname}' added successfully with fees ₹{fees}.")
                elif ach == 2:
                    uname = input("Enter New Username: ")
                    if uname in users:
                        print("User already exists!")
                    else:
                        upass = input("Enter Password: ")
                        users[uname] = upass
                        print(f"User '{uname}' added successfully.")
                elif ach == 3:
                    print("------ Available Courses ------")
                    for course, fee in course_fees.items():
                        print(f"{course} : ₹{fee}")
                elif ach == 4:
                    print('-'*125)
                    print(f'|{"Reg No":^20}|{"StudentName":^20}|{"CourseName":^20}|{"TotalFees":^20}|{"PaidFees":^20}|{"RemainingFees":^20}|')
                    print('-'*125)
                    for reg in student_db:
                        print(f'|{reg:^20}|{student_db[reg]["name"]:^20}|{student_db[reg]["course"]:^20}|{student_db[reg]["tfees"]:^20}|{student_db[reg]["pfees"]:^20}|{student_db[reg]["rfees"]:^20}|')
                        print('-'*125)
                elif ach == 5:
                    new_admin = input("Enter New Admin Username: ")
                    if new_admin in admins:
                        print("Admin already exists!")
                    else:
                        new_pass = input("Enter Admin Password: ")
                        admins[new_admin] = new_pass
                        print(f"Admin '{new_admin}' added successfully!")
                elif ach == 6:
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid Choice.")
        else:
            print("Invalid Admin Credentials.")
    elif ch==7:
        break
    else:
        print('Invalid Input')