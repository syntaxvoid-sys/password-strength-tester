password = input("enter password:")
symbols = "!@#$%^&*()_-+~?=[]}{/§°':.;,´`"
numbers = "1234567890"
has_number = False
has_symbols = False
is_8_long = False

if len(password) >= 8:
    is_8_long = True

for character in password:
    if character in symbols:
     has_symbols = True

    if character in numbers:
        has_number = True 
        

if has_number:
      print("has atleast one number")  
else:
     print("needs atleast one number")
    
if has_symbols:
      print("has atleast one symbol")
else:
     print("need atleast one symbol")

if is_8_long:
      print("is atleast 8 characters long")
else:
     print("password needs to be 8 characters long")

if has_number and has_symbols and is_8_long:
      print("password is strong")
else:
     print("password is weak")