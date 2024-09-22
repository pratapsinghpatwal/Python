class criketer :
  def __init__ (self,fn,ln,by,t) :
    self.firstname=fn
    self.lastname =ln
    self.birthyear =by
    self.team =t
    self.scores=[]


virat=criketer('virat','kohali',1988,'india')
virat.scores.append(100)
virat.scores.append(0)
virat.scores.append(10)
virat.scores.append(110)

print(virat.firstname + ' ' + virat.lastname)
print(virat.scores)
print('Average score of Virat ' , (sum(virat.scores)/len(virat.scores)))


david=criketer('david','warner',1988,'india')
david.scores.append(140)
david.scores.append(37)
david.scores.append(110)
david.scores.append(114)

print(david.firstname + ' ' + david.lastname)
print(david.scores)
print('Average score of david  ' , (sum(david.scores)/len(david.scores)))