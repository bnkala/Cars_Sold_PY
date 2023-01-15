if __name__=="__main__":
    cars = []
    numCars = 0
    num =1
    totCars =0
    highNum =0
    high =0
    i = 0
    
    for i in range(14):
        numCars = int(input("Enter number of Car(s) sold: "))
        cars.append(numCars)
        if(cars[i]> high):
            high = cars[i]
            highNum = num
        
        num+=1
        totCars += cars[i]
    
    print("The total number of Cars sold: {}".format(totCars))
    print("The Salesperson with max. number of Slaes: {}".format(highNum))