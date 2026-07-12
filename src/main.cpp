#include "main.h"

// Collector Bot: a VEX V5 robot that drives around, lifts its arm,
// and grabs objects with its claw.

pros::Controller master(pros::E_CONTROLLER_MASTER);

pros::Motor left_drive(1);    // left wheel motor
pros::Motor right_drive(-2);  // right wheel motor, reversed so both wheels push forward
pros::Motor arm(3);           // lifts the arm up and down
pros::Motor claw(4);          // opens and closes the claw

const int ARM_SPEED = 90;   // arm speed out of 127
const int CLAW_SPEED = 90;  // claw speed out of 127

// Runs once when the program starts.
void initialize() {
	pros::lcd::initialize();
	pros::lcd::set_text(1, "Collector Bot is ready!");

	// HOLD keeps the motor locked in place when it stops,
	// so the arm stays up and the claw keeps its grip.
	arm.set_brake_mode(pros::E_MOTOR_BRAKE_HOLD);
	claw.set_brake_mode(pros::E_MOTOR_BRAKE_HOLD);
}

void disabled() {}

void competition_initialize() {}

// Runs by itself during the autonomous part of a match:
// drives forward for one second, then stops.
void autonomous() {
	left_drive.move(80);
	right_drive.move(80);
	pros::delay(1000);
	left_drive.move(0);
	right_drive.move(0);
}

// Runs while a person drives the robot with the controller.
void opcontrol() {
	while (true) {
		// Tank drive: left stick controls the left wheel,
		// right stick controls the right wheel.
		int left_speed = master.get_analog(pros::E_CONTROLLER_ANALOG_LEFT_Y);
		int right_speed = master.get_analog(pros::E_CONTROLLER_ANALOG_RIGHT_Y);

		// Ignore tiny stick movements so the robot doesn't creep.
		if (left_speed > -8 && left_speed < 8) left_speed = 0;
		if (right_speed > -8 && right_speed < 8) right_speed = 0;

		left_drive.move(left_speed);
		right_drive.move(right_speed);

		// Arm: R1 lifts up, R2 lowers down, otherwise hold in place.
		if (master.get_digital(pros::E_CONTROLLER_DIGITAL_R1)) {
			arm.move(ARM_SPEED);
		} else if (master.get_digital(pros::E_CONTROLLER_DIGITAL_R2)) {
			arm.move(-ARM_SPEED);
		} else {
			arm.brake();
		}

		// Claw: L1 grabs, L2 lets go, otherwise keep the grip.
		if (master.get_digital(pros::E_CONTROLLER_DIGITAL_L1)) {
			claw.move(CLAW_SPEED);
		} else if (master.get_digital(pros::E_CONTROLLER_DIGITAL_L2)) {
			claw.move(-CLAW_SPEED);
		} else {
			claw.brake();
		}

		pros::delay(20);  // update 50 times per second
	}
}
