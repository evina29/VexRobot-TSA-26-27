# Builds the Collector Bot model as a colored STEP file using cadquery.
# Same geometry as generate_model.py, in a real CAD format.
# The robot was designed and built physically from VEX parts, so this
# model is a recreation of it, made after the build.
# Run with: python cad/generate_step.py   (needs: pip install cadquery)
# Output: cad/collector_bot.step

import math
import os
import cadquery as cq

SILVER = cq.Color(0.75, 0.75, 0.78)
RED = cq.Color(0.85, 0.15, 0.12)
GREEN = cq.Color(0.10, 0.55, 0.25)
BLACK = cq.Color(0.15, 0.15, 0.15)
GRAY = cq.Color(0.35, 0.38, 0.42)
BLUE = cq.Color(0.45, 0.65, 0.85)

asm = cq.Assembly(name="collector_bot")
COUNT = [0]


def add(solid, color):
    COUNT[0] += 1
    asm.add(solid, name="part%d" % COUNT[0], color=color)


def box(center, size, tilt_x=0, tilt_z=0, pivot=None):
    if pivot is None:
        pivot = center
    b = cq.Workplane().box(size[0], size[1], size[2]).translate(center)
    if tilt_x:
        b = b.rotate((pivot[0] - 1, pivot[1], pivot[2]),
                     (pivot[0] + 1, pivot[1], pivot[2]), tilt_x)
    if tilt_z:
        b = b.rotate((pivot[0], pivot[1], pivot[2] - 1),
                     (pivot[0], pivot[1], pivot[2] + 1), tilt_z)
    return b


def cyl_x(center, radius, width):
    c = cq.Workplane("YZ").circle(radius).extrude(width)
    return c.translate((center[0] - width / 2, center[1], center[2]))


def gear(center, radius, width, color):
    teeth = max(10, int(radius / 2.6))
    add(cyl_x(center, radius, width), color)
    add(cyl_x(center, 9, width + 6), color)
    for i in range(teeth):
        ang = 360.0 * i / teeth
        tooth = (center[0], center[1], center[2] + radius + 3)
        add(box(tooth, (width, 2 * math.pi * radius / teeth * 0.45, 8),
                tilt_x=ang, pivot=center), color)


def omni_wheel(center, radius, width):
    add(cyl_x(center, radius - 7, width), BLACK)
    add(cyl_x(center, 16, width + 6), GRAY)
    for i in range(12):
        ang = 360.0 * i / 12
        roller = (center[0], center[1], center[2] + radius - 6)
        add(box(roller, (width + 4, 19, 13), tilt_x=ang, pivot=center), GRAY)


def channel_y(center, length):
    cx, cy, cz = center
    add(box((cx, cy, cz - 11), (25, length, 3)), SILVER)
    add(box((cx - 11, cy, cz), (3, length, 25)), SILVER)
    add(box((cx + 11, cy, cz), (3, length, 25)), SILVER)


def channel_x(center, length):
    cx, cy, cz = center
    add(box((cx, cy, cz - 11), (length, 25, 3)), SILVER)
    add(box((cx, cy - 11, cz), (length, 3, 25)), SILVER)
    add(box((cx, cy + 11, cz), (length, 3, 25)), SILVER)


def channel_z(center, height):
    cx, cy, cz = center
    add(box((cx, cy + 11, cz), (25, 3, height)), SILVER)
    add(box((cx - 11, cy, cz), (3, 25, height)), SILVER)
    add(box((cx + 11, cy, cz), (3, 25, height)), SILVER)


def motor(center):
    add(box(center, (48, 48, 40)), BLACK)
    add(cyl_x(center, 12, 56), BLACK)


# drive base
channel_y((-140, 0, 55), 400)
channel_y((140, 0, 55), 400)
channel_x((0, 187, 55), 255)
channel_x((0, -187, 55), 255)

# wheels with drive gears
for wx in (-165, 165):
    for wy in (-140, 140):
        omni_wheel((wx, wy, 50), 50, 28)
        gx = wx - 32 if wx > 0 else wx + 32
        gear((gx, wy, 50), 34, 10, RED)

# drive motors
motor((-95, -140, 80))
motor((95, -140, 80))

# brain, screen, battery
add(box((0, -60, 90), (130, 95, 30)), GRAY)
add(box((0, -60, 108), (100, 70, 5)), BLUE)
add(box((0, 40, 95), (85, 130, 45)), GRAY)

# towers and brace
channel_z((-95, 130, 235), 330)
channel_z((95, 130, 235), 330)
add(box((0, 130, 390), (215, 25, 25)), SILVER)

# gear train up the towers
for gz, gr, gc in ((160, 22, GREEN), (235, 34, RED), (305, 22, GREEN)):
    add(cyl_x((0, 130, gz), 4, 250), SILVER)
    gear((-85, 130, gz), gr, 12, gc)
    gear((85, 130, gz), gr, 12, gc)
add(cyl_x((0, 130, 370), 6, 260), SILVER)
gear((-85, 130, 370), 48, 14, RED)
gear((85, 130, 370), 48, 14, RED)

# arm motor
motor((0, 160, 300))

# arm beams and cross plate
ARM_TILT = -35
for bx in (-85, 85):
    add(box((bx, -85, 370), (25, 430, 18),
            tilt_x=ARM_TILT, pivot=(bx, 130, 370)), SILVER)
add(box((0, -50, 370), (150, 90, 6),
        tilt_x=ARM_TILT, pivot=(0, 130, 370)), SILVER)


def rot_x_pt(p, deg, pivot):
    y, z = p[1] - pivot[1], p[2] - pivot[2]
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return (p[0], pivot[1] + y * c - z * s, pivot[2] + y * s + z * c)


# claw
tip = rot_x_pt((0, -300, 370), ARM_TILT, (0, 130, 370))
add(box(tip, (60, 55, 55)), BLACK)
add(box((tip[0] - 45, tip[1] - 55, tip[2]), (10, 95, 60), tilt_z=25,
        pivot=(tip[0] - 45, tip[1] - 15, tip[2])), SILVER)
add(box((tip[0] + 45, tip[1] - 55, tip[2]), (10, 95, 60), tilt_z=-25,
        pivot=(tip[0] + 45, tip[1] - 15, tip[2])), SILVER)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "collector_bot.step")
asm.save(out)
print("wrote", out, "with", COUNT[0], "parts")
