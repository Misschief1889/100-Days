print('Welcome to the tip calculator!\n What was the total bill? ')

check = float(input())

print('How many people to split the bill? ')
people = float(input())

print('What percentage of tip would you like to give? 10, 12, or 15? ')

tip_percent = float(input())

if tip_percent == 10:
  tip_total = 1.10
elif tip_percent == 12:
  tip_total = 1.12
elif tip_percent == 15:
  tip_total = 1.15
else:
  print('Please enter a valid tip amount.')


payment = ( check / people ) * tip_total 

rounded_payment = "{:.2f}".format(payment)

print('Each person should pay: ' + str(rounded_payment))
