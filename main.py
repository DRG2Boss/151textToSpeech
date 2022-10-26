# Installed gtts, pyttsx3, and playsound (v1.2.2)
# pyttsx3 is automatically recalled when importing gtts.
import gtts
# Want to input JUST the playsound function within the playsound library.
from playsound import playsound

gaveRightAnswer = False
while not gaveRightAnswer:
    answer = input("Can I have more candy?")
    goodResponses = ["yes", "yep", "sure", "ok", "alright", "i guess"]

    if answer.lower() in goodResponses:
        gaveRightAnswer = True

celebrate = "Yummy! Time to munch."
speaker1 = gtts.gTTS(celebrate)
speaker1.save("celebrate.mp3")

repeat = "again and again and"
speaker2 = gtts.gTTS(repeat)
speaker2.save("repeat.mp3")

playsound("celebrate.mp3")
# Want to repeat the repeat.mp3 audio file 5 times because we're creepy.
for repeat_count in range(5):
    playsound("repeat.mp3")
