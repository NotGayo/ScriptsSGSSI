import sys

msgenc1 = sys.argv[1]
print(msgenc1)
msg_enc = msgenc1.replace(" ", "").replace(",","").replace(".","").replace("1","").replace("2","").replace("3","").replace("9","").replace("6","").replace("4","").replace("7","")
length_msg = len(msg_enc)
abecedario = ["E", "A", "O", "L", "S", "N", "D", "R", "U", "I", "T", "C", "P", "M", "Y", "Q", "B", "H", "G", "F", "V", "J", "Z", "X", "K", "W"]

conversion_dictionary = {
    
}

for letter in msg_enc:
	appearances = ""
	if letter in conversion_dictionary:
		appearances = conversion_dictionary.get(letter)
		conversion_dictionary.update({letter : appearances+1})
	else:
		conversion_dictionary.update({letter : 1})

sorted_dict = dict(sorted(conversion_dictionary.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict)
print(length_msg)
i= 0
for key in sorted_dict:
	
	print(key ,"==>", abecedario[i],":",(conversion_dictionary.get(key)/(length_msg+14))*100)
	i+=1
