print('welcome to the tip calculator')
totalBill = input('what was the total bill? $')

numOfPeople = input('how many people to split the bill?')

tipPercentage = input('what percentage tip would you like to give? 10, 12 or 15?')


result = (float(totalBill) / float(numOfPeople))+ float(totalBill)/float(numOfPeople)*(float(tipPercentage)/100.00)
print("You're Total bill is " + str(round(result, 2))) 

