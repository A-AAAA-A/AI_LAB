class Enviroment:
    def __init__(self):
        self.rooms = ["Dirty", "Dirty", "Dirty"]
    def getstatus(self, roomnumber):
        return self.rooms[roomnumber]
    def setstatus(self,roomnumber):
        self.rooms[roomnumber] = "Clean"

class Agent:
    def __init__(self):
        pass
    def act(self,status):
        if(status == "Dirty"):
            return "The room is being cleaned"
        else:
            return "The room has already been cleaned"

def runAgent(agent,enviroment,room):
    status = enviroment.getstatus(room)
    if(status == "Dirty"):
        enviroment.setstatus(room)
    action = agent.act(status)
    print(f"Perceived = {status} \t Action = {action}")

env = Enviroment()
ag = Agent()
runAgent(ag,env,1)
runAgent(ag,env,2)
runAgent(ag,env,2)
