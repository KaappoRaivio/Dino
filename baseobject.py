from color import colors

class BaseObject:
    """DON'T INSTANTIATE FROM THIS CLASS"""
    def __init__(self, pos_x=0, pos_y=0, sprite=None, speed_x=0, speed_y=0, is_movable=False, has_collision_logic=False):
        self.spr = sprite
        self.spr.draw(pos_x, pos_y)


        self.is_movable = is_movable
        self.has_collision_logic = has_collision_logic

    @property
    def pos_x(self):
        return self.spr.pos_x

    @property
    def pos_y(self):
        return self.spr.pos_y


    def updateMoving(self):
        if not self.is_movable:
            return

        self.spr.move(self.speed_x, self.speed_y)

    def delIfOverTheEdge(self):
        if self.pos_x < -self.spr.dim_y: # Over the screen border

            print(f"Deleted object: {self.spr}")
            self.delete()


    def reportCollision(self):
        if not self.has_collision_logic:
            return

        if not self.spr.drawn:
            return

        for coordinate, char in self.spr.getCurrentScreenBuffer().items():

            coordinate = (coordinate[0] + self.spr.pos_x, coordinate[1] + self.pos_y) #convertabsolute

            if char == self.spr.getTransparentChar():
                continue
            else:
                if coordinate not in self.spr.screenPrinter.collision_matrix:
                    self.spr.screenPrinter.collision_matrix.append(coordinate)
