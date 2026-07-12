# Collector Bot Engineering Journal

**Project:** VEX V5 Collector Bot
**Developer:** Evina Shingvi
**Timeline:** April 2026 to July 12, 2026

A note on how this journal is written: I started building the robot in April
2026, before I decided to apply to Stardance, and I did not keep notes while I
was building. So the first part of this journal is a retrospective, written on
July 12, 2026, looking back at three months of building. From July 12 onward,
entries are written as things happen, and the software work is documented by
the commit history of this repository.

---

## The build, April to early July 2026 (retrospective)

### Planning

I started by researching different drivetrain and claw mechanisms used in VEX
robots and sketching several concepts. Some of my early sketches turned out to
be too large for the parts I actually had, and I was unsure how to gear the arm
so it could lift objects without stalling. I ended up revising the dimensions
to fit a compact frame and settled on a simple collector design: a drivetrain,
a lifting arm, and a claw.

### The drivetrain

The chassis came together from VEX metal C-channels with omni wheels and one
smart motor per side. My first version had the wheels misaligned, and the robot
veered to one side when pushed. I ended up rebuilding one side of the
drivetrain, measuring the spacing between the wheels, and tightening screws
that had worked themselves loose.

### The arm

The first version of the arm was too heavy and struggled to lift, and the gears
would skip under load. I lightened it by removing unnecessary pieces,
repositioned the gears so they meshed properly, and reinforced the structure.
This was the part of the build that taught me that lifting is a gearing problem
more than a motor problem. Later, when driving with the arm raised, the frame
flexed slightly during turns, so I added more structural supports.

### The claw

The first claw could not grip objects securely and its two sides were uneven.
I rebuilt it using longer metal pieces and adjusted the spacing, then tested it
against objects of different sizes. Larger objects still slipped at first, so
I tightened the mechanism until the grip was reliable.

### Wiring and reliability

Wires occasionally snagged on moving parts, and one motor disconnected in the
middle of a test. I rerouted the wiring away from anything that moves, added
cable ties, labeled the motor ports, and got into the habit of checking every
connection before each run.

By early July the robot itself was solid: it could be pushed around, the arm
held together under load, and the claw gripped. What it did not have yet was
a program.

## July 12, 2026: The complete program, and a real repository

Big day for the software side. The robot now has a full working program:

* Wrote the whole driver control program in C++ using PROS. Tank drive on the
  joysticks, R1/R2 for the arm, L1/L2 for the claw, plus a one second
  autonomous routine that drives forward.
* Learned about motor brake modes. The arm and claw now use HOLD mode, so the
  arm stays up and the claw keeps its grip when I let go of the buttons.
* Reversed the right drive motor in code so both sides push the robot forward
  together.
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

### Current status (July 12, 2026)

The Collector Bot can:

* Drive using tank controls.
* Lift and lower an arm.
* Open and close a claw to collect objects.
* Hold arm and claw position using brake mode.
* Execute a basic autonomous routine.
* Build and upload successfully using PROS.

### Next steps

* Test the program on the actual robot and tune the arm and claw speeds.
* Improve the autonomous routine.
* Add sensors for more accurate movement.
* Increase claw grip strength.
* Practice driving for TSA competitions during the 2026 to 2027 season.
