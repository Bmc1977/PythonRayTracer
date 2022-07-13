from math import sqrt


class Sphere:
    """
    Sphere is the only 3D shape implemented. Has radius, center, and material.
    """

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersects(self, ray):
        """
        Checks if ray intersects this sphere. Returns distance to intersection or None if no intersection.
        """
        sphere_to_ray = ray.origin - self.center
        b = 2 * ray.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - self.radius ** 2
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist

        return None

    def normal(self, surface_point):
        """
        Returns surface normal to the point on sphere's surface.
        """
        return (surface_point - self.center).normalize()
