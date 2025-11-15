# 🕐 Alarm Clock

A simple, cross-platform alarm clock application built with Python and Tkinter. Features a clean GUI interface with real-time clock display and customizable alarm settings.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🕒 **Real-time Clock Display** - Live updating digital clock showing current time (HH:MM:SS)
- ⏰ **Easy Alarm Setup** - Intuitive dropdown menus for hours, minutes, and seconds
- 🔊 **Cross-platform Audio Support** - Works on Windows, macOS, and Linux
- 🎵 **Custom Sound Support** - Play your own WAV files or use system alerts
- 🎨 **Clean GUI** - Modern, easy-to-use interface built with Tkinter
- 🧵 **Non-blocking** - Uses threading to prevent GUI freezing

## 📋 Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- Standard Python libraries:
  - `tkinter`
  - `datetime`
  - `time`
  - `subprocess`
  - `platform`
  - `threading`

> **Note**: Tkinter comes pre-installed with most Python distributions. If you encounter issues, install it using:
> - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
> - **macOS**: Should be included with Python
> - **Windows**: Should be included with Python

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/alarm-clock.git
   cd alarm-clock
   ```

2. **Or download the files**:
   - Download `alarm_clock.py` to your desired directory

3. **(Optional) Add a custom alarm sound**:
   - Place a `sound.wav` file in the same directory as `alarm_clock.py`
   - If no sound file is provided, the app will use system alerts

## 💻 Usage

### Running the Application

```bash
python alarm_clock.py
```

or

```bash
python3 alarm_clock.py
```

### Setting an Alarm

1. **Launch the application** - Run the script to open the GUI window
2. **View current time** - The blue clock display shows the current time
3. **Set alarm time**:
   - Use the **HR** dropdown to select the hour (00-23)
   - Use the **MIN** dropdown to select the minute (00-59)
   - Use the **SEC** dropdown to select the second (00-59)
4. **Activate alarm** - Click the "Set Alarm" button
5. **Wait for alarm** - When the current time matches your set time, the alarm will trigger

### Audio Behavior

- **With `sound.wav` file**: Plays your custom sound file
- **Without sound file**:
  - **macOS**: Uses `say` command to speak "Alarm! Wake up!"
  - **Windows**: Plays a system beep
  - **Linux**: Uses system sound notification

## 🖼️ Screenshot

```
┌─────────────────────────────┐
│      Alarm Clock            │
│                             │
│        12:34:56             │
│                             │
│      Set Alarm Time         │
│                             │
│  [HR ▼] HR  [MIN ▼] MIN  [SEC ▼] SEC  │
│                             │
│      [Set Alarm]            │
└─────────────────────────────┘
```

## 🔧 How It Works

1. **GUI Thread**: The main thread runs the Tkinter GUI with a live clock display
2. **Alarm Thread**: A separate thread continuously checks the current time against the set alarm time
3. **Time Matching**: When the current time exactly matches the alarm time, the alarm triggers
4. **Audio Playback**: Cross-platform audio handler plays the sound or system alert

## 🌐 Platform Compatibility

| Platform | Status | Audio Method |
|----------|--------|--------------|
| **macOS** | ✅ Fully Supported | `afplay` / `say` command |
| **Windows** | ✅ Fully Supported | `winsound` / System beep |
| **Linux** | ✅ Fully Supported | `aplay` / `paplay` |

## 📁 Project Structure

```
alarm-clock/
│
├── alarm_clock.py          # Main application file
├── README.md               # This file
├── sound.wav               # (Optional) Custom alarm sound
└── .gitignore             # Git ignore file
```

## 🛠️ Customization

### Changing Window Size

Edit line 14 in `alarm_clock.py`:
```python
root.geometry("400x250")  # Change width x height
```

### Using a Different Sound File

1. Place your sound file (`.wav` format recommended) in the project directory
2. Edit line 86 in `alarm_clock.py`:
```python
play_sound("your-sound-file.wav")
```

### Modifying Fonts and Colors

- **Title**: Line 89 - Change font size and color
- **Clock Display**: Line 92 - Change font size and color
- **Labels**: Lines 112, 127, 142 - Modify label text and styling

## ⚠️ Known Limitations

- Alarm thread runs continuously (resource consideration for long-running sessions)
- No alarm snooze functionality
- No multiple alarms support
- Alarm sound plays once per match (doesn't loop)

## 🔮 Future Enhancements

- [ ] Multiple alarm support
- [ ] Snooze functionality
- [ ] Alarm repeat/loop option
- [ ] Alarm history/log
- [ ] Different sound themes
- [ ] 12-hour format option
- [ ] Alarm stop button
- [ ] Notification system integration

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Inspired by simple, functional desktop applications
- Thanks to the Python community for excellent documentation

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page for existing solutions
2. Create a new issue with details about your problem
3. Include your OS version and Python version when reporting bugs

---

⭐ **Star this repo if you find it helpful!**

Made with ❤️ using Python

