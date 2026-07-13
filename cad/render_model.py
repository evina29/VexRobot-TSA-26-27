# Renders cad/collector_bot.stl to an SVG image for the README.
# Run with: python cad/render_model.py
# Output: docs/model_render.svg

import math
import struct
import os

HERE = os.path.dirname(os.path.abspath(__file__))
STL = os.path.join(HERE, "collector_bot.stl")
OUT = os.path.join(HERE, "..", "docs", "model_render.svg")

YAW = 35        # turn the robot so the front and one side are visible
PITCH = -62     # tilt the camera down onto the robot
WIDTH, HEIGHT = 900, 760


def read_stl(path):
    with open(path, "rb") as f:
        data = f.read()
    count = struct.unpack("<I", data[80:84])[0]
    tris = []
    for i in range(count):
        o = 84 + i * 50
        pts = []
        for j in range(3):
            pts.append(struct.unpack("<3f", data[o + 12 + j * 12:
                                               o + 24 + j * 12]))
        tris.append(pts)
    return tris


def transform(p):
    x, y, z = p
    a = math.radians(YAW)
    x, y = x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a)
    b = math.radians(PITCH)
    y, z = y * math.cos(b) - z * math.sin(b), y * math.sin(b) + z * math.cos(b)
    return (x, y, z)


def main():
    tris = [[transform(p) for p in t] for t in read_stl(STL)]

    xs = [p[0] for t in tris for p in t]
    zs = [p[2] for t in tris for p in t]
    scale = min((WIDTH - 60) / (max(xs) - min(xs)),
                (HEIGHT - 60) / (max(zs) - min(zs)))

    def screen(p):
        sx = 30 + (p[0] - min(xs)) * scale
        sy = HEIGHT - 30 - (p[2] - min(zs)) * scale
        return sx, sy

    light = (0.35, -0.65, 0.67)
    tris.sort(key=lambda t: -(t[0][1] + t[1][1] + t[2][1]) / 3)

    polys = []
    for a, b, c in tris:
        u = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
        v = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
        n = (u[1] * v[2] - u[2] * v[1],
             u[2] * v[0] - u[0] * v[2],
             u[0] * v[1] - u[1] * v[0])
        ln = math.sqrt(n[0] ** 2 + n[1] ** 2 + n[2] ** 2) or 1.0
        n = (n[0] / ln, n[1] / ln, n[2] / ln)
        if n[1] > 0:
            n = (-n[0], -n[1], -n[2])
        i = max(0.18, -(n[0] * light[0] + n[1] * light[1] + n[2] * light[2]))
        shade = int(60 + i * 175)
        pts = " ".join("%.1f,%.1f" % screen(p) for p in (a, b, c))
        polys.append('<polygon points="%s" fill="rgb(%d,%d,%d)"/>'
                     % (pts, shade, shade, shade))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" '
                'viewBox="0 0 %d %d">\n' % (WIDTH, HEIGHT))
        f.write('<rect width="%d" height="%d" fill="white"/>\n'
                % (WIDTH, HEIGHT))
        f.write("\n".join(polys))
        f.write("\n</svg>\n")
    print("wrote", os.path.normpath(OUT), "with", len(polys), "polygons")


if __name__ == "__main__":
    main()
