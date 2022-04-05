def register():
    db = open('database.txt', 'r')
    email = input("Enter email: ")
    valid_email(email)
    password = input("Enter password: ")
    valid_password(password)
    password1 = input("Confirm password: ")

    d = []
    f = []
    for i in db:
        a,b = i.split()
        d.append(a)
        f.append(b)
    dat = dict(zip(d,f))
    print(dat)


    if password != password1:
        print("passwords don't match")
        register()
    elif email in d:
        print("email already exists")
    else:
        db = open('database.txt', 'a')
        db.write(email + " " + password + "\n")
        print("registration successful")
    login()

def login():
    db = open("database.txt", "r")

    email = input("Email: ")
    password = input("Password: ")
    if not len(email or password) < 1:
        if True:
            d = []
            f = []
            for i in db:
                a,b = i.split()
                d.append(a)
                f.append(b)
            zipped = zip(d,f)
            dat = dict(zipped)
            try:
                if dat[email]:
                    try:
                        if password == dat[email]:

                            print("Login successful")
                            print("Welcome to my first page")
                        else:
                            print("Incorrect email or password")
                            l = input("Enter 0 for forgot password: ")
                            if l == "0":
                                print(dat[email])
                    except:
                        print("Incorrect email or password")
                else:
                    print("Incorrect email or password")
            except:
                print("Incorrect email or password")
        else:
            print("Incorrect email or password")




def valid_email(n):
     a = (n.count("@") == 1 and n.count("&") <= 1)
     count = 0
     for i in range(len(n)):
         if n[i] == "@":
             j = i + 1
             while True:
                 if n[j] == ".":
                     break
                 else:
                     count = count + 1
                     j = j + 1
     b = (count >= 4)
     if (a and b):
         return n
     else:
         print("Not a Valid Email id")
         register()






def valid_password(p):

    flag = True
    if ((len(p)<5) or (len(p)>16)):
        flag = False
    if p.isalnum() == True:
        flag = False
    if p.islower() == True:
        flag = False
    if p.isupper() == True:
        flag = False
    if flag:
        return p
    else:
        print("reenter")
        register()


def home():
    print("                       ")
    print("          HOME         ")
    print("          ----         ")
    print("                       ")
    q = input("Registration --> 1\n"
              "Login        --> 2\n")
    if q == "1":
        register()
    elif q == "2":
        login()
    else:
        print("type either 1 or 2")
    home()

home()
