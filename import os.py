import os 
import csv 

a=os.getcwd()
os.path.join("list.csv", a)
hosts=[["James", "Nick"],["LAdo", "Dato", "Gio"], ["King", "Boby"], ["Mister name", "kristina"], ["Day", "Mayhem"]]

try:
    with open("list.csv", "w")as file:
        writer=csv.writer(file)
        writer.writerows(hosts)

except IOError:
    print("Operation failed")