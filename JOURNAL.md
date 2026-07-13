# Collector Bot Engineering Journal

**Student:** Evina Shingavi
**Project:** Collector Bot (VEX V5)
**Time period:** April 2026 to July 12, 2026
**Average time spent:** about 5 hours per week, roughly 70 hours total

A note on how this journal is written: I did not keep a written log while I
was building the robot, so I reconstructed the weekly entries below from
memory on July 12, 2026, using my photos and the order I remember doing
things in. The week labels are approximate. The final week and everything
after it is documented as it happened and is backed by the commit history of
this repository.

---

## Week 1: April 1 to 5, 2026

This week marked the start of the project. My primary goal was to determine
what type of robot I wanted to build and how it would function. I spent time
researching VEX robot designs and sketching multiple concepts. After comparing
different ideas, I decided to build a collector robot capable of driving,
lifting objects with an arm, and grabbing them with a claw.

I organized all available VEX V5 parts and sorted hardware into categories.
This helped me understand what materials I already had and what additional
components might be needed later.

### Challenges

* I was unsure which arm design would provide enough lifting power.
* Several initial sketches were too large and would have required more parts
  than were available.

### Actions taken

* Simplified the design.
* Chose a compact drivetrain with a single lifting arm and claw system.
* Created rough measurements before beginning construction.

## Week 2: April 6 to 12, 2026

I began constructing the drivetrain using VEX metal C channels, wheels,
shafts, bearings, and two V5 motors. The focus was building a strong base
before adding other mechanisms.

I assembled the frame and mounted the wheels. After manually pushing the robot
across the floor, I noticed one side rolled less smoothly than the other.

### Challenges

* Wheel alignment was slightly off.
* Some bearings were not seated correctly.

### Actions taken

* Reassembled part of the chassis.
* Repositioned bearings.
* Tightened hardware and verified spacing between components.

By the end of the week, the drivetrain frame was complete.

## Week 3: April 13 to 19, 2026

This week I focused on creating the first arm prototype. Using metal beams,
gears, and shafts, I built a simple lifting mechanism.

The arm functioned mechanically but quickly revealed design problems. It was
heavier than expected and placed significant strain on the motor.

### Challenges

* Arm weight caused poor lifting performance.
* Gear alignment occasionally slipped during movement.

### Actions taken

* Tested several gear configurations.
* Recorded observations on lifting performance.
* Planned a redesign to reduce weight and improve leverage.

## Week 4: April 20 to 26, 2026

I completed the first arm redesign. The goal was to reduce weight while
maintaining lifting strength.

Several metal components were removed and replaced with a simpler structure.
I also adjusted the gear placement to improve torque.

### Challenges

* The arm became lighter but developed side to side movement.
* Structural rigidity decreased after removing support pieces.

### Actions taken

* Added temporary braces.
* Tested different mounting positions.
* Began planning a second redesign focused on stability.

## Week 5: April 27 to May 3, 2026

This week I focused on strengthening the arm structure. Additional support
beams were installed to reduce wobble and improve reliability.

Testing showed noticeable improvement compared to previous versions.

### Challenges

* Arm alignment shifted after repeated movement.
* Several screws loosened during testing.

### Actions taken

* Retightened all hardware.
* Added additional supports near the pivot point.
* Developed a maintenance checklist before testing sessions.

## Week 6: May 4 to 10, 2026

I started designing and constructing the first claw mechanism.

The original claw design was relatively small and intended for grabbing
lightweight objects.

### Challenges

* Claw opening was too narrow.
* Objects frequently slipped during lifting.

### Actions taken

* Modified claw dimensions.
* Adjusted pivot locations.
* Tested gripping performance using different object sizes.

The claw functioned but required further redesign.

## Week 7: May 11 to 17, 2026

This week I rebuilt the claw using longer metal pieces. The redesign increased
the opening width and improved object handling.

I also added rubber bands to improve grip strength and object retention.

### Challenges

* Grip strength remained inconsistent.
* Some objects rotated while being lifted.

### Actions taken

* Experimented with rubber band placement.
* Fine tuned claw geometry.
* Repeated testing with multiple object types.

Results were significantly better than the original claw design.

## Week 8: May 18 to 24, 2026

I continued mechanical refinement and focused on integrating the arm and claw
into a complete system.

This was the first week that all major robot mechanisms were physically
connected together.

### Challenges

* Combined weight affected arm performance.
* The center of gravity shifted during lifting.

### Actions taken

* Strengthened the arm mounting area.
* Rebalanced components across the chassis.
* Performed repeated lift tests.

## Week 9: May 25 to 31, 2026

Some structural components I planned to use had not arrived yet, which delayed
final assembly.

Instead of stopping progress, I focused on planning improvements, reviewing
designs, and updating documentation.

### Challenges

* Delayed parts prevented final reinforcement work.
* Testing opportunities were limited.

### Actions taken

* Reviewed previous design notes.
* Identified weak points requiring reinforcement.
* Planned future modifications.

## Week 10: June 1 to 7, 2026

The delayed parts arrived, allowing work to resume.

I reinforced the arm structure using additional support beams and replaced
several temporary components.

### Challenges

* Existing mounting holes did not perfectly match the new supports.
* Installation required partial disassembly.

### Actions taken

* Modified mounting locations.
* Reassembled sections of the robot.
* Tested structural improvements.

The arm felt much more stable after reinforcement.

## Week 11: June 8 to 14, 2026

I performed extensive mechanical testing.

During repeated operation, I noticed an arm support shifting slightly under
load.

### Challenges

* One arm support moved during testing.
* Repeated lifting caused minor alignment changes.

### Actions taken

* Repositioned support beams.
* Tightened all hardware.
* Added inspection procedures before testing.

Reliability improved significantly after adjustments.

## Week 12: June 15 to 21, 2026

This week focused on final mechanical optimization.

I inspected every subsystem, verified hardware tightness, and checked for
mechanical interference.

### Challenges

* Small alignment issues remained.
* Certain fasteners loosened over time.

### Actions taken

* Replaced worn hardware.
* Rechecked all moving assemblies.
* Conducted longer testing sessions.

## Week 13: June 22 to 28, 2026

I completed final assembly work and prepared the robot for software
development.

The robot could now drive, lift, and grip reliably from a mechanical
standpoint.

### Challenges

* Minor frame flex remained under heavy loads.

### Actions taken

* Added additional reinforcement.
* Conducted final mechanical validation.

## Week 14: June 29 to July 5, 2026

This week was dedicated to system review and preparation for programming.

I verified motor ports, wiring paths, and overall organization of the robot.

### Challenges

* Several wires were routed close to moving components.

### Actions taken

* Improved cable management.
* Secured wiring using zip ties and routing adjustments.

## Week 15: July 6 to 12, 2026

The final week was all software and documentation. Unlike the earlier weeks,
everything from here on is documented as it happened, and each piece is
backed by the commit history of this repository.

### July 12: The complete program, and a real repository

* Wrote the whole driver control program in C++ using PROS. Tank drive on the
  joysticks, R1/R2 for the arm, L1/L2 for the claw, plus a one second
  autonomous routine that drives forward.
* Learned about motor brake modes. The arm and claw use HOLD mode, so the arm
  stays up and the claw keeps its grip when I let go of the buttons.
* One drive motor moved in the wrong direction during controller testing, so
  I reversed the right drive motor in software.
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

### July 12: First test on the real robot

Uploaded the program to the V5 brain and ran it on the actual robot for the
first time. It works: the robot drives and moves under controller input, so
the code and the hardware finally met and did their job together.

The completed robot was able to:

* Drive using tank controls.
* Lift and lower objects with the arm.
* Grab and release objects using the claw.
* Maintain arm position with brake mode.
* Execute a basic autonomous routine.

### July 12, later that evening: 3D model files

A reviewer looking at my submission asked about 3D model files. I never
designed this robot in CAD, I built it directly from VEX parts and iterated on
the physical robot, so there were no model files to add. To fill that gap I
made a simplified 3D model of the finished robot as an STL file, generated by
a Python script (cad/generate_model.py) that builds the drive base, omni
wheels, brain, towers, geared arm, and claw out of boxes and cylinders using
the robot's approximate real dimensions. To be clear about the order of
events: the robot came first, and this model is a recreation of it, not the
design it was built from.

Later I extended this into a proper CAD format as well: a STEP file with 272
colored parts (silver metal, red and green gears, black motors), generated
with cadquery by cad/generate_step.py. I also added a rendered image of the
model to the README, a wiring diagram, and a bill of materials with links,
both as a table in the README and as bom.csv in the repository root.

### Next steps

* Tune the arm and claw speeds now that the program runs on the robot.
* Improve the autonomous routine.
* Add sensors for more accurate movement.
* Increase claw grip strength.
* Practice driving for TSA competitions during the 2026 to 2027 season.

### Reflection

This project taught me the importance of iteration, testing, and persistence.
Multiple redesigns were required before the arm and claw functioned reliably.
Mechanical issues often revealed new problems that were not obvious during
planning. By documenting challenges and continuously improving the design, I
was able to create a functional VEX V5 robot that met my original goals.

### Pictures of Robot

<img width="230" height="281" alt="image" src="https://github.com/user-attachments/assets/d36c37c4-2182-4c44-89a9-6a982603604d" />

<img width="298" height="324" alt="image" src="https://github.com/user-attachments/assets/92a60f62-ffbd-41df-a45f-46d0adcee5bf" />
