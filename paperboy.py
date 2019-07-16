class PaperBoy:

    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.earnings = 0

    def __str__(self):
        return "PAPERBOY: name: {} - experience: {} - earnings {}.".format(self.name, self.experience, self.earnings)

    def quota(self):
        return (self.experience / 2 + 50)
    
    def deliver(self, start_address, end_address):
        total_delivery = 50
        (self.experience = self.end_address - self.start_address + total_delivery)
        self.earnings += 0.25 * 50
        if self.experience





#Need about this much code for deliver function. needs to be more complicated.

    def report(self):
        return "Hello! I'm {}, I've delivered {} papers and I've earned ${:2f} so far!".format(self.name, self.experience, self.earnings)