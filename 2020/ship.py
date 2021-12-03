class Ship:
    waypoint = {'N':1,'S':0,'E':10,'W':0}
    pos = {'N':0,'S':0,'E':0,'W':0}
    def rotate(self,action,value):
        rotations = {
                'R':{'N':'E','E':'S','S':'W','W':'N'},
                'L':{'N':'W','E':'N','S':'E','W':'S'}}
        for i in range(value // 90):
            self.waypoint = {rotations[action][k]:v for k,v in self.waypoint.items()}
    def navigate(self,action,value):
        if action in ['N','S','E','W']:
            self.waypoint[action] += value
        elif action in ['L','R']:
            self.rotate(action,value)
        elif action == 'F':
            for direction in self.waypoint:
                self.pos[direction] += value * self.waypoint[direction]
        return
    def mdistance(self):
        return abs(self.pos['E'] - self.pos['W']) + abs(self.pos['N'] - self.pos['S'])

with open('aoc12-input.txt') as f:
    insts = [(inst[0:1],int(inst[1:])) for inst in f.read().strip().split('\n')]

ship = Ship()
for inst in insts:
    ship.navigate(*inst)
print(ship.mdistance())
