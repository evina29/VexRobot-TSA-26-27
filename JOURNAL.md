# Collector Bot Devlog

This is the build journal for Collector Bot, my VEX V5 collector robot for
Stardance Hack Club and the 2026 to 2027 TSA year.

A note on how this journal is written: I started building the robot in April
2026, before I decided to apply to Stardance, and I did not keep notes while I
was building. So the first part of this journal is a retrospective, written on
July 12, 2026, looking back at the three months of building. From July 12
onward, entries are written as things happen.

---

## The build, April to early July 2026 (retrospective)

I started this project in April 2026 because I wanted a robot for the 2026 to
2027 TSA year that could actually collect and carry objects, not just drive
around. I built it from VEX metal parts and V5 electronics.

The robot as it stands today, and roughly in the order it came together:

**The drive base.** A metal C-channel chassis with omni wheels and one smart
motor per side. Omni wheels have small rollers around the rim, which lets the
robot turn smoothly without the wheels fighting each other.

**The arm.** Two long metal beams driven by a motor through red high strength
gears. The gears at the top of the beams are what the photo in this repo shows
best. Getting an arm to lift and hold weight is a gearing problem more than a
motor problem, which I did not appreciate when I started.

**The claw.** A motor at the end of the arm that opens and closes to grab and
release objects. This is what turns the robot from a drive base into an actual
collector.

Three months sounds like a long time for this, and most of that time went into
rebuilding: getting gears to mesh properly, getting the arm geometry to a point
where it could lift without tipping the robot, and rearranging motors and
wiring as the design changed. I do not have week by week notes from this
period, which is exactly why the rest of this journal exists.

## July 12, 2026: The complete program, and a real repository

Big day for the software side. The robot now has a full working program:

* Wrote the whole driver control program in C++ using PROS. Tank drive on the
  joysticks, R1/R2 for the arm, L1/L2 for the claw, plus a one second
  autonomous routine that drives forward.
* Learned about motor brake modes. The arm and claw now use HOLD mode, so the
  arm stays up and the claw keeps its grip when I let go of the buttons.
* Added a joystick deadband so the robot does not creep when the sticks are
  not perfectly centered.
* Hit a real build problem: the newest PROS kernel (4.2.2) asked the compiler
  for the gnu++26 standard, but the toolchain that ships with the PROS VS Code
  extension only supports up to gnu++20. Fixed it by changing the C and C++
  standards in common.mk, and after that the project compiled cleanly.
* Set the project up as a proper repository: everything at the root, a README
  that explains the robot and how to run it, an MIT license, and this journal.
* Learned that uploading files to GitHub through the browser skips folders.
  My first upload was missing src, include, and firmware, meaning the repo had
  no actual code in it. Fixed by pushing the full project with git instead.

Next up: test the program on the actual robot, tune the arm and claw speeds,
and start practicing driving for TSA.
