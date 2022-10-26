class Ship:
    def __init__(self):
        self.direction = "STOP" 
        self.xnave=450 
        self.ynave=800
    
    def move(self):
        if self.direction == "LEFT": 
            self.xnave -= 7  
        elif self.direction == "RIGHT": 
            self.xnave += 7
        elif self.direction == "STOP": 
            pass    