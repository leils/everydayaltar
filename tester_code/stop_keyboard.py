from pytimedinput import timedKey
userText, timedOut = timedKey("Continue? (y/n): ", allowCharacters="yYnN")
if(timedOut):
    print("Timed out when waiting for input.")
else:
    if(userText in "yY"):
        print("Yes")
    else:
        print("No")