import  random

def generate():
        passcode=[1,2,3,4,5,6]
        for i in range(3):
                passcode[i] = translate(random.randint(48,57))
                passcode[i+3] = translate(random.randint(97,122))
        prasscode=random.shuffle(passcode)
        passcode= passcode[0]+passcode[1]+passcode[2]+passcode[3]+passcode[4]+passcode[5]
        return passcode

def translate(var):
        temp = chr(var)
        return temp
