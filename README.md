# minicom-tone-gen
A small library and set of audio files to display and send messages for an UltraTec Minicom III.


## How To Use
Import `minicom.py` and call `minicom.displayMessage(str)`

## Technical Details
Note: I haven't looked into technical documents so this is just what I learned from experimenting with it. 

The device uses the same tones for both the letters and their "shifted" special character. When you send a special character after sending letters, what I'm calling the "shift on" tone is sent and it puts the device into special character mode for all subsequent characters, until the next non-special character is sent, when the device will send a "shift off" tone.

All audio files were recorded from my UltraTec Minicom III using a Sennheiser E945 mic mixed through a Behringer MX602A and captured with a Creative SoundBlaster SB1570 and cleaned up with audacity.
