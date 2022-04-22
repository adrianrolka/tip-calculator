print('Welcome to the tip calculator.')
total = input('What was the total bill? $')
people = input("How many people to split the bill? ")
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
while int(percentage) not in [10, 12, 15]:
  print("Incorrect precentage")
  break
else:
  tip = (int(percentage)/int(total)*100)/int(people)
  totaldevided = int(total)/int(people)
  print("Each person should pay: $" + str(tip + totaldevided))
  