class Enviroment:
    def __init__(self,motion, intensity):
        self.motion = motion
        self.intensity = intensity

    def getmotion(self):
        return self.motion
    def getintensity(self):
        return self.intensity

class Agent:
    def __init__(self):
        pass
    def act(self,intensity,motion):
        if(intensity == "Bright"):
            return("Light is off")
        elif(intensity == "Dim" and motion == "Yes"):
            return("Light is on")
        else:
            return("Light is off")

def runAgent(agent,enviroment):
    motion = enviroment.getmotion()
    intensity = enviroment.getintensity()
    action = agent.act(intensity,motion)
    print(f"Perceived = (motion = {motion}, intensity = {intensity})\t Action = {action}")

env = Enviroment("Yes", "Bright")
ag = Agent()
runAgent(ag,env)
