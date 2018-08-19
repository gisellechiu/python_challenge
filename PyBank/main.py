
import csv

with open('budget.csv') as file:
    reader = csv.reader(file)

  
    next(reader) 
    revenue = []
    date = []
    revchange = []

    
    for row in reader:

        revenue.append(float(row[1]))
        date.append(row[0])

   
    for i in range(1,len(revenue)):
        revchange.append(revenue[i] - revenue[i-1])   
        avgrevchange = sum(revchange)/len(revchange)

        maxrev = max(revchange)

        minrev = min(revchange)

        maxdate = str(date[revchange.index(max(revchange))])
        mindate = str(date[revchange.index(min(revchange))])



    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))
    print("Avereage Revenue Change: $", round(avgrevchange))
    print("Greatest Increase in Revenue:", maxdate,"($", maxrev,")")
    print("Greatest Decrease in Revenue:", mindate,"($", minrev,")")