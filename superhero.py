class  Avenger :
   def __init__(self,n,a,g,s,w) -> None:
      self.name=n
      self.age=a
      self.gender=g
      self.superPower=s
      self.weapon=w
   def getinfo(self) :
      pass
      
   def get_info(self):
        return f"""
        Avenger Profile:

        Name:   {self.name}
        Age:    {self.age}
        Gender: {self.gender}
        
        Has {self.weapon} weapon and {self.superPower} super Power. 
        """ 

hero=['Captain America','Iron Man', 'Blac Widow','Hulk','Thor','Hawkeye']
suppower=['Super strength','Technology','superhuman','Unlimited Strength','super Energy','fighting skills as superpowers']
# let's create a ages and gender list randomly
ages = [110, 40, 35, 34, 10000, 30]
genders = ['M', 'M', 'F', 'M', 'M', 'M']
wepon=['hield', 'Armor', 'Batons', 'No Weapon for hulk', 'Hammer', 'Bow and Arrows']


avengers = []
for name, age, gender, power, weapon in zip(hero, ages, genders, suppower, wepon):
    avengers.append(
        Avenger(name, age, gender, power, weapon)
    )
# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.


for i in range(0,6) :
    print(avengers[i].get_info())

