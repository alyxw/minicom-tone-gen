# minicom-tone-gen
A small library and set of audio files to display and send messages for an UltraTec Minicom III.

# Requirements
* an Ultratec Minicom III or other TTY device using the same control tones (presumably any TTY device should work for accessiblity and compatability, but I don't know enough about TTYs to say for sure)
* a speaker, headphone, or other audio device you an attach to the acoustic coupler on your TTY device.
* Python 3.8
* the `playsound` Python module

## How To Use
Import `minicom.py` and call `minicom.displayMessage(str)`

## Technical Details
Note: I haven't looked into technical documents so this is just what I learned from experimenting with it. 

The device uses the same tones for both the letters and their "shifted" special character. When you send a special character after sending letters, what I'm calling the "shift on" tone is sent and it puts the device into special character mode for all subsequent characters, until the next non-special character is sent, when the device will send a "shift off" tone.

This script automatically sends shift tones by tracking the current shift status and looking up if the current character is a special character. At the end of a displayMessage(), it will automatically default the shift status back to off.

Any characters not found in `tonemap.py`, the dictionary of all of the characters, their audio files and shift statuses, will be omitted from the displayed message since there are no available tones for unsupported characters.

All audio files were recorded from my UltraTec Minicom III using a Sennheiser E945 mic mixed through a Behringer MX602A and captured with a Creative SoundBlaster SB1570 and cleaned up with audacity.
