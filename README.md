# Anime Saver v2.0

Anime Saver v2.0 is a desktop UI prototype built with Python and PySide6. The current app starts in a frameless, full-screen window and shows an animated loading/title screen with custom window controls, bundled fonts, SVG icons, and a live date/time display.

## Features

- Full-screen frameless PySide6 main window
- Animated `ANiME SAVER` title shine effect
- Custom minimize, maximize/fullscreen, and close controls
- Live date/time widget
- Bundled fonts, images, and SVG assets
- Experimental scripts for UI tests and pattern logic

## Requirements

- Python 3.10+
- PySide6
- screeninfo

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install PySide6 screeninfo
```

## Run

From the project root:

```powershell
python main.py
```

The app opens as a full-screen window. Use the custom controls at the top center to close, minimize, or toggle fullscreen.

## Project Structure

```text
.
├── main.py                  # Application entry point
├── pages/
│   ├── firstloading.py      # Current startup/loading screen
│   └── login.py             # Reserved for login page work
├── widgets/                 # Custom PySide6 widgets
├── tools/                   # Small shared helpers
├── fonts/                   # Bundled application fonts
├── icons/                   # SVG window-control icons
├── images/                  # Image assets
├── others/                  # Experiments and scratch prototypes
└── patterns.py              # Android-style pattern experiment
```

## Notes

- The active startup page is `FirstLoading` in `pages/firstloading.py`.
- `pages/login.py` is currently empty, and `LoginPage` is commented out in `main.py`.
- `test*.py` and files in `others/` appear to be development experiments rather than the main application flow.
- The main window is currently fixed at `1920x1080` before entering full-screen mode.

## License

No license has been added yet.
