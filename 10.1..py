Class elevator:
initialization of def(self, lower floor, upper floor):
self.bottom_floor = lower floor
self.top_floor = top floor
self.current_floor = lower floor

def go_to_floor(self, floor):
if floor > self.current_floor. current floor:
self.floor_up(floor)
top floor < self.current_floor_field:
self.floor_down(floor)

default floor_up(self, floor):
while self.current_floor < floor and self.current_floor < self.top_floor:
self.current_floor += 1
print ("Elevator on {} floor".format(self.current_floor))

def floor_down(self, floor):
while self.current_floor > floor and self.current_floor > self.bottom_floor:
self.current_floor -= 1
print ("Elevator on {} floor".format(self.current_floor))