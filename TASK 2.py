class simplereflexagent:
    def __init__(self, temp)
        self.desired_temp = temp

    def percieve(self):
        return int(input("Enter current temperature"))
    
    def act(self, temp):
        if temp > self.desired_temp:
            