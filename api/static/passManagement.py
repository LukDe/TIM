from tim_app.models import User, Request, Supply

#takes username returns password
def getPass(name):
    #check if username exists
    if User.objects.filter(username=name):
        #get password of user and return it
        temp=User.objects.get(username=name).password
        return temp
    #if the user does not exist, abort
    else:
        print('user does not exist')


#takes username, phone number, password and returns True or None for false
def checkPass(name,number,passw):
    #if the user exists get the user object
    if User.objects.filter(username=name):
        temp=User.objects.get(username=name)
        #check the phoneNr
        if int(temp.phoneNr)==int(number):
            #return if True if the password matches
            if temp.password==passw:
                return True
