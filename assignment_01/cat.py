class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Hello I am {self.name}!")
    
    def greet_other(self, other):
        self.speak()
        print(f"I see you are also a cool fluffy kitty {other.name}, let’s together purr at the human, so that they shall give us food")