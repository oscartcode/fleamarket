"""
Object Oriented Programming in Python

while python is not intended to be a OOP
language, it supports it, therefore you can
use its capabilities in your favor.

brief concepts: 

a class is a blueprint to something you want
to model in a software, has to be an entity
such as, a thing, or a concept.

Cars for example are phisycal objects while
Bot could be a logical entity, a concept

python supports creations of classes

class classname:

"""


class Vehicle:
    def __init__(self, plates, color):
        self.plates = plates
        self.color = color

    def reassign_plates(self, new_plate):
        self.plates = new_plate

    def start_car(self):
        if not hasattr(self, 'status') or self.status == 'off':
            self.status = 'on'
            print('starting the car rum rum... yes i wrote rum rum...')
        else:
            print('car is already on, you wanna break it? ')

    def turn_off_car(self):
        if not hasattr(self, 'status') or self.status == 'on':
            self.status = 'off'
            print('turning off the car, the exhaust coughs...')
        else:
            print('car is already off, no effect')

    def check_out_the_car(self):
        print(f'the car has a nice shiny {self.color} color, and its plates are {self.plates}')
        if not hasattr(self, 'status'):
            print('we cannot know if it is on or off')
        else:
            print(f'the car is actually {self.status}')


def main():
    car = Vehicle('ABC 123', 'RED')
    car.check_out_the_car()
    car.start_car()
    car.start_car()
    car.turn_off_car()
    car.turn_off_car()
    car.reassign_plates("ASD 231")
    car.check_out_the_car()


if __name__ == '__main__':
    main()
