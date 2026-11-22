class StudentMarkSheet:
   def __init__(self):
      self.Name = input ("Enter your Name:")
      self.Tamil = (input("Enter your tamil mark:"))
      self.English = (input("Enter your english mark:"))
      self.Maths = (input("Enter your maths mark:"))
   
   def calculate_total(self):
      return int(self.Tamil) + int(self.English) + int(self.Maths)
   
   def calculate_average(self):
      return self.calculate_total()/3

   
   def calculate_result(self):
      if int(self.Tamil)>=35 and int(self.English)>=35 and int(self.Maths)>=35:
         return "pass"
      else:
         return "fail"
      
   def show_details(self):
      print("Name:",self.Name)
      print("Tamil:",self.Tamil)
      print("English:",self.English)
      print("Maths:",self.Maths)
      print("Total:",self.calculate_total())
      print("Average:",self.calculate_average())
      print("Result:",self.calculate_result())


student1 = Student()
student1.show_details() 
