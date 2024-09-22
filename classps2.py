import datetime

class criketer :
  def __init__ (self,fn,ln,by,t) :
    self.firstname=fn
    self.lastname =ln
    self.birthyear =by
    self.team =t
    self.scores=[]
  
  def getage(self) :
      now=datetime.datetime.now()
      return now.year-self.birthyear

  def addscore(self,s) :
      self.scores.append(s)
  def getaverage(self) :
    return (sum(self.scores)/len(self.scores))
  def __lt__(self,other) :
      vs= self.getaverage()
      os= other.getaverage() 
      return vs<os
      


  def __str__(self) :
    return (f'{self.firstname} {self.lastname}, dob {self.birthyear} team from {self.team}, scored  {self.scores}')
  
virat=criketer('Virat','Kohli',1988,'india')

virat.addscore(100)
virat.addscore(80)
virat.addscore(180)
virat.addscore(70)




print('The age of virat kohli is  ', virat.getage())
print('The score of virat is  ',virat.scores)
print('Average score of virate is  ' ,virat.getaverage())
print(virat)


david=criketer('Virat','Kohli',1988,'india')

david.addscore(100)
david.addscore(80)
david.addscore(90)
david.addscore(70)




print('The age of virat kohli is  ', david.getage())
print('The score of virat is  ',david.scores)
print('Average score of virate is  ' ,david.getaverage())
print(david)

if (virat < david) :
   print('virat score is less then david score ')
else :
   print('virat score is not less then david score ')







