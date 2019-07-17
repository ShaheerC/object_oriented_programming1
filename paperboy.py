class PaperBoy:

    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.earnings = 0

    def __str__(self):
        return "PAPERBOY: name: {} - experience: {} - earnings {}.".format(self.name, self.experience, self.earnings)

    def quota(self):
        base_quota = 50
        return (self.experience / 2 + base_quota)
    
    def deliver(self, start_address, end_address):
        regular_rate = 0.25
        special_rate = 0.50
        delivery_earning = 0 
        self.experience = end_address - start_address
        if self.experience < self.quota():
            delivery_earning = self.experience * regular_rate - 2.00
            return delivery_earning
        elif self.experience > self.quota():
            delivery_earning = (self.experience - self.quota() * special_rate) + self.quota() * regular_rate
            return delivery_earning

#add variable for earning specific delivery only
#update overall self.earnings value
#add variable for experience specific delivery and update overall self.experience value

#-------
#variable for regular rate vs special rate
#if total deliveries that day < quota = regular rate
#elif total deliveries > quota = total deliveries - quota = * special rate + base quota * regular rate

    # def report(self):
    #     return "Hello! I'm {}, I've delivered {} papers and I've earned ${:2f} so far!".format(self.name, self.experience, self.earnings)

bob = PaperBoy('bob')
print(bob)
# print(bob.deliver(101, 160))
print(bob.deliver(1, 75))
print(bob.deliver(100, 150))
print(bob)