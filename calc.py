#stating variables
hrs = input("Enter your hours: ")
rph = input("enter your hourly rate: ")
gp = float(hrs)*float(rph)

#converting to float
hrs = float(hrs)
rph = float(rph)

#conditional statement without overtime
if hrs <= 40:
    gp= hrs*rph
else:
    rg = 40 * rph
    oth = hrs-40
    otp = oth*(rph*2.5)
    gp = rg+otp

print("Gross Pay", gp)




#Overtime calculation
otp = (hrs-40)*rph*2.5

print(gp)