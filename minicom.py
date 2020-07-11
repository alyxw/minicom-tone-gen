from playsound import playsound
import tonemap

def displayMessage(message):
    shift = False  # whether the "shift" for special characters is currently on or off, starts off
    chars = list(message.upper())
    for i in range(len(chars)):
        current_letter = tonemap.tonemap.get(chars[i])
        if current_letter:
            if current_letter["special"] == True and shift == False:
                playsound("audio/CONTROL/TOGGLE SHIFT ON.wav")
                shift = True
            if current_letter["special"] == False and shift == True:
                playsound("audio/CONTROL/TOGGLE SHIFT OFF.wav")
                shift = False
            playsound(current_letter["file"])
