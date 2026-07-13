# Collector Bot Engineering Journal

**Student:** Evina Shingavi
**Project:** Collector Bot (VEX V5)
**Time period:** April 2026 to July 12, 2026
**Average time spent:** about 5 hours a week, so roughly 70 hours total

Quick note about how this journal is written: I didn't keep a written log
while I was building the robot. I reconstructed the weekly entries below from
memory on July 12, 2026, using my photos and the order I remember doing things
in, so the week labels are approximate. The last week and everything after it
was written as it happened, and you can check it against the commit history of
this repository.

---

## Week 1: April 1 to 5, 2026

This was the start of the project. I spent most of the week figuring out what
kind of robot I even wanted to build. I looked at a bunch of VEX robot
designs, and the one that stuck with me was the official VEX V5 Clawbot. I
used it as my inspiration: I liked the idea of a robot that drives, lifts,
and grabs, but I wanted to design my own version instead of following the kit
instructions. Mine ended up pretty different, with taller towers, a longer
two beam arm driven by a gear train, and omni wheels on a bigger chassis.
I sketched out a few ideas and settled on that direction.

Some of the robots I looked at in person while I was deciding what to build:

<img width="307" height="399" alt="a robot I looked at for inspiration" src="https://github.com/user-attachments/assets/972cb72f-1691-4b63-b9c7-ae3cab8441d0" />
<img width="496" height="403" alt="a tread robot I looked at for inspiration" src="https://github.com/user-attachments/assets/2fbce6d8-c6b1-42cd-ac7b-221859901601" />
<img width="471" height="404" alt="top view of the tread robot" src="https://github.com/user-attachments/assets/54cf41aa-821c-402b-a89c-c34f619c04fb" />

I also dumped out all my VEX parts and sorted the hardware into groups so I
knew what I actually had and what I might need to get later.

### Challenges

* I wasn't sure which arm design would be strong enough to actually lift
  things.
* A couple of my sketches were way too big and would have needed more parts
  than I had.

### What I did about it

* Simplified the design.
* Went with a compact drivetrain plus one lifting arm and a claw.
* Did some rough measurements before starting to build.

## Week 2: April 6 to 12, 2026

I started building the drivetrain with VEX C channels, wheels, shafts,
bearings, and two V5 motors. I wanted a solid base before adding anything
else.

I got the frame together and mounted the wheels. When I pushed the robot
across the floor by hand, one side rolled worse than the other.

### Challenges

* The wheel alignment was a little off.
* Some bearings weren't seated right.

### What I did about it

* Took apart and rebuilt part of the chassis.
* Fixed the bearing positions.
* Tightened everything and checked the spacing between parts.

By the end of the week the drivetrain frame was done.

The first version of the drive base:

<img width="389" height="398" alt="first version of the drive base" src="https://github.com/user-attachments/assets/ee93d5da-97c8-49db-825e-0584d6f92764" />

## Week 3: April 13 to 19, 2026

This week was the first arm prototype. I built a simple lifting mechanism out
of metal beams, gears, and shafts.

It technically worked, but it had problems right away. It was heavier than I
expected and it was really straining the motor.

The first arm prototype, with the big gears mounted on the beams:

<img width="307" height="374" alt="first arm prototype with gears" src="https://github.com/user-attachments/assets/49e943c1-c62b-4cf4-baed-2cea39dea6f9" />

### Challenges

* The arm was too heavy to lift well.
* The gears slipped sometimes while it moved.

### What I did about it

* Tried a few different gear setups.
* Wrote down what I noticed about the lifting.
* Started planning a redesign to cut weight and get better leverage.

## Week 4: April 20 to 26, 2026

I finished the first arm redesign. The whole point was making it lighter
without losing lifting strength.

I took off several metal pieces and went with a simpler structure, and moved
the gears around to get better torque.

### Challenges

* The arm got lighter but started wobbling side to side.
* Taking off support pieces made the whole thing less rigid.

### What I did about it

* Added some temporary braces.
* Tried different mounting spots.
* Started planning a second redesign, this time for stability.

## Week 5: April 27 to May 3, 2026

This week was about making the arm sturdier. I added more support beams to cut
down the wobble.

Testing went a lot better than the earlier versions.

### Challenges

* The arm alignment kept shifting after moving it a bunch of times.
* Some screws came loose during testing.

### What I did about it

* Retightened all the hardware.
* Added extra supports near the pivot.
* Started doing a quick check of the hardware before every testing session.

## Week 6: May 4 to 10, 2026

I started building the first claw.

The first version was pretty small and only really meant for light objects.

### Challenges

* The claw didn't open wide enough.
* Things kept slipping out while lifting.

### What I did about it

* Changed the claw dimensions.
* Moved the pivot points.
* Tested the grip on different sized objects.

It worked, but I knew it needed a redesign.

## Week 7: May 11 to 17, 2026

I rebuilt the claw with longer metal pieces so it opens wider and handles
objects better.

I also added rubber bands to help it grip and hold on to stuff.

### Challenges

* The grip strength was still inconsistent.
* Some objects would rotate while getting lifted.

### What I did about it

* Messed around with the rubber band placement until it worked.
* Adjusted the claw geometry.
* Kept testing with different kinds of objects.

The rebuilt claw on the end of the arm:

<img width="407" height="400" alt="the rebuilt claw" src="https://github.com/user-attachments/assets/8613b248-8f4f-485f-9b2b-dcdc06b60916" />

Way better than the first claw.

## Week 8: May 18 to 24, 2026

This week I put the arm and claw together into one system. First time all the
main mechanisms of the robot were actually connected.

The gear train that drives the arm, coming together on the towers:

<img width="335" height="403" alt="arm gear train on the towers" src="https://github.com/user-attachments/assets/ced9a6d8-08b9-455c-9aa8-7ba2d0c08065" />

### Challenges

* The combined weight made the arm perform worse.
* The center of gravity moved around when lifting.

### What I did about it

* Strengthened where the arm mounts.
* Moved things around on the chassis to rebalance it.
* Did a bunch of lift tests over and over.

## Week 9: May 25 to 31, 2026

Some parts I ordered hadn't shown up yet, so I couldn't do the final assembly
work I wanted to do.

Instead of just stopping, I used the week to plan improvements, go over my
designs, and update my notes.

### Challenges

* Missing parts meant I couldn't do the reinforcement work.
* Not much testing was possible.

### What I did about it

* Went back through my design notes.
* Made a list of the weak points that needed reinforcement.
* Planned out the next changes.

## Week 10: June 1 to 7, 2026

The parts finally came, so work started back up.

I reinforced the arm with more support beams and swapped out some of the
temporary pieces.

### Challenges

* The existing mounting holes didn't line up with the new supports.
* I had to partially take the robot apart to install them.

### What I did about it

* Changed the mounting locations.
* Put the sections back together.
* Tested it to make sure the structure actually improved.

The arm felt way more stable after this.

Mid rebuild on my work table:

<img width="185" height="260" alt="mid rebuild on the work table" src="https://github.com/user-attachments/assets/dc7a7034-d55a-4cc4-b715-0b12f773c5cc" />

## Week 11: June 8 to 14, 2026

Lots of mechanical testing this week.

While running it over and over, I noticed one of the arm supports shifting a
little under load.

### Challenges

* An arm support moved during testing.
* Lifting over and over caused small alignment changes.

### What I did about it

* Repositioned the support beams.
* Tightened all the hardware again.
* Started inspecting things before each test.

It got a lot more reliable after that.

## Week 12: June 15 to 21, 2026

This week was final mechanical cleanup. I went through every subsystem,
checked that the hardware was tight, and looked for anything rubbing or
interfering.

### Challenges

* There were still some small alignment issues.
* Certain fasteners kept loosening over time.

### What I did about it

* Replaced the worn hardware.
* Rechecked all the moving parts.
* Ran longer testing sessions.

## Week 13: June 22 to 28, 2026

Finished up the assembly work and got the robot ready for programming.

At this point it could drive, lift, and grip reliably, at least mechanically.

Almost fully assembled:

<img width="316" height="388" alt="robot almost fully assembled" src="https://github.com/user-attachments/assets/af0bb3f8-617f-4216-a507-b2b6592137cd" />

### Challenges

* There was still a little frame flex under heavier loads.

### What I did about it

* Added more reinforcement.
* Did one last round of mechanical checks.

## Week 14: June 29 to July 5, 2026

This week was mostly review and getting ready to write the code.

I went through the motor ports, the wiring paths, and the overall organization
of the robot.

### Challenges

* Some wires were running too close to moving parts.

### What I did about it

* Cleaned up the cable management.
* Secured the wires with zip ties and rerouted the bad ones.

## Week 15: July 6 to 12, 2026

The last week was all software and documentation. Unlike the earlier weeks,
everything from here on was written down as it happened, and you can check all
of it against the commit history.

### July 12: The complete program, and a real repository

* Wrote the whole driver control program in C++ with PROS. Tank drive on the
  joysticks, R1/R2 for the arm, L1/L2 for the claw, plus a one second
  autonomous routine that drives forward.
* Learned about motor brake modes. The arm and claw use HOLD mode, so the arm
  stays up and the claw keeps its grip when I let go of the buttons.
* One drive motor spun the wrong way during controller testing, so I reversed
  the right drive motor in the code.
* Added a joystick deadband so the robot doesn't slowly creep when the sticks
  aren't perfectly centered.
* Ran into a real build problem: the newest PROS kernel (4.2.2) wants the
  gnu++26 compiler standard, but the toolchain that comes with the PROS VS
  Code extension only goes up to gnu++20. Fixed it by changing the C and C++
  standards in common.mk, and after that it compiled clean.
* Set the project up as a proper repository: everything at the root, a README
  that explains the robot and how to run it, an MIT license, and this journal.
* Also learned the hard way that uploading files to GitHub through the browser
  skips folders. My first upload was missing src, include, and firmware, so
  the repo literally had no code in it. Fixed it by pushing with git instead.

### July 12: First test on the real robot

Uploaded the program to the V5 brain and ran it on the actual robot for the
first time. It works. The robot drives and moves with the controller, so the
code and the hardware finally met and did their job together.

The finished robot can:

* Drive with tank controls.
* Lift and lower objects with the arm.
* Grab and release objects with the claw.
* Hold the arm position with brake mode.
* Run a basic autonomous routine.

### July 12, later that evening: 3D model files

A reviewer looking at my submission asked about 3D model files. I never
designed this robot in CAD. I built it straight from VEX parts and iterated on
the physical robot, so there were no model files to add. To fill that gap I
made a simplified 3D model of the finished robot as an STL file, generated by
a Python script (cad/generate_model.py) that builds the drive base, omni
wheels, brain, towers, geared arm, and claw out of boxes and cylinders using
the robot's real approximate measurements. Just to be clear about the order of
events: the robot came first, and this model is a recreation of it, not the
design it was built from.

Later I extended it into a proper CAD format too: a STEP file with 272 colored
parts (silver metal, red and green gears, black motors), generated with
cadquery by cad/generate_step.py. I also added a rendered image of the model
to the README, a wiring diagram, and a bill of materials with links, both as a
table in the README and as bom.csv in the root of the repository.

### Next steps

* Tune the arm and claw speeds now that the program runs on the robot.
* Improve the autonomous routine.
* Add sensors for more accurate movement.
* Make the claw grip stronger.
* Practice driving for TSA competitions during the 2026 to 2027 season.

### Reflection

This project taught me a lot about iteration, testing, and just sticking with
it. The arm and claw both needed multiple redesigns before they worked
reliably, and fixing one mechanical problem usually revealed another one I
hadn't noticed during planning. By writing down what went wrong and improving
the design piece by piece, I ended up with a working VEX V5 robot that does
what I originally wanted it to do.

### Pictures of Robot

<img width="230" height="281" alt="image" src="https://github.com/user-attachments/assets/d36c37c4-2182-4c44-89a9-6a982603604d" />

<img width="298" height="324" alt="image" src="https://github.com/user-attachments/assets/92a60f62-ffbd-41df-a45f-46d0adcee5bf" />









