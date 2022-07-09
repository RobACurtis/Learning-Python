# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
# print to the terminal, which day of the week do you want to count?
# then give a list of days with the indexes
# if they type exit, then quit the program
# if they type a valid number then ask them what month
# then what year
# when they type the year, there needs to be an equation to count the number of days in the month of that year


import calendar

def main():

  daysinmonth = 0
  dayoftheweek = 0
  month = 0
  year = 0

  dayoftheweek = input("Which day of the week do you want to count? \n 0: Monday \n 1: Tuesday \n 2: Wednesday \n 3: Thursday \n 4: Friday \n 5: Saturday \n 6: Sunday \n or 'exit' to quit \n? " )
  if dayoftheweek == 'exit':
      return
  elif dayoftheweek.isnumeric() == False:
    print("Value must be a positive integer!")
    main()

  month = input("Enter Month: ")
  if month == 'exit':
    return
  elif month.isnumeric() == False:
    print("Value must be a positive integer!")
    main()

  year = input("Enter Year: ")
  if year == 'exit':
    return
  elif year.isnumeric() == False:
    print("Value must be a positive integer!")
    main()

  c = calendar.monthcalendar(int(year), int(month))
  for i in c:
    if i[int(dayoftheweek)] != 0:
      daysinmonth +=1



  print('There are '+ str(daysinmonth) + ' days in the month of ' + str(month) +', ' + str(year))
  main()
if __name__ == "__main__":
  main()
