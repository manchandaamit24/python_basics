def isNumberEven(num):
    isEven = False
    if((int(num)%2) == 0):
        isEven = True
    else:
        isEven = False
        
    return isEven

#print(isNumberEven(0))

def checkNum(num):
    number_1 = int(num)

    if(number_1%3==0 and number_1%5==0):
        print("Number divisble by both 3 & 5")
    elif(number_1%3==0):
        print("Number divisible by 3")
    elif(number_1%5==0):
        print("Number is divisble by 5")
    else:
        print("Sorry, Number doesn't divide by 3 & 5")

checkNum(26)


def monthConversion(mon):
    monthConversionsDic = {
        "Jan":"January",
        "Feb":"February",
        "Mar":"March"
    }
    print(monthConversionsDic.get(mon,"Not a valid Month"))

#monthConversion("Feb1")


#def isNumberPrime(num):
#    input_num = int(num)
    

def sampleWhileLoop():
    i = 1
    while i<=10:
        print(i)
        i += 1
    
    print(i)

    print("Done with Loop")

sampleWhileLoop()

