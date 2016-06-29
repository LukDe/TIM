import  random

#creates a password composed of three chars and three ints
def generate():
        #initialising array
        passcode=[1,2,3,4,5,6]
        #override elements in array with random elements
        for i in range(3):
                #picks three random integers ins ascii
                passcode[i] = translate(random.randint(48,57))
                #picks three random chars in ascii
                passcode[i+3] = translate(random.randint(97,122))
        #shuffle the elements in the array
        prasscode=random.shuffle(passcode)
        #assembles the array as a string
        passcode= passcode[0]+passcode[1]+passcode[2]+passcode[3]+passcode[4]+passcode[5]
        return passcode

#converts int to ascii
def translate(var):
        temp = chr(var)
        return temp
