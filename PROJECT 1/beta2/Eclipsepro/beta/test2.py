import pygame

def play_audio(file_name):
    audio_folder = "C:\\Users\\d7oom\\OneDrive\\Documents\\Soundrecordings\\Newfolder"
    file_path = audio_folder + "\\" + file_name + ".wav"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    print("read it")

def ten(no):
    if no > 0 and no < 20:
        play_audio(str(no))
    elif no >= 20:
        if no % 10 == 0:
            play_audio(str(no))
        else:
            play_audio(str(no % 10))
            play_audio("w")
            no = no - (no % 10)
            play_audio(no)

def hun(no):
    if int(no) // 100 == 1 or int(no) // 100 == 2:
        no2 = int(no) - int(no) % 100
        play_audio(str(no2))
        no = int(no) % 100
        if no > 0:
            play_audio("w")
            ten(no)
    else:
        hundreds_digit = int(no) // 100
        play_audio(str(hundreds_digit))
        play_audio("100")
        no = int(no) % 100
        if no > 0:
            play_audio("w")
            ten(no)

number = input("enter No.: ")

if int(number) == 0:
    play_audio("0")
elif int(number) < 100:
    ten(int(number))
elif int(number) < 1000:
    hun(int(number))
elif int(number) < 10000:
    if int(number) // 1000 == 1 or int(number) // 1000 == 2:
        no = int(number) - int(number) % 1000
        play_audio(str(no))
        no = int(number) % 1000
        if no > 0:
            play_audio("w")
            if no < 100:
                ten(no)
            else:
                hun(no)
    else:
        print("error.")
elif int(number) < 100000:
    ten(int(number) // 1000)
    play_audio("1000")
    no = int(number) % 1000
    if no > 0:
        play_audio("w")
        if no < 100:
            ten(no)
        else:
            hun(no)
elif int(number) < 1000000:
    hun(int(number) // 1000)
    play_audio("1000")
    no = int(number) % 1000
    if no > 0:
        play_audio("w")
        if no < 100:
            ten(no)
        else:
            hun(no)
elif int(number) == 1000000:
    play_audio("1000000")
else:
    print("error.")

print("Done: ", number)