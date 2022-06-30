from color import Color
from vector import Vector3
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine


def main():
    WIDTH, HEIGHT = 320, 200

    camera = Vector3(0, 0, -1.0)
    objects = [Sphere(Point(0, 0, 0), 0.5, Color.from_hex("#FF0000"))]
    scene = Scene(camera, objects, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("../test.ppm", "w") as imgFile:
        image.write_ppm(imgFile)


if __name__ == '__main__':
    main()
