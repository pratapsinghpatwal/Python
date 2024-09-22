class Player :
  def __init__(self,fn,ln,dob):
    self.fname=fn
    self.lname=ln
    self.datebirth=dob

class Criketer (Player):
  def __init__(self,fn,ln,dob,cteam) :
    Player.__init__(self,fn,ln,dob)
    self.team=cteam
    self.scores=[]
  def addscore(self,score) :
      self.scores.append(score)
  def averagescore(self) :
    return  (sum(self.scores)/len(self.scores))

virat=Criketer('virat','kohali',1997,'India')
virat.addscore(100)
virat.addscore(80)
virat.addscore(70)
avgscor=virat.averagescore()
print("score  ",virat.scores)
print("Average score is ", avgscor)



