class Player:
    
    def __init__(self):
        self.restart()
        # self.gold_coins = gold_coins
        # self.health_points = health_points
        # self.lives = lives
    
    def __str__(self):
        return "PLAYER: gold_coins: {} - health_points: {} - lives: {}".format(self.gold_coins, self.health_points, self.lives)

    def level_up(self):
        self.lives += 1

    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins / 10 == 1:
            self.level_up()
    
    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points <= 0: #Need more levels of if statements to make sure lives can't go below 0
            self.health_points = 10
            self.lives -= 1
            if self.lives <= 0:
                self.restart()

    def restart(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

crono = Player()
print (crono)

crono.collect_treasure()
crono.collect_treasure()
crono.collect_treasure()
crono.collect_treasure()
crono.collect_treasure()
crono.collect_treasure()
crono.collect_treasure()
crono.collect_treasure()
crono.collect_treasure()
crono.collect_treasure()
print(crono)

crono.do_battle(10)
print(crono)
crono.do_battle(10)
print(crono)
crono.do_battle(10)
print(crono)
crono.do_battle(10)
print(crono)
crono.do_battle(10)
print(crono)
crono.do_battle(10)
print(crono)