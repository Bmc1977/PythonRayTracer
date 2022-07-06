import argparse
import importlib
from scene import Scene
from engine import RenderEngine


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (without .py extension)")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)

    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    with open("../{}".format(mod.RENDERED_IMG), "w") as imgFile:
        image.write_ppm(imgFile)


if __name__ == '__main__':
    main()
