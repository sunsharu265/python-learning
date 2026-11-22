class Mobilephone:
  def __init__(self,brand,model,battery=100):
    self.brand = brand
    self.model = model
    self.battery = battery

  def show_details(self):
    print("Brand:",self.brand)
    print("Moduel:",self.model)
    print ("Battery:",self.battery,"%")
  
  def use (self,minutes):
    self.battery -=minutes//10
    if self.battery<0:
       self.battery=0


def main():
    mobile1= Mobilephone ("vivo","v50")
    mobile2= Mobilephone ("vivo","v60")

    mobile1.show_details()
    mobile2.show_details()

if __name__ =="__main__":
   main()
   