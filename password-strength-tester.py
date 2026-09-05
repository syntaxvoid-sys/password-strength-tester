password = input("enter password:")
symbols = "!@#$%^&*()_-+~?=[]}{/§°':.;,´`"
numbers = "1234567890"
has_number = False
has_symbols = False
is_8_long = False
has_uppercase = False
score = 0
weak = 0

if password .upper:
     has_uppercase = True

if len(password) >= 8:
    is_8_long = True

for character in password:
    if character in symbols:
     has_symbols = True

    if character in numbers:
        has_number = True 

if has_number:
      print("has atleast one number") 
      score += 1 
else:
     print("needs atleast one number")
if has_symbols:
      print("has atleast one symbol")
      score += 1
else:
     print("need atleast one symbol")
if is_8_long:
      print("is atleast 8 characters long")
      score += 1
else:
     print("password needs to be 8 characters long")
if has_uppercase:
     print("has atleast one uppercase")
     score += 1
if score == 0:
     print("password is SUPER WEAK")
elif score == 1:
     print("passwors is weak")
elif score == 2:
     print("password is weak but okay")
elif score == 3:
     print("Password is kinda strong")
else:
     print("Password is strong")

print("score is", score, "out of 4" )
