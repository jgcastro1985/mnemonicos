import random
import binascii
import hashlib

coin = 3
num_bin = ''
stop = ''

while len(num_bin) < 256:
	while coin != 0 and coin != 1:
		if stop == 'y':
			coin = random.randint(0,1)
		else:
			coin = int(input('A moeda caiu de qual lado? Digite 0 para "cara", 1 para "coroa" ou 2 para parar: '))
			if coin == 2:
				coin = random.randint(0,1)
				stop = 'y'
	num_bin += str(coin)
	coin = 3

num_hex = hex(int(num_bin, 2))[2:].zfill(64)
random_bin = binascii.unhexlify(num_hex)
random_hex = binascii.hexlify(random_bin)

hashed_sha256 = hashlib.sha256(random_bin).hexdigest()

bin_result = (
	bin(int(random_hex, 16))[2:].zfill(256)
	+ bin(int(hashed_sha256, 16))[2:].zfill(256)[:8]
)

index_list = []
with open("english.txt", "r", encoding="utf-8") as f:
	for w in f.readlines():
		index_list.append(w.strip())

wordlist = []
for i in range(len(bin_result) // 11):
	index = int(bin_result[i*11 : (i+1)*11], 2)
	wordlist.append(index_list[index])
	
phrase = " ".join(wordlist)
print('\nMnemônicos: ' + phrase)
