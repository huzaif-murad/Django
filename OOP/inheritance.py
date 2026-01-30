class Car:
    name="Huzaif"
    def __init__(self,type,brand):
        self.brand=brand
        self.type=type
    
    @staticmethod
    def start():
        print("Car started.")
    
    @staticmethod
    def stop():
        print("Car stopped.")

class Fortuner(Car):
    def __init__(self,price,type,brand):
        super().__init__(type,brand)
        super().start()
        print(super().name)
        self.price=price

        
fortuner=Fortuner(1000,"Electric","Toyota")

# print(fortuner.start())
# print(fortuner.stop())
# print(fortuner.type)
# print(fortuner.brand)
# print(fortuner.name)