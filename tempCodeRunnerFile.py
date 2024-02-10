    if keys[K_LEFT] is True:
                    self.move_x -= self.vel
                    print("moved left: ", self.move_x)
                if keys[K_RIGHT] is True:
                    self.move_x += self.vel
                    print("moved right: ",self.move_x)
                if keys[K_DOWN] is True:
                    self.move_y -= self.vel
                    print("moved down: ", self.move_y)
                if keys[K_UP] is True:
                    self.move_y += self.vel
                    print("moved up: ", self.move_y)