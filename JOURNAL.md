# Collector Bot Devlog

This is the build journal for Collector Bot, my VEX V5 collector robot for
Stardance Hack Club and the 2026 to 2027 TSA year. Newest entries are at the
bottom.

---

## April 2026: Starting the project

[Write what really happened here! For example: why you decided to build a
collector robot, what parts you started with, what your first idea for the
design was, and what the very first thing you built looked like. Photos are
great too, you can drag them into this file on GitHub.]

## May 2026: Building the chassis and drivetrain

[Write about building the drive base: how you attached the motors and wheels,
anything that went wrong, anything you had to rebuild. Real problems and how
you fixed them are the best part of a devlog.]

## June 2026: The arm and claw

[Write about building the lift arm with the gears and the claw: how you got
the gears to mesh, how many tries the arm geometry took, what the robot could
do by the end of the month.]

## July 12, 2026: Finished the first complete version of the code

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
* Set the project up as a proper GitHub repository: everything at the root,
  a README that explains the robot and how to run it, an MIT license, and
  this journal.

Next up: test the program on the actual robot, tune the arm and claw speeds,
and start practicing driving for TSA.
