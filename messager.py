import os

# number is an  10 digit integer - not string - of recipient
# message is a string containing message
def sendMessage(number, message):
    cmd = f'osascript sendMessage.applescript {number} {message}'
    os.system(cmd)

#insert file path of txt file here
file = '<filepath>'

f = open(file, 'r')

wholetxt = f.read()

#clean string of apostrophes and new lines
cleantxt = wholetxt.replace("'", "").replace("\n", " ")

words = cleantxt.split()

#phone number of recipient
phone_num = 1234567890

for word in words:
    sendMessage(phone_num, word)

f.close()