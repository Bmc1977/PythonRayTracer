import math
from random import randint
from color import Color
from light import Light
from material import Material, CheckeredMaterial
from point import Point
from sphere import Sphere
from vector import Vector3

WIDTH, HEIGHT = 1200, 800
RENDERED_IMG = "two-balls.ppm"
CAMERA = Vector3(0, -0.35, -1)
OBJECTS = [Sphere(Point(0.75, -0.05, 1), 0.6, Material(Color.from_hex("#0000FF"), diffuse=0.2)),
           Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Color.from_hex("#803980"), reflection=.7, diffuse=0.2)),
           Sphere(Point(0, 10000.5, 1), 10000.0, CheckeredMaterial(color1=Color.from_hex("#420500"), color2=Color.from_hex("#e6b87d"), ambient=0.01, reflection=0.55)),
           Sphere(Point(0, -10001.5, 1), 10000.0, CheckeredMaterial(color1=Color.from_hex("#420500"), color2=Color.from_hex("#e6b87d"), ambient=0.01, reflection=0.55))]
LIGHTS = [Light(Point(1.5, -0.5, -10.0), Color.from_hex("#FFFFFF")),
          Light(Point(-0.5, -10.5, 0.0), Color.from_hex("#E6E6E6")),
          Light(Point(0.0, 1, -.025), Color.from_hex("#02FFFF"))]
