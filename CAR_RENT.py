class Bookcar:

    def __init__(self,List_of_cars):
        self.car = List_of_cars
    
    def DisplayAvailablcar(self):
        print("CAR AVIALABLE IN GARAGE ARE: ")
        for car in self.car:
            print(" \t * "+ car)
    
    def Rentcar(self,CarModel):
        if CarModel in self.car:
            print(f"You have been booked {CarModel}. please keep it clean and safe")
            self.car.remove(CarModel)
            
        else:
            print("sorry, this carmodel is already booked! , try another car model")
            

    def returncar(self, CarModel):
        self.car.append(CarModel)
        print("thanks for using our rent car service")

class customer:
    def requestcar(self):
        self.car = input("Enter the car model you want to rent")
        return self.car
    
    def returncar(self):
        self.car = input("Enter the car Model to Return!")
        return self.car

if __name__ == "__main__":
    CarRentCompany = Bookcar(["BMW X4","GLS 460","NANO","TATA HARRIAR","BUGGATI","LAMBORGINI","FERARRI"]) 
    client = customer()

    welcomemsg = '''
    ==== WELCOME TO DUBAI CAR RENT SERVICE PVT LTD ====
    '''
    print(welcomemsg)


while(True):

    options = '''
     PLEASE CHOOSE OPTIONS:

    1. SHOW AVIALABLE CARS  

    2. REQUEST A CAR FOR RENT

    3. RETURN CAR

    4. EXIT
    '''
    print(options)

    a = int(input("Enter a choise: "))

    if a == 1:
     CarRentCompany.DisplayAvailablcar()

    elif a == 2:
     CarRentCompany.Rentcar(client.requestcar())

    elif a == 3:
     CarRentCompany.returncar(client.returncar())

    elif a == 4:
     print("thanks for visting our car rent service! have nice day")
     exit()

    else:
      print("invalid choise") 

