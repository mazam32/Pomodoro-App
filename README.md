# Pomodoro Timer Application

## Overview

This is a Pomodoro Timer application built using Python and Tkinter. The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This application automates the timing for work periods and breaks to help improve productivity and focus.

## Features

- **Work Interval**: Set to 25 minutes by default.
- **Short Break Interval**: Set to 5 minutes by default.
- **Long Break Interval**: Set to 20 minutes by default.
- **Cycle**: After 4 work intervals, a longer break is provided.
- **Visual and Text Indicators**: The application displays the current timer and changes the label color based on the current phase (Work, Short Break, Long Break).
- **Check Marks**: Track progress with check marks displayed after each completed work session.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python installations)
- An image file for the tomato (default file path: `/Users/muhammadhamdazam/Documents/Python Programs/Day 28/pomodoro-start/tomato.png`)

## How to Use

1. **Clone the repository**: Ensure you have a local copy of the application.
2. **Prepare the environment**: Ensure you have Python and Tkinter installed.
3. **Run the application**: Execute the script using a Python interpreter.

```bash
python main.py
```

4. **Start Timer**: Click the "Start" button to begin the Pomodoro cycle.
5. **Reset Timer**: Click the "Reset" button to reset the timer and the progress check marks.

## File Structure

- **pomodoro_timer.py**: The main script containing the application logic and GUI setup.
- **tomato.png**: Image file used in the GUI (ensure the path is correctly set in the script).

## Code Explanation

### Constants

- **PINK, RED, GREEN, YELLOW**: Color codes used for GUI elements.
- **FONT_NAME**: Font used for text elements.
- **WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN**: Duration for work, short break, and long break intervals respectively.

### Functions

- **reset_timer()**: Resets the timer, labels, and progress marks.
- **start_timer()**: Starts the timer and sets the interval based on the current phase (work/break).
- **count_down(count)**: Manages the countdown mechanism and updates the timer display every second.

### GUI Setup

- **window**: Main Tkinter window setup with title and background color.
- **title_label**: Label to display the current phase (Timer, Break, Work).
- **canvas**: Canvas to display the tomato image and the timer text.
- **start_button, reset_button**: Buttons to start and reset the timer.
- **check_mark**: Label to display check marks for completed work sessions.

### Running the Application

Execute the script using the Python interpreter to start the GUI application.

```bash
python main.py
```

## Customization

- Modify the duration constants (**WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN**) to change the default timing intervals.
- Ensure the path to the tomato image is correct. Update the `PhotoImage(file="path_to_your_image/tomato.png")` line if necessary.

## License

This project is open source and available under the [MIT License](LICENSE).

---

This README file provides a comprehensive guide to understanding, running, and customizing the Pomodoro Timer application. Enjoy enhanced productivity with this simple yet effective time management tool!