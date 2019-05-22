#Calc for determining state population as height in mm with Cali as 175mm
#2015 pop estimates from http://state.1keydata.com/state-population.php
caliPop = 39144818 #39,144,818

def calc():
    maxHeight = int (input ("Maximum height in mm:  "))
    stateName = input ("State:  ")
    statePop = int (input ("State Population:  "))
    
    stateHeight = ((maxHeight*statePop)/caliPop)
    
    print (stateName, "height is", stateHeight, "mm")
    print ("--------------------------------------------")
    print ("\n")

while True:
    calc()
