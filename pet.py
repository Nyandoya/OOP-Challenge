class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting with mid-range values
        self.energy = 5
        self.happiness = 5
        self.tricks = []  # For storing learned tricks
    
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy increased!")
    
    def play(self):
        if self.energy >= 2:  # Only play if there's enough energy
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play. Maybe time for a nap?")
    
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10 ({'Full' if self.hunger == 0 else 'Very hungry' if self.hunger == 10 else 'Okay'})")
        print(f"Energy: {self.energy}/10 ({'Tired' if self.energy == 0 else 'Fully rested' if self.energy == 10 else 'Okay'})")
        print(f"Happiness: {self.happiness}/10 ({'Miserable' if self.happiness == 0 else 'Ecstatic' if self.happiness == 10 else 'Content'})")
        
        if self.hunger >= 8:
            print(f"Warning: {self.name} is very hungry!")
        if self.energy <= 2:
            print(f"Warning: {self.name} is very tired!")
        if self.happiness <= 2:
            print(f"Warning: {self.name} is very unhappy!")
    
    # Bonus methods
    def train(self, trick):
        if self.energy >= 3:  # Training requires energy
            self.energy -= 1
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to learn new tricks right now.")
            print(f"{self.name} hasn't learned any tricks yet.")
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")