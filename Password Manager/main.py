from cryptography.fernet import Fernet

'''
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)

write_key()
'''

def load_key():
  file = open("key.key", "rb")
  key = file.read
  file.close()
  return key

key = load_key()
fer = Fernet(key)



def view():
  with open('passwords.txt', 'r') as f:
    for line in f.readlines():
      data = line.rstrip()
      user, passw = data.split(",")
      fer.decrypt(passw.encode()).decode()

def add():
  user = input("Username: ")
  pw = input("Password: ")

  with open('passwords.txt', 'a') as f:
    f.write(user + "," + fer.encrypt(pw.encode()).decode() + '\n')


while True:
  
    mode = input("Would you like to add a new password or view existing ones? (view, add) press q to quit").lower()
    if mode == "q":
      break
    if mode == "view":
      view()
    elif mode == "add":
      add()
    else:
      print("Invalid Mode")
      continue
