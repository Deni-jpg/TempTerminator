# TempTerminator Script 🧹🚀

## Description

This Python script cleans up temporary files and folders on your system (the `%TEMP%` directory on Windows) quickly and with customization options. It features an interactive menu with colored ASCII art, displays the number of deleted files, the number of failures, and even includes an exit animation.

> ⚠️ **Warning:** Use with caution! Removing temporary files may affect running applications.

---

## Features

- **Complete Cleanup** of the temporary directory (`C:\Users\<user>\AppData\Local\Temp`).
- Counts of successfully deleted files and failures.
- Interactive, color-gradient ASCII art menu.
- Stylish exit animation.
- Option to return to the menu or exit immediately after an action.

---

## Prerequisites

- Python 3.6 or higher  
- [colorama](https://pypi.org/project/colorama/) package for terminal colors

```bash
pip install colorama
```

## Usage

1. Clone this repository:
```bash
git clone https://github.com/Deni-jpg/TempTerminator.git
cd TempTerminator
```

2. Install dependencies:
```bash
pip install colorama
```

3. Run the script:
```bash
python TempTerminator.py
```

4. Follow the menu:

> Enter 1 to clean temporary files; Enter 2 to exit.

## Executable

If you have installed `TempTerminator.exe`, you can run it directly without Python:
```bash
./TempTerminator.exe
```

Or simply double-click `TempTerminator.exe` in Windows Explorer, or run it from the command prompt:
```bash
TempTerminator.exe
```

## Contributing
Pull requests are welcome! Feel free to open issues or suggest improvements.
