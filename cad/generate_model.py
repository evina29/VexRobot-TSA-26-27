# Builds a simplified 3D model of the Collector Bot as an STL file.
# The real robot was designed and built physically from VEX parts,
# so this model is a recreation of it, made after the build.
# Run with: python cad/generate_model.py
# Output: cad/collector_bot.stl

import math
import struct
import os

TRIS = []


def rot_x(p, deg, pivot):
    # rotates a point around a line parallel to the x axis through pivot
    y, z = p[1] - pivot[1], p[2] - pivot[2]
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return (p[0], pivot[1] + y * c - z * s, pivot[2] + y * s + z * c)


def rot_z(p, deg, pivot):
    # rotates a point around a line parallel to the z axis through pivot
    x, y = p[0] - pivot[0], p[1] - pivot[1]
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return (pivot[0] + x * c - y * s, pivot[1] + x * s + y * c, p[2])


def add_quad(a, b, c, d):
    TRIS.append((a, b, c))
    TRIS.append((a, c, d))


def add_box(center, size, tilt_x=0, tilt_z=0, pivot=None):
    # axis aligned box, optionally tilted around the x or z axis
    cx, cy, cz = center
    hx, hy, hz = size[0] / 2, size[1] / 2, size[2] / 2
    if pivot is None:
        pivot = center
    v = []
    for dx in (-hx, hx):
        for dy in (-hy, hy):
            for dz in (-hz, hz):
                p = (cx + dx, cy + dy, cz + dz)
                if tilt_x:
                    p = rot_x(p, tilt_x, pivot)
                if tilt_z:
                    p = rot_z(p, tilt_z, pivot)
                v.append(p)
    add_quad(v[0], v[1], v[3], v[2])
    add_quad(v[6], v[7], v[5], v[4])
    add_quad(v[4], v[5], v[1], v[0])
    add_quad(v[2], v[3], v[7], v[6])
    add_quad(v[0], v[2], v[6], v[4])
    add_quad(v[5], v[7], v[3], v[1])


def add_cyl_x(center, radius, width, segments=32):
    # cylinder whose axis runs along the x axis, like a wheel or a gear
    cx, cy, cz = center
    x0, x1 = cx - width / 2, cx + width / 2
    ring0, ring1 = [], []
    for i in range(segments):
        a = 2 * math.pi * i / segments
        y = cy + radius * math.cos(a)
        z = cz + radius * math.sin(a)
        ring0.append((x0, y, z))
        ring1.append((x1, y, z))
    for i in range(segments):
        j = (i + 1) % segments
        add_quad(ring0[i], ring0[j], ring1[j], ring1[i])
        TRIS.append(((x0, cy, cz), ring0[j], ring0[i]))
        TRIS.append(((x1, cy, cz), ring1[i], ring1[j]))


def write_stl(path):
    with open(path, "wb") as f:
        f.write(b"Collector Bot simplified model".ljust(80, b" "))
        f.write(struct.pack("<I", len(TRIS)))
        for a, b, c in TRIS:
            u = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
            v = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
            n = (u[1] * v[2] - u[2] * v[1],
                 u[2] * v[0] - u[0] * v[2],
                 u[0] * v[1] - u[1] * v[0])
            ln = math.sqrt(n[0] ** 2 + n[1] ** 2 + n[2] ** 2) or 1.0
            f.write(struct.pack("<3f", n[0] / ln, n[1] / ln, n[2] / ln))
            for p in (a, b, c):
                f.write(struct.pack("<3f", *p))
            f.write(struct.pack("<H", 0))


# All sizes are in millimeters. z is up, y is toward the front.

# drive base: two side rails and two cross rails made of C channel
add_box((-140, 0, 55), (25, 400, 30))
add_box((140, 0, 55), (25, 400, 30))
add_box((0, 187, 55), (255, 25, 30))
add_box((0, -187, 55), (255, 25, 30))

# four omni wheels
for wx in (-165, 165):
    for wy in (-140, 140):
        add_cyl_x((wx, wy, 50), 50, 28)
        add_cyl_x((wx, wy, 50), 20, 32)

# two drive motors
add_box((-95, -140, 80), (45, 45, 45))
add_box((95, -140, 80), (45, 45, 45))

# V5 brain with its screen
add_box((0, -20, 90), (130, 95, 30))
add_box((0, -20, 108), (100, 70, 5))

# two vertical tower channels holding the arm, with a brace on top
add_box((-95, 130, 235), (25, 25, 330))
add_box((95, 130, 235), (25, 25, 330))
add_box((0, 130, 390), (215, 25, 25))

# arm pivot axle and the big red gears that drive the arm
add_cyl_x((0, 130, 370), 6, 260)
add_cyl_x((-85, 130, 370), 48, 14)
add_cyl_x((85, 130, 370), 48, 14)

# smaller gears and the arm motor on the tower
add_cyl_x((85, 130, 310), 24, 14)
add_cyl_x((-85, 130, 310), 24, 14)
add_box((0, 155, 300), (50, 45, 50))

# the two long arm beams, angled upward toward the front
ARM_TILT = -35
for bx in (-85, 85):
    pivot = (bx, 130, 370)
    add_box((bx, -85, 370), (25, 430, 18),
            tilt_x=ARM_TILT, pivot=pivot)

# claw at the end of the arm: motor block and two angled fingers
tip = rot_x((0, -300, 370), ARM_TILT, (0, 130, 370))
add_box((tip[0], tip[1], tip[2]), (60, 55, 55))
add_box((tip[0] - 45, tip[1] - 55, tip[2]), (10, 95, 60), tilt_z=25,
        pivot=(tip[0] - 45, tip[1] - 15, tip[2]))
add_box((tip[0] + 45, tip[1] - 55, tip[2]), (10, 95, 60), tilt_z=-25,
        pivot=(tip[0] + 45, tip[1] - 15, tip[2]))

out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "collector_bot.stl")
write_stl(out)
print("wrote", out, "with", len(TRIS), "triangles")
