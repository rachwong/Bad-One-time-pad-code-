
alphabet = ('0x41','0x42', '0x43', '0x44', '0x45', '0x46', '0x47',
            '0x48','0x49','0x4A','0x4B','0x4C','0x4D','0x4E','0x4F',
            '0x50','0x51','0x52','0x53','0x54','0x55','0x56','0x57','0x58',
            '0x59','0x5A', '0x20', '0x2E')


alphabet2 = ("0x61","0x62","0x63","0x64","0x65","0x66","0x67","0x68","0x69","0x6A",
             "0x6B","0x6C","0x6D","0x6E","0x6F","0x70","0x71","0x72",
             "0x73","0x74","0x75","0x76","0x77","0x78","0x79","0x7A",'0x20', '0x2E')

cipher = ('0x7F', '0x7B', '0x6D', '0x7B', '0x6A', '0x7E', '0x6A')    
cipher2 = ('0xC8', '0xC4', '0xC9', '0xC0', '0xCE', '0xD4', '0xCE')
cipher3 = ('0x4F', '0x55', '0x50', '0x4D', '0x54', '0x57', '0x54')
cipher4 = ('0x8D', '0x84', '0x9B', '0x9C', '0x8D', '0x8E', '0x8D')
cipher5 = ('0xD0', '0x83', '0xD0', '0x9C', '0x9F', '0x99', '0xD0')

counter = 0
for count in alphabet: #for each letter?
    key = hex(int(cipher[0], 16) ^ int(alphabet[counter], 16))
    key2 = hex(int(cipher2[0], 16) ^ int(alphabet2[counter], 16))
    key3 = hex(int(cipher3[0], 16) ^ int(alphabet2[counter], 16))
    key4 = hex(int(cipher4[0], 16) ^ int(alphabet2[counter], 16))
    key5 = hex(int(cipher5[0], 16) ^ int(alphabet2[counter], 16))
    #print('key: ' + key)
    #print('Alphabet letter: ' + chr(int(alphabet[counter], 16)) + ' and '
          #+ chr(int(alphabet2[counter], 16)))
    print('Alphabet letter: ' + chr(int(alphabet2[counter], 16)))
    list1 = []
    counter2 = 0
    print('Key: ' + key + ' ' + key2 + ' ' + key3 + ' ' + key4 + ' ' + key5)
    for item in cipher: # printing the corrosponding letter 
        xor = hex(int(key, 16) ^ int(item, 16))
        letter1 = chr(int(xor, 16))
        
        list1.append(letter1)
        
        
        xor2 = hex(int(key2, 16) ^ int(cipher2[counter2], 16))
        letter2 = chr(int(xor2, 16))
        
        xor3 = hex(int(key3, 16) ^ int(cipher3[counter2], 16))
        letter3 = chr(int(xor3, 16))

        xor4 = hex(int(key4, 16) ^ int(cipher4[counter2], 16))
        letter4 = chr(int(xor4, 16))

        xor5 = hex(int(key5, 16) ^ int(cipher5[counter2], 16))
        letter5 = chr(int(xor5, 16))
        
        #if letter1.isalpha() == True and letter2.isalpha() == True:
        print(letter1 + ' ' + letter2 + ' ' + letter3 + ' ' + letter4 + ' ' + letter5)
        
        #else:
            #print('')

            
        print ('----')
        
        
        #print(chr(int(xor2, 16)))
        #for char in alphabet:
            
        counter2 += 1
    #print(list1)
    counter += 1 
