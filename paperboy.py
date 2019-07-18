class Paperboy:

    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.earnings = 0
        self.base_quota = 50

    def __str__(self):
        return "PAPERBOY: name: {} - experience: {} - earnings {}.".format(self.name, self.experience, self.earnings)

    def quota(self):
        return self.base_quota
    
    def deliver(self, start_address, end_address):
        deliveries = abs(end_address - start_address) + 1
        self.experience += deliveries
        if deliveries > self.base_quota:
            self.earnings += self.base_quota * 0.25
            self.earnings += (deliveries - self.base_quota) * 0.5
        else:
            self.earnings += deliveries * 0.25
            self.earnings -= 2
        self.base_quota += round(self.experience/2)
        return self.earnings

    def report(self):
        return "Hello! I'm {}, I've delivered {} papers and I've earned ${} so far!".format(self.name, self.experience, self.earnings)

tommy = Paperboy("Tommy")
print(tommy.quota()) #  50
print(tommy.deliver(101, 160)) # 17.5
print(tommy.earnings) # 17.5
print(tommy.report()) # "I'm Tommy, I've delivered 60 papers and I've earned $17.5 so far!"

print(tommy.quota()) # 80
print(tommy.deliver(1, 75)) # 16.75
print(tommy.earnings) # 34.25
print(tommy.report()) # "I'm Tommy, I've been delivered 135 papers and I've earned $34.25 so far!"