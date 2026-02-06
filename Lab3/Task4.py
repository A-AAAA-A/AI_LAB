class Enviroment:
  def __init__(self,costA,timeA,costB,timeB):
    self.costA = costA
    self.timeA = timeA
    self.costB = costB
    self.timeB = timeB

  def getinfo(self):
    return self.costA,self.timeA,self.costB,self.timeB

class Agent:
  def __init__(self,tweight,cweight):
    self.tweight = tweight
    self.cweight = cweight
  def act(self,costA,timeA,costB,timeB):
    if (costA*self.cweight + timeA*self.tweight) < (costB*self.cweight + timeB*self.tweight):
      return (costA*self.cweight + timeA*self.tweight) , (costB*self.cweight + timeB*self.tweight), "Option A is perfered"
    else:
      return (costA*self.cweight + timeA*self.tweight) , (costB*self.cweight + timeB*self.tweight), "Option B is perfered"

def runAgent(enviroment,agent):
  print ("Lower utility rating is beter")
  costA,timeA,costB,timeB = enviroment.getinfo()
  A,B,decision = agent.act(costA,timeA,costB,timeB)
  print (f"Utility of A: {A} \nUtility of B: {B} \nDecision: {decision}")

env = Enviroment(4,2,2,3.5)
ag = Agent(0.7,0.4)
runAgent(env,ag)
