class Enviroment:
  def __init__(self,goal):
    self.goal = goal

  def get_goal(self):
    return self.goal

class Agent:
  def __init__(self):
    pass

  def act(self,currpos,goal):
    if currpos < goal:
      return 1
    elif currpos > goal:
      return -1
    else:
      return 0

def runAgent(enviroment,agent):
  goal = enviroment.get_goal()
  currpos = 0
  count = 0
  while (True):
    if(currpos == goal):
      print ("Goal Reached")
      print (f"Number of Steps = {count}")
      return
    action = agent.act(currpos,goal)
    count = count + 1
    currpos = currpos + action
    print(f"Current Position = {currpos}")

env = Enviroment(15)
ag = Agent()
runAgent(env,ag)
