import random
class Node:
    def __init__(self, edges=[]):
        self.edges = edges
        random.seed()
    def execute(self, function, world):
        if function == None:
            return None
        return function()
    def set_seed(self, seed):
        random.seed(seed)
        
    def select_next(self):
        total = self.__get_weights()
        r = random.uniform(0, total)
        print(r)
        total = 0
        for n in self.edges:
            total += n.weight
            if r <= total:
                return n.node
        return None

    def __get_weights(self):
        total = 0
        for n in self.edges:
            total += n.weight
        return total






