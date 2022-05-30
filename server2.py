msg = input("please enter your message here:")
#create a key taht you'll use to encrypt the message

key = "abcdefghijklmnopqrstuvwxyz0123456789 !"
#reverse the key so the output can read the key from last to end order

val = key[:: -1]

e_msg = dict(zip(key , val))
#print(e_msg)

enc_msg = "".join([e_msg[words] for words in msg.lower()])
print((enc_msg))
derripter = dict(zip(val , key))
dec_msg = "".join([e_msg[words]for words in msg.lower()])