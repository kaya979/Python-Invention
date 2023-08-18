###############################################
#      DECISION MAKING IN PYTHON  : ELIF      #
###############################################
#
#
# When you need to check multiple statements, then use elif statements
#
# if condition 1: 
#       statements
# elif condition 2: 
#       statements
# elif condition 3:
#       statements
# else :    
#       statements

# ELIF cannot exit by itself
# IT must come after an IF
# ELIF will be checked in the order that they appear
# example:

if 5==4:
    print("An if statement. Wooooow!")
elif 4 == 5:
    print("Elif is something neeeew!!!")
elif 14<9: 
    print("Really?")
else:
    print("Not this time")

# change the number in the above example to understand what happens. The second elif will not be
# evaluated if the first elif evaluates as true. 
# In if-elif blocks, the conditions will be tested until a condition is found to be true. 
# if all the if and elif conditions are evaluated false, then the else block will be executed. 
