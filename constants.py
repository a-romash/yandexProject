from random import randint
from mainMenu import load_image
import pygame

SIZE = WIDTH, HEIGHT = 1280, 720
FPS = 60
# 0 - начальное меню
# 1 - уже сама игра
# 2 - меню после смерти
UI_CONDITION = 0
IMAGE = randint(1, 2)  # константа конкретно на одну сессию, значение может отличаться при разных запусках программы
TITLE = "BATTLE TRIAL"
