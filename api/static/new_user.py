from tim_app.models import User, Request, Supply
from api.static import passGen

#creates a user with a random password and takes an unique username and phone number
def create_user_phone(userName,number):
    #if username is taken, abort creation
    if User.objects.filter(username=userName):
        print('username is already taken')
    elif User.objects.filter(phoneNr = number):
        print('phone number already taken')
    #creates user with random password and adds it to the database
    else:
        u = User(username=userName,password=passGen.generate(),phoneNr=number)
        u.save()


#creates a user with complete data, takes username, password, phone number, email, coordinates, radius
def create_user_complete(userName, passw, number, mail, position, rad):
    #if username is taken, abort creation
    if User.objects.filter(username=userName):
        print('username is already taken')
    #creates user and saves it to the database
    else:
        u = User(username=userName, password=passw, phoneNr=number, email=mail, location=position, radius= rad)
        u.save()
