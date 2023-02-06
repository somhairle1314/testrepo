# Python Code
# This program will calculate the number of pleats in a kilt
# The user will be prompted to input the Tartan Size and Hip Measurements

# Developer Wilkins, Somhairlè CMIS102 Date 1/19/2023
# I wrote this edition from scratch on 2/2/2023 to update code for calling functions and validating inputs


#------Functions--------------------------

def Welcome():# This function will Welcome the user, explain the program purpose, and position the first steps
    print("\nWelcome to Somhairlè's Kilt service")
    print("\nThis program will determine the number of pleats in your kilt and how wide each pleat should be")
    print("\nFirst we need some measurements from you.")


def measurement1():
    #Get user input for hip measurement
    hip = eval(input("\n Please enter your hip measurement in inches."))
    #Validate the user input as the standard 8 yard kilt may be too big or too small for some measurements
    if hip <= 20 or hip >= 50:
        print("\nAre you sure the number is correct? This calculator is for our standard 8 yard kilt. You may be better served by one of our other calculators.")
        hip = eval(input("\n Please enter your hip measurement in inches."))
    else: print("\nThank you.")
    return(hip)

def measurement2():
     #Get user input the size of the tartan sett
    sett = eval(input("\n Please enter the size of the Tartan Sett in inches."))
    #validate the user input to make sure the number is correct and that the material is an appropriate tartan for making kilts. 
    if sett <= 0:
        print("\nA tartan sett has to be a positve number.")
        sett = eval(input("\n Please enter the size of the Tartan Sett in inches."))
    elif sett < 5 and sett > 0:
        print("\nThis tartan is not suitable for a kit as the sett size is too small. Make sure your measurement is accurate or reach out for how to buy kilt tartan.")
        sett = eval(input("\n Please enter the size of the Tartan Sett in inches."))
    else: print("\nThank you.")
    return(sett)

def pleatNumber(a):#Calculate the number of whole pleats
    rearYardage = 216 #the number of inches in 6 yards. This is a constant as the typical kilt has 6 yards of material to make the pleats
    numPleat = rearYardage // a #a will be set to sett size for this equation

    return(numPleat)

def pleatWidth(x, y): #Calculate the width in inches of each pleat
    widthPleat = x / 2 / y #this takes half the hip measurement and determines how large each pleat needs to be to fit across the back of the kilt.

    return(widthPleat)

#Both calculations were taken from
#Tewksbury B., & Stuehmeyer E (2019) The Art of Kiltmaking (pp 36-40)(3rd ed.). Celtic Dragon Press.

def display(a,b):
    print("\nThe number of pleats in your kilt is: ", a)
    print("\nThe width of each pleat in your kilt is: ", b)
    return()

def main():
    Welcome()# Call the welcome function

    #get user inputs for hip size and sett size
    hipSize = measurement1()
    settSize = measurement2()
    
    print(hipSize)
    numPleat = pleatNumber(settSize)#calculate number of pleats
    pleatSize = pleatWidth(hipSize,numPleat)#calculate the width in inches for each pleat
    
    display(numPleat, pleatSize)#displays the number of pleats and their width

    
main()
