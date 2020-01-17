import time
from random import randint
import logging
import os
from datetime import datetime


logging.basicConfig(
    level=logging.INFO, filename='machine.log', filemode='w', format='')


def log(f):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        ret = f(*args, **kwargs)
        delta = datetime.now() - start_time
        s = delta.seconds
        ms = delta.microseconds / 1000
        exec_time = ms if not s else s + ms / 1000
        unit = "ms" if not s else "s"
        logging.info('({}) Running: {}{:10}[ exec-time = {:.3f} {} ]'.format(
            os.getlogin(), f.__name__, '', exec_time, unit))
        return ret
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
