class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def printinfo(self):
    print("名前:", self.name)
    print("年齢:", self.age)

human = Human("侍花子", 20)

human.printinfo()