class ModelBasedReflexAgent:
    def __init__(self, threshold=22):
        self.threshold = threshold 
        self.previous_action = None  

    def perceive_environment(self, current_temperature):
        return current_temperature

    def decide_action(self, current_temperature):
        if current_temperature < self.threshold:
            if self.previous_action != "Turn Heater On":
                self.previous_action = "Turn Heater On"
                return "Turn Heater On"
        elif current_temperature > self.threshold:
            if self.previous_action != "Turn Heater Off":
                self.previous_action = "Turn Heater Off"
                return "Turn Heater Off"
        return "Do Nothing"

    def act(self, current_temperature):
        action = self.decide_action(current_temperature)
        print(f"Current Temperature: {current_temperature}°C -> Action: {action}")
        return action

if __name__ == "__main__":
    agent = ModelBasedReflexAgent(threshold=22)
    temperatures = [20, 21, 22, 23, 24, 22, 21, 20, 19, 23, 24, 22]
    
    for temp in temperatures:
        agent.act(temp)

            
