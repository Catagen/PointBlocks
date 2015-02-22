import pygame, random
from tileC import Tile

pygame.mixer.init()


class Character(pygame.Rect):

    width, height = 45, 45
    List = []
    vel = 3

    def __init__(self, x, y):

        self.tx, self.ty = None, None
        pygame.Rect.__init__(self, x, y, Character.width, Character.height)

    def __str__(self):
        return str(self.get_number())

    def set_target(self, next_tile): #sets target for character movement function
        if self.tx == None and self.ty == None:
            self.tx = next_tile.x
            self.ty = next_tile.y

    def get_number(self):
        return ((self.x / self.width) + Tile.H) + ((self.y / self.height) * Tile.V)

    def get_tile(self):
        return Tile.get_tile(self.get_number())

    @staticmethod
    def on_point(): #returns true if both characters are on the meeting point
        on = 0
        for character in Character.List:
            if character.x == Tile.get_tile(Tile.meeting_point).x and character.y == Tile.get_tile(Tile.meeting_point).y:
                on += 1
        if on == len(Character.List):
            return True

    @staticmethod
    def update_characters(bill, bull): #looks for characters falling in holes or standing on the meeting point
        i = Tile.level
        for character in Character.List:
            if Tile.get_tile(character.get_number()).type == 'hole':
                if Tile.get_tile(character.get_number()).x == character.x and Tile.get_tile(character.get_number()).y == character.y:
                    Character.List.remove(character)

        if bill.x == Tile.get_tile(Tile.meeting_point).x and bill.y == Tile.get_tile(Tile.meeting_point).y and not Character.on_point():
            bill.status = 'happy'
            bull.status = 'sad'

        elif bull.x == Tile.get_tile(Tile.meeting_point).x and bull.y == Tile.get_tile(Tile.meeting_point).y and not Character.on_point():
            bull.status = 'happy'
            bill.status = 'sad'

        elif Character.on_point():
            bill.status = 'happy'
            bull.status = 'happy'
            Tile.freeze = True
            Tile.load_level(Tile.level + 1)
            i += 1

        else:
            bill.status = 'sad'
            bull.status = 'sad'


    @staticmethod
    def draw_characters(screen): #draws characters according to their status (sad/happy)
        for character in Character.List:
            if character.status == 'sad':
                if character.name == 'Bill':
                    character.sprite = pygame.image.load('images/bill.png')
                elif character.name == 'Bull':
                    character.sprite = pygame.image.load('images/bull.png')

            elif character.status == 'happy':
                if character.name == 'Bill':
                    character.sprite = pygame.image.load('images/bill_happy.png')
                elif character.name == 'Bull':
                    character.sprite = pygame.image.load('images/bull_happy.png')

            screen.blit(character.sprite, (character.x, character.y))



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Bill(Character):

    def __init__(self, x, y):

        Character.__init__(self, x, y)
        self.status = ''
        self.name = 'Bill'
        Character.List.append(self)

    def movement(self): #moves character according to velocity one frame at a time

        if self.tx != None and self.ty != None: # Target is set

            X = self.x - self.tx
            Y = self.y - self.ty

            if X < 0: # --->
                self.x += Character.vel
            elif X > 0: # <----
                self.x -= Character.vel

            if Y > 0: # up
                self.y -= Character.vel
            elif Y < 0: # down
                self.y += Character.vel

            if X == 0 and Y == 0:
                self.tx, self.ty = None, None



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Bull(Character):

    def __init__(self, x, y):

        Character.__init__(self, x, y)
        self.status = ''
        self.name = 'Bull'
        Character.List.append(self)

    def movement(self):

        if self.tx != None and self.ty != None: # Target is set

            X = self.x - self.tx
            Y = self.y - self.ty

            if X < 0: # --->
                self.x += Character.vel
            elif X > 0: # <----
                self.x -= Character.vel

            if Y > 0: # up
                self.y -= Character.vel
            elif Y < 0: # down
                self.y += Character.vel

            if X == 0 and Y == 0:
                self.tx, self.ty = None, None