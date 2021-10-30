print ("Welcome!")
print ("pleas answer in English and click space once before you answer")  

def een():

    a = input ("what is your name?")
    print("hello, " + a )

    b = input ("are you older then 12?") 
    if b == 'no' or b == 'NO':
     print ("We are sorry, but you have to be above 12")  
    if b == 'yes' or b == 'YES':
     print ("thats good to hear!")

    c = input ("How old are you then?") 
    print("thats good to hear, " + a ) 

een()
 