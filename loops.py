import csv
import copy

lst = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for i in lst:
    print("Item {} is Type of {}.".format(i,type(i)))
    
car_dic={
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key,value in car_dic.items():
    print("{} {} ".format(key,type(value) ))
    
car_lst=[];

with open('cars.csv') as csvFile:
    csvReader=csv.reader(csvFile, delimiter=',')
    lines=0
    for row in csvReader:
        if lines==0:
              print(f'Column names are: {", ".join(row)}')  
              lines+=1
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            car = copy.deepcopy(car_dic)  
            car["vin"] = row[0]  
            car["make"] = row[1]  
            car["model"] = row[2]  
            car["year"] = row[3]  
            car["range"] = row[4]  
            car["topSpeed"] = row[5]  
            car["zeroSixty"] = row[6]  
            car["mileage"] = row[7]  
            car_lst.append(car)  
            lines += 1  
    print(f'Processed {lines} lines.')
    