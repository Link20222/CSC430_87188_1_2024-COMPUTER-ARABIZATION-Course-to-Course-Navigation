import pygame
no=0
no2=0
def play_audio(file_name):
    audio_folder = "C:\\Users\\d7oom\\OneDrive\\Documents\\Soundrecordings\\Newfolder"
    file_path = audio_folder+"\\"+file_name+".wav"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    print("read it")

def ten(no):
     if no>0 & no<20:
        play_audio(str(no))
     elif no>=20:
          if int(no%10) == 0:  
                  play_audio(str(no))
          else:
                  play_audio(no%10)
                  play_audio("w")
                  no=no-no%10
                  play_audio(no)

def hun(no):
     if int(no) // 100==1| int(no) // 100==2:
          no2=int(no)-int(no)%100
          play_audio(str(no2))
          no=int(no)%100
          if no>0:
               play_audio("w")
               ten(no)
     else:
        hundreds_digit = int(number) // 100
        play_audio(str(hundreds_digit))
        play_audio(str(100))
        no=int(number)%100
        if no>0:
             play_audio("w")
             ten(no)
# طلب إدخال الرقم من المستخدم
                  


number = input("enter No.: ")

# تشغيل الصوت المرتبط بالرقم
if int(number) == 0:
    play_audio("0")
elif int(number) < 100:
     ten(number)
elif int(number) < 1000:
     hun(number)
elif int(number) < 10000:
     if int(number) // 1000==1| int(number) // 1000==2:
          no=int(number)-int(number)%1000
          play_audio(str(no))
          no=int(number)%1000
          if no>0:
            play_audio("w")
            if no<100:
                 ten(no)
            else:
                 hun(no)
elif int(number) < 100000:
       ten(str(int(number)//1000))
       play_audio("1000")
       no=number%1000
       if no>0:
        play_audio("w")
        if no<100:
            ten(no)
        else:
             hun(no)
elif int(number) < 1000000:
     hun(str(int(number)//1000))
     play_audio("1000")
     no=number%1000
     if no>0:
        play_audio("w")
        if no<100:
            ten(no)
        else:
             hun(no)
elif int(number) == 1000000:
        play_audio("1000000")
else:
    print("error.")

print("Done: ", number)