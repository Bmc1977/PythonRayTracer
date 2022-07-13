import argparse
import importlib
from scene import Scene
from engine import RenderEngine
from multiprocessing import cpu_count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (without .py extension)")
    parser.add_argument("-p", "--processes", action="store", type=int, dest="processes", default=0, help="Number of processes (0=automatic)")
    args = parser.parse_args()

    if args.processes == 0:
        processCount = cpu_count()
    else:
        processCount = args.processes

    mod = importlib.import_module(args.scene)

    scene = Scene(mod.CAMERA, mod.OBJECTS, mod.LIGHTS, mod.WIDTH, mod.HEIGHT)
    engine = RenderEngine()

    with open("../{}".format(mod.RENDERED_IMG), "w") as imgFile:
        engine.render_multi_process(scene, processCount, imgFile)


if __name__ == '__main__':
    main()
