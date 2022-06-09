class User(object): 
  def __init__(self,name,age): 
    self.name = name 
    self.age = age 
  
  def SetName(self,name): 
    self.name = name 
  
  def SetAge(self,age): 
    self.age = age 
  
  def GetName(self): 
    return self.name 
  
  def GetAge(self): 
    return self.age 
  
u = User("no",15) 
u.SetName("li") 
print(u.name) 

# self is like the instance in the method , so method is the instance method, the first argument is always self , it shows which instance will use this method 
# in the init is like to add argument to the class
hahahaha
