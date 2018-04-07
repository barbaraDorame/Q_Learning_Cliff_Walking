'''

'''
import random
from collections import defaultdict


class Clifford:
    def __init__(self):
        self.x, self.y = 0, 0

    actions = ["up", "down", "right", "left"]

    def terminal(self):
        if self.x == 11 and self.y == 0:
            return True
        else:
            return False

    def transition(self, action):
        if action == "up":
            self.y += 1
        elif action == "down":
            self.y -= 1
        elif action == "right":
            self.x += 1
        else:
            self.x -= 1

        if self.x > 11:
            self.x = 11
        elif self.y > 3:
            self.y = 3
        elif self.x < 0:
            self.x = 0
        elif self.y < 0:
            self.y = 0

        return -100 if 11 > self.x > 0 and self.y == 0 else -1


def Coo_Learning(episodes, gamma):
    q = defaultdict(float)

    for ep in range(episodes):
        cliff = Clifford()
        s = cliff.x, cliff.y
        while not cliff.terminal():
            a = random.choice(cliff.actions) if random.random() < 0.1 else max(
                cliff.actions, key=lambda x: q[(s, x)])
            r = cliff.transition(a)
            primas = cliff.x, cliff.y
            q[(s, a)] = q[(s, a)] + 0.5 * (r + gamma*max(q[(primas, a)] for a
                                                         in cliff.actions)
                                           - q[(s, a)])
            s = primas
    return [((x, y), max(cliff.actions, key=lambda a: q[((x, y), a)]))
            for x in range(12) for y in range(4)]


print(Coo_Learning(10000, 0.7))
