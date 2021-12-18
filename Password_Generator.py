import random

pswd_char_big = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
pswd_char_small = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","y","j","k","l","z","x","c","v","b","n","m"]
pswd_char_number = ["1","2","3","4","5","6","7","8","9","0"]
pswd_char_specialCharacter = ["~","!","@","#","$","%","^","*","-","_","=","+","[","{","]","}","/",";",":",",",".","?"]


true = True
while true == True:
  password_length = int(input("Enter the length of the password: "))

  password = ''

  if password_length >7:
    for i in range(password_length):
      random.shuffle(pswd_char_big)
      random.shuffle(pswd_char_small)
      random.shuffle(pswd_char_number)
      random.shuffle(pswd_char_specialCharacter)

      password += pswd_char_big[random.randint(0,len(pswd_char_big)-1)] + pswd_char_small[random.randint(0,len(pswd_char_small)-1)] + pswd_char_number[random.randint(0,len(pswd_char_number)-1)] + pswd_char_specialCharacter[random.randint(0,len(pswd_char_specialCharacter)-1)]
      password = ''.join(random.sample(password, len(password)))
      if len(password) > password_length:
        password = password[:password_length]
        break
  else:
    print("Password length too short, pick a stronger password length")

  print(password)