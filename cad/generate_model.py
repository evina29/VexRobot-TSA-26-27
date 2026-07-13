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


def add_gear(center, radius, width, teeth=None):
    # a VEX style gear: a disk with square teeth around the rim and a hub
    if teeth is None:
        teeth = max(10, int(radius / 2.6))
    add_cyl_x(center, radius, width)
    add_cyl_x(center, 9, width + 6)
    for i in range(teeth):
        ang = 360.0 * i / teeth
        tooth = (center[0], center[1], center[2] + radius + 3)
        add_box(tooth, (width, 2 * math.pi * radius / teeth * 0.45, 8),
                tilt_x=ang, pivot=center)


def add_omni_wheel(center, radius, width):
    # an omni wheel: main disk, hub, and rollers around the rim
    add_cyl_x(center, radius - 7, width)
    add_cyl_x(center, 16, width + 6)
    rollers = 12
    for i in range(rollers):
        ang = 360.0 * i / rollers
        roller = (center[0], center[1], center[2] + radius - 6)
        add_box(roller, (width + 4, 19, 13), tilt_x=ang, pivot=center)


def add_channel_y(center, length):
    # VEX C channel running along the y axis, a U shape open on top
    cx, cy, cz = center
    add_box((cx, cy, cz - 11), (25, length, 3))
    add_box((cx - 11, cy, cz), (3, length, 25))
    add_box((cx + 11, cy, cz), (3, length, 25))


def add_channel_x(center, length):
    # VEX C channel running along the x axis, a U shape open on top
    cx, cy, cz = center
    add_box((cx, cy, cz - 11), (length, 25, 3))
    add_box((cx, cy - 11, cz), (length, 3, 25))
    add_box((cx, cy + 11, cz), (length, 3, 25))


def add_channel_z(center, height):
    # VEX C channel standing vertically, a U shape open toward the front
    cx, cy, cz = center
    add_box((cx, cy + 11, cz), (25, 3, height))
    add_box((cx - 11, cy, cz), (3, 25, height))
    add_box((cx + 11, cy, cz), (3, 25, height))


def add_motor(center):
    # a V5 smart motor: rounded body approximated by a box and a cap
    add_box(center, (48, 48, 40))
    add_cyl_x((center[0], center[1], center[2]), 12, 56)


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

# drive base: two side C channels and two cross C channels
add_channel_y((-140, 0, 55), 400)
add_channel_y((140, 0, 55), 400)
add_channel_x((0, 187, 55), 255)
add_channel_x((0, -187, 55), 255)

# four omni wheels with a drive gear next to each one
for wx in (-165, 165):
    for wy in (-140, 140):
        add_omni_wheel((wx, wy, 50), 50, 28)
        gx = wx - 32 if wx > 0 else wx + 32
        add_gear((gx, wy, 50), 34, 10)

# two drive motors tucked inside the frame
add_motor((-95, -140, 80))
add_motor((95, -140, 80))

# V5 brain with its screen at the front, battery behind it
add_box((0, -60, 90), (130, 95, 30))
add_box((0, -60, 108), (100, 70, 5))
add_box((0, 40, 95), (85, 130, 45))

# two vertical tower channels holding the arm, with a brace on top
add_channel_z((-95, 130, 235), 330)
add_channel_z((95, 130, 235), 330)
add_box((0, 130, 390), (215, 25, 25))

# the gear train that climbs the towers, matching the real robot:
# small green gears low, medium red gears in the middle, and the big
# red gears at the arm pivot on top, with axles spanning the towers
for gz, gr in ((160, 22), (235, 34), (305, 22)):
    add_cyl_x((0, 130, gz), 4, 250)
    add_gear((-85, 130, gz), gr, 12)
    add_gear((85, 130, gz), gr, 12)
add_cyl_x((0, 130, 370), 6, 260)
add_gear((-85, 130, 370), 48, 14)
add_gear((85, 130, 370), 48, 14)

# arm motor mounted on the tower driving the gear train
add_motor((0, 160, 300))

# the two long arm beams, angled upward toward the front,
# with a cross plate connecting them partway up
ARM_TILT = -35
for bx in (-85, 85):
    pivot = (bx, 130, 370)
    add_box((bx, -85, 370), (25, 430, 18),
            tilt_x=ARM_TILT, pivot=pivot)
plate_pivot = (0, 130, 370)
add_box((0, -50, 370), (150, 90, 6), tilt_x=ARM_TILT, pivot=plate_pivot)

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
