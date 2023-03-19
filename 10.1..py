class Elevator:
    def init(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            self.floor_up(floor)
        elif floor < self.current_floor:
            self.floor_down(floor)

    def floor_up(self, floor):
        while self.current_floor < floor and self.current_floor < self.top_floor:
            self.current_floor += 1
            print("Elevator on {} floor".format(self.current_floor))

    def floor_down(self, floor):
        while self.current_floor > floor and self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print("Elevator on {} floor".format(self.current_floor))
