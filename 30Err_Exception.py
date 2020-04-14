# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:22:06 2020

@author: Kajal
"""



def add(n1, n2):
    print(n1 + n2)
    
add(10, 20)

## Now
num1 = 10
num2 = input("Please provide a number : ")

add (num1, num2)    ## Type error : as num2 is taken as string
print("Something Happened ! ")

## After occurence of error nothing will get executed from the line at which error occurred

## So Using try

try:
    # Want to attempt a code
    result = 10 +10
except:
    print("Hey it looks you aren't adding correctly!" )

#result   ##>> 20

## Now get error for int + str
try:
    # Want to attempt a code
    result = 10 + '10'
except:
    print("Hey it looks you aren't adding correctly!" )
## >> Hey it looks you aren't adding correctly!
    
try:
    # Want to attempt a code
    result = 10 + 10
except:
    print("Hey it looks you aren't adding correctly!" )
else:
    print("Add went well ! ")
    print(result)

## Finally keyword

try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    print("There was a typeerror")
except OSError:
    print("Hey you have an OS Error ")
finally:
    print("I always run")

# The above block xecutes properrlly
    ## Now lets induce an error
try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a typeerror")
except OSError:
    print("Hey you have an OS Error ")
    print("All other exception!")
finally:
    print("I always run")
## With finally statement the except block along with finally will run
   
    
## Example
def ask_for_int():
    try:
        result = int(input("Please provide number : "))
    except:
        print("Whoops! That is not a number")
    finally:
        print("End of try/except/finally")

ask_for_int()   ## >> Please provide number : 20
                    #End of try/except/finally

# Now if I give string as input
# >> Please provide number : word
#Whoops! That is not a number
#End of try/except/finally
 
# Lets write a while loop if wee provide a word input                   
def ask_for_int():
    while True:
    
        try:
            result = int(input("Please provide number : "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes, Thank you!")
            break
        finally:
            print("End of try/except/finally")
            print("If you provide wrong input I am going to ask you again")
            print("I will always run at the end")
ask_for_int()

## For input as number : 
#>>Please provide number : 20
#Yes, Thank you!
#End of try/except/finally
#I will always run at the end

# For input as string
# It runs in while loop
#>> Please provide numbe : q
#Whoops! That is not a number
#End of try/except/finally
#I will always run at the end


