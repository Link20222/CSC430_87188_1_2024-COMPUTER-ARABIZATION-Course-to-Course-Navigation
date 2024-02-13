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
          no2=int(no)-int(no)%100
          play_audio(str(no2))
          no=int(no)%100
          print(no)
          if no>0:
               play_audio("w")
               ten(no)

def th(number):
        no = int(number) - int(number) % 1000
        print(no)
        play_audio(str(no))
        no = int(number) % 1000
        if int(no) > 0 and int(no) < 100:
            play_audio("w")
            ten(no)
        elif int(no) >=100:
               play_audio("w")  
               hun(no)

def tenth(number):
      ten(str(int(number)//1000))
      play_audio("1000")
      no=int(number)%1000
      if int(no) > 0 and int(no) < 100:
          play_audio("w")
          ten(no)
      elif int(no) >=100:
          play_audio("w")  
          hun(no)

def hunth(number):
      hun(str(int(number)//1000))
      play_audio("1000")
      no=int(number)%1000
      if int(no) > 0 and int(no) < 100:
          play_audio("w")
          ten(no)
      elif int(no) >=100:
          play_audio("w")  
          hun(no)



number = input("enter No. Between 0-1000000: ")

while True:
    if int(number) == 0:
        play_audio("0")
    elif int(number) < 100:
        ten(number)
    elif int(number) < 1000:
        hun(number)
    elif int(number) < 10000:
        th(number)
    elif int(number) < 100000:
        tenth(number)
    elif int(number) < 1000000:
        hunth(number)       
    elif int(number) == 1000000:
        play_audio("1000000")
    else:
        print("Error in your input.")
     

    print("Done: ", number)
    choice = input("Do you want to continue? (1 to continue, 0 to exit): ")
    if choice == "0":
        print("Good bye")
        break
    elif choice == "1":
        number = input("enter No. Between 0-1000000:  ")
    else:
        print("Invalid choice. Exiting...")
        break











