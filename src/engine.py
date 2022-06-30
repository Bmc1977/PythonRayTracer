from image import Image
from point import Point
from ray import Ray
from color import Color


class RenderEngine:
    """
    Renders 3D objects into 2D objects using ray tracing.
    """

    def render(self, scene):
        width = scene.width
        height = scene.height

        aspectratio = float(width) / height

        x0 = -1.0
        x1 = 1.0
        xstep = (x1 - x0) / (width - 1)

        y0 = -1.0 / aspectratio
        y1 = 1.0 / aspectratio
        ystep = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for j in range(height):
            y = y0 + (j * ystep)
            for i in range(width):
                x = x0 + (i * xstep)
                ray = Ray(camera, Point(x, y) - camera)
                pixels.setPixel(i, j, self.rayTrace(ray, scene))
            print("{:3.0f}%".format(float(j)/float(height) * 100))
        return pixels

    def rayTrace(self, ray, scene):
        color = Color(0, 0, 0)
        #Find the nearest object hit by the ray
        distHit, objHit = self.findNearest(ray, scene)
        if objHit is None:
            return color
        hitPos = ray.origin + ray.direction * distHit
        hitNormal = objHit.normal(hitPos)
        color += self.colorAt(objHit, hitPos, hitNormal, scene)
        return color

    def findNearest(self, ray, scene):
        distMin = None
        objHit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (objHit is None or dist < distMin):
                distMin = dist
                objHit = obj
        return distMin, objHit

    def colorAt(self, objHit, hitPos, normal, scene):
        material = objHit.material
        objColor = material.colorAt(hitPos)
        toCam = scene.camera - hitPos
        specularK = 50
        color = material.ambient * Color.from_hex("#000000")
        #Light calculations
        for light in scene.lights:
            toLight = Ray(hitPos, light.position - hitPos)
            #Diffuse shading
            color += objColor * material.diffuse * max(normal.dot(toLight.direction), 0)
            #Specular shading
            halfVector = (toLight.direction + toCam).normalize()
            color += light.color * material.specular * max(normal.dot(halfVector), 0) ** specularK
        return color
