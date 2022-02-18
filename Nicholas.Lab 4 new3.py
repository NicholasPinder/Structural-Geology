import math
theta1= 130    # true dip of theta 2 
alpha1= 15     # respective plunge of 1 
theta2= 45     # true dip of theta2 
alpha2= 28     # respective plunge of 2 

phi = abs(theta1 - theta2)  # take absolute value to get true dip direction er
 
while phi >=90:             
    if phi <180:            # if the angle is less that 180 than do this 
        phi = 180 - phi     # add them together if the number is acute 
    elif phi > 180:         # if it is greater than 180 then do this 
        phi = phi - 180     # minus the difference by 180 to get to a number that is not acute 

assert phi !=0, 'Apparent dips not the same'   # State this statement if meets neither of these conditions 

print ("phi=",phi)

ralpha1 = math.radians(alpha1)   # converts degrees to radians 
ralpha2 = math.radians(alpha2)   # converts degrees to radians 
rphi = math.radians(phi)         # converts phi t radians 

TDA= (1/math.sin(rphi)) * ((1/math.tan(ralpha1)) * (math.tan(ralpha2)) - (math.cos(rphi))) # angle between theta 1 and true dip angle 
print ("True Dip Angle=",TDA)

if (theta1 > theta2):       # find true dip direction 
    TDD = theta1 - TDA      # if theta is to large minus to get to back to get true direction 
else:                       # if not greater than this 
    TDD = theta1 + TDA      # if theta is smaller than add them to get true direction 
print ("True Dip Direction=",TDD)

strike = TDD - 90         # get the strike by minusing 90 
if strike < 0:            # however if the strike is less than 0 or negative then add 360 
     strike += 360        # strike direction 

print ('Strike=',strike)    # print statement, outputs Strike =


"""
sigma = math.sin(ralpha2)                 # take the sin of the variable 
delta = math.tan(ralpha1)/(sigma)         # take the value by dividing tan by sin 
Strike = math.tan(delta)/math.sin(sigma)  # get strike by dividing them both 

"""

