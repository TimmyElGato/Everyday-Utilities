# Everyday Utilities in Python 🧰

This project is a personal collection of everyday utilities written in Python.  
The goal is to bring together small tools and converters I frequently use in my daily life into one single, organized, and expandable program.

## 💡 Features

- Binary Converter!
- Unit converter for:
  - 📏 Distance (meters, miles, inches, etc.)
  - 🌡️ Temperature (Celsius, Fahrenheit, Kelvin)
  - ⚖️ Weight (grams, kilograms, pounds, etc.)
  - ⏱ Time (seconds, minutes, hours, days, etc.)
  - 💾 Data (bits, bytes, kilobytes, megabytes, etc.)
- Designed with modularity in mind: each category is separated in its own file
- Easy-to-use text-based interface
- Built in Python 3 using basic control flow and functions — no external libraries required

## 📁 Structure

UnitConverter/
│
├── main.py # Program entry point (menu logic)
├── UnitConversor.py # Handles general unit conversions
├── TempConversor.py # Handles all temperature conversions
├── WeightConversor.py # Handles all weight conversions
├── DistanceConversor.py# Handles all distance conversions
├── DataConversor.py. # Handles all data conversions (e.g. bytes, terabytes)
├── TimeConversor.py # Handles all time conversions
├── BinaryConversor.py # Handles binary <-> text/number conversions
├── MyFunctions.py # Contains shared utility functions (e.g. display_menu)
└── README.md # This file

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository or download the files.
3. Run the main script:

'```bash'
python main.py

## 🔧 Future Plans

Add currency conversion (using API)

Add more features

Create a graphical user interface (GUI)

Store usage history

## 👤 Author

Created by Timmy ElGato as a way to practice and build helpful tools for everyday tasks.
