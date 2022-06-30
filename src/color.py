from vector import Vector3


class Color(Vector3):
    """
    Stores color as RGB triplets. An alias for vector
    """

    @classmethod
    def from_hex(self, hexColor="#000000"):
        r = int(hexColor[1:3], 16) / 255.0
        g = int(hexColor[3:5], 16) / 255.0
        b = int(hexColor[5:7], 16) / 255.0
        return Color(r, g, b)
