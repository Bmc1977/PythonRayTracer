from color import Color
from vector import Vector3
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("imageout", help="Path to rendered image")
    args = parser.parse_args()
    WIDTH, HEIGHT = 320, 200

    camera = Vector3(0, 0, -1.0)
    objects = [Sphere(Point(0, 0, 0), 0.5, Material(Color.from_hex("#FF0000")))]
    lights = [Light(Point(1.5, -0.5, -10.0), Color.from_hex("#FFFFFF"))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("../{}".format(args.imageout), "w") as imgFile:
        image.write_ppm(imgFile)


if __name__ == '__main__':
    main()
