class Cat:
    
    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time
    
    def __str__(self):
        return "CAT: name: {} - preferred_food: {} - meal_time: {}".format(self.name, self.preferred_food, self.meal_time)
    
    def eats_at(self):
        if self.meal_time == 0:
            return "12 AM"
        elif self.meal_time < 12:
            return "{} AM".format(self.meal_time)
        elif self.meal_time == 12:
            return "{} PM".format(self.meal_time)
        elif self.meal_time > 23:
            return "Please use the 24 hour clock."
        else:
            pm = self.meal_time - 12
            return "{} PM".format(pm)

    def meow(self):
        return "My name is {} and I eat {} at {}.".format(self.name, self.preferred_food, self.eats_at())


mojo = Cat('Mojo', 'Temptations', 1)

luna = Cat('Luna', 'Wet food', 16)

print(mojo)
print(luna)
print(luna.eats_at())
print(mojo.eats_at())
print(luna.meow())
print(mojo.meow())