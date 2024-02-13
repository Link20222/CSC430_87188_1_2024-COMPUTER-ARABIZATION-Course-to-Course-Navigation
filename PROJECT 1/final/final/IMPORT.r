IMPORT pygame
no <- 0
no2 <- 0

FUNCTION play_audio(file_name):
    audio_folder <- "C:\\Users\\d7oom\\Desktop\\Eclipsepro"
    file_path <- audio_folder + "\\" + file_name + ".wav"
    pygame.mixer.init()
    sound <- pygame.mixer.Sound(file_path)
    sound.play()
    # Important
    pygame.time.delay(int(sound.get_length() * 800))
# https://github.com/Link20222/CSC430_87188_1_2024-COMPUTER-ARABIZATION-Course-to-Course-Navigation/tree/main/PROJECT%201/final
# Missing code - Please provide the remaining code
# https://youtu.be/7Ym5-yIU-u0

FUNCTION ten(no):
    IF int(no) > 0 AND int(no) < 20 THEN
       CALL play_audio(str(no))
    ELSE IF int(no) >= 20 THEN
        IF int(no) % 10 == 0 THEN
            CALL play_audio(str(no))
        ELSE
            no2 <- int(no) % 10
            CALL play_audio(str(no2))
            CALL play_audio("w")
            no <- int(no) - int(no) % 10
            CALL play_audio(str(no))


FUNCTION hun(no):
    no2 <- int(no) - int(no) % 100
    CALL play_audio(str(no2))
    no <- int(no) % 100
    IF no > 0 THEN
        CALL play_audio("w")
        CALL ten(no)

FUNCTION th(number):
    no <- int(number) - int(number) % 1000
    CALL play_audio(str(no))
    no <- int(number) % 1000
    IF int(no) > 0 AND int(no) < 100 THEN
        CALL play_audio("w")
        CALL ten(no)
    ELSE IF int(no) >= 100 THEN
        CALL play_audio("w")
        CALL hun(no)


FUNCTION tenth(number):
    ten(str(int(number) // 1000))
    CALL play_audio("1000")
    no <- int(number) % 1000
    IF int(no) > 0 AND int(no) < 100 THEN
        CALL play_audio("w")
        CALL ten(no)
    ELSE IF int(no) >= 100 THEN
        CALL play_audio("w")
        CALL hun(no)

FUNCTION hunth(number):
    hun(str(int(number) // 1000))
    play_audio("1000")
    no <- int(number) % 1000
    IF int(no) > 0 AND int(no) < 100 THEN
        CALL play_audio("w")
        CALL ten(no)
    ELSE IF int(no) >= 100 THEN
        CALL play_audio("w")
        CALL hun(no)

number <- INPUT("enter No. Between 0-1000000: ")

WHILE True DO
    IF int(number) == 0 THEN
        CALL play_audio("0")
    ELSE IF int(number) < 100 THEN
        CALL ten(number)
    ELSE IF int(number) < 1000 THEN
        CALL hun(number)
    ELSE IF int(number) < 10000 THEN
        CALL th(number)
    ELSE IF int(number) < 100000 THEN
        CALL tenth(number)
    ELSE IF int(number) < 1000000 THEN
        CALL hunth(number)
    ELSE IF int(number) == 1000000 THEN
        CALL play_audio("1000000")
    ELSE
        PRINT "Error in your input."
    
    PRINT "Done: ", number
    choice <- INPUT("Do you want to continue? (1 to continue, 0 to exit): ")
    IF choice == "0" THEN
        PRINT "Good bye"
        BREAK
    ELSE IF choice == "1" THEN
        number <- INPUT("enter No. Between 0-1000000: ")
    ELSE
        PRINT "Invalid choice. Exiting..."
        BREAK