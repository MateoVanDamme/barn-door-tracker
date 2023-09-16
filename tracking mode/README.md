# Tracking Mode

The "tracking mode" project is the most important component of the Barn Door Tracker control system. Its sole task is ensuring the tracker's reliable operation during astrophotography sessions. This means maintaining a constant rotational speed while the tracker opens. The paramount objective of this module is reliability. Every bug could potentially compromise an entire evening of astrophotography. To mitigate this, the project remains intentionally straightforward and efficient to find and track bugs more easily. 

## tracking_script

The `tracking_script` is the heart of the "tracking mode" project. It contains the script responsible for controlling the Barn Door Tracker's motion. This script calculates the precise timing for sending step commands to the stepper motor, ensuring that the tracker opens at a consistent rate. 

## trinket_m0_test

The `trinket_M0_test` folder contains a simple test script for the Adafruit Trinket M0 microcontroller, which is used in this project. The scripts can be used to check the proper functionality of the microcontroller before deploying it in the "tracking mode" project.

## Kinematics calculations

To know when to send step commands the tracking_script has to preform some simple kinematics calculations. These calculations are defined by the trackers geometry, as well as the lengths of the various linkages. 