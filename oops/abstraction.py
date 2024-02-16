from abc import ABC,abstractmethod

class car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class swift(car):
    def start(self):
        print("swift starts")

    def accelerate(self):
        print("swift accelerate")
    
    def stop(self):
        print("swift stop")

obj=swift()
obj.start()