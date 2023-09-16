# Barn Door Tracker Repository

This repository houses the control scripts for my barn door tracker project. A barn door tracker is a unique astrophotography tool that compensates for the Earth's rotation, allowing you to capture stunning long-exposure images of celestial objects. 

## Project Boxes

Currently, the control system is divided into distinct project boxes, each serving a specific purpose.

### Interactive Control 

The "interactive control" project box utilizes an Arduino Nano IoT with BLE capabilities. Its primary function is to provide interactive control of the Barn Door Tracker. This allows you to perform tasks such as polar calibration, stowing or unstowing the tracker, and making real-time adjustments using a web interface on your mobile device.

**Folder Contents:**

- Arduino sketch for the interactive control script.
- Documentation on how to set up and use the interactive control system.

### Tracking Mode

The "tracking mode" project box is designed for capturing long-exposure images with the Barn Door Tracker. It uses an Adafruit Trinket M0 microcontroller to precisely control the tracker's motion during photography sessions, ensuring a consistent and uniform rotation.

**Folder Contents:**

- Arduino sketch for the photography mode control script.
- Documentation on configuring and using the photography mode.

### Ble.eding Edge 

The "ble.eding edge" project represents the future of the Barn Door Tracker control system with the goal of eventually integrating the functionalities of the other project boxes into a single unit. It utilizes a Seed Xiao BLE microcontroller with CircuitPython to enhance the tracker's capabilities further.

**Folder Contents:**

- Circuit Python code for the bleeding-edge BLE project box.
- Any related documentation and resources for development and usage.

## Getting Started

To get started with any of the project boxes, navigate to the respective folder and follow the provided documentation. Each project box folder contains detailed instructions on setting up and using the control system. Feel free to explore each project box to understand its functionality and how it contributes to the overall Barn Door Tracker project.

## License

This repository is licensed under the [MIT License](LICENSE)