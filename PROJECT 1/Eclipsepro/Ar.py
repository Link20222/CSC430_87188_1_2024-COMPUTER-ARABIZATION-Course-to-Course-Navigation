import pygame
no=0
no2=0
def play_audio(file_name):
    audio_folder = "C:\\Users\\d7oom\\Desktop\\Eclipsepro"
    file_path = audio_folder+"\\"+file_name+".wav"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    # important
    pygame.time.delay(int(sound.get_length() * 800))
    print("read it")

def ten(no):
     if int(no) > 0 and int(no) < 20:
        play_audio(str(no))
     elif int(no)>=20:
          if int(no)%10 == 0:  
                  play_audio(str(no))
          else:
                  no2=int(no)%10
                  play_audio(str(no2))
                  play_audio("w")
                  no=int(no)-int(no)%10
                  play_audio(str(no))

def hun(no):
     if int(no) // 100==1 or int(no) // 100==2:
          no2=int(no)-int(no)%100
          play_audio(str(no2))
          no=int(no)%100
          print(no)
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
def th(number):
     if int(number) // 1000 == 1 or int(number) // 1000 == 2:
        no = int(number) - int(number) % 1000
        print(no)
        play_audio(str(no))
        no = int(number) % 1000
        if int(no) > 0 and int(no) < 100:
            play_audio("w")
            ten(no)
        else:
               play_audio("w")  
               hun(no)
     if int(number)>2999:
        no2=int(number) // 1000
        no =int(number) % 1000
        print(no)
        play_audio(str(no2))
        play_audio(str(1000))
        if int(no) > 0 and int(no) < 100:
            play_audio("w")
            if int(no) < 100:
                ten(no)
            else:
                play_audio("w")
                hun(no)

number = input("enter No.: ")

# تشغيل الصوت المرتبط بالرقم
if int(number) == 0:
    play_audio("0")
elif int(number) < 100:
     ten(number)
elif int(number) < 1000:
     hun(number)
elif int(number) < 10000:
     th(number)
elif int(number) < 100000:
       ten(str(int(number)//1000))
       play_audio("1000")
       no=int(number)%1000
       if int(no) > 0:
            print(no)
            play_audio("w")
            if int(no) > 99:
               hun(no)
            else:
               ten(no)
elif int(number) < 1000000:
     no=(str(int(number)//1000))  # تحويلها إلى نص
     print(no)
     hun(no)
     no=str((int(number))%1000)  # تحويلها إلى نص
     
     play_audio("1000")
     if int(no)>0:   
          if int(no)>99:
               play_audio("w")
               hun(no)
          else:
               play_audio("w")
               ten(no)
        
             
elif int(number) == 1000000:
        play_audio("1000000")
else:
    print("error.")

print("Done: ", number)