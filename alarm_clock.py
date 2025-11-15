# Import Required Library
from tkinter import *
import datetime
import time
import subprocess
import platform
import os
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("400x250")

# Use Threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()

def play_sound(filename="sound.wav"):
	"""Play sound file cross-platform with fallback"""
	system = platform.system()
	
	# Check if file exists
	if not os.path.exists(filename):
		# Use system beep/notification as fallback
		print(f"Sound file '{filename}' not found. Using system alert instead.")
		try:
			if system == "Darwin":  # macOS
				# Use macOS say command as fallback
				subprocess.Popen(["say", "Alarm! Wake up!"])
			elif system == "Windows":
				import winsound
				winsound.Beep(1000, 500)  # Beep at 1000Hz for 500ms
			else:  # Linux
				subprocess.Popen(["paplay", "/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga"], 
				               stderr=subprocess.DEVNULL)
		except Exception as e:
			print(f"Error playing fallback sound: {e}")
		return
	
	# Play the sound file if it exists
	try:
		if system == "Darwin":  # macOS
			subprocess.Popen(["afplay", filename], stderr=subprocess.DEVNULL)
		elif system == "Windows":
			import winsound
			winsound.PlaySound(filename, winsound.SND_ASYNC)
		else:  # Linux
			subprocess.Popen(["aplay", filename], stderr=subprocess.DEVNULL)
	except Exception as e:
		print(f"Error playing sound: {e}")
		# Try fallback
		if system == "Darwin":
			subprocess.Popen(["say", "Alarm! Wake up!"])

# Clock display variable
clock_label = None

def update_clock():
	"""Update the clock display every second"""
	current_time = datetime.datetime.now().strftime("%H:%M:%S")
	if clock_label:
		clock_label.config(text=current_time)
	# Schedule next update
	root.after(1000, update_clock)

def alarm():
	# Infinite Loop
	while True:
		# Set Alarm
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

		# Wait for one seconds
		time.sleep(1)

		# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time, set_alarm_time)

		# Check whether set alarm is equal to current time or not
		if current_time == set_alarm_time:
			print("Time to Wake up")
			# Playing sound
			play_sound("sound.wav")

# Add Labels, Frame, Button, Optionmenus
Label(root,text="Alarm Clock",font=("Helvetica 24 bold"),fg="red").pack(pady=10)

# Current time display
clock_label = Label(root,text="",font=("Helvetica 28 bold"),fg="blue")
clock_label.pack(pady=5)

# Start clock updates
update_clock()

Label(root,text="Set Alarm Time",font=("Helvetica 20 bold")).pack(pady=5)

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT, padx=5)
Label(frame, text="HR", font=("Helvetica 18")).pack(side=LEFT, padx=2)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT, padx=5)
Label(frame, text="MIN", font=("Helvetica 18")).pack(side=LEFT, padx=2)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT, padx=5)
Label(frame, text="SEC", font=("Helvetica 18")).pack(side=LEFT, padx=2)

Button(root,text="Set Alarm",font=("Helvetica 20"),command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
