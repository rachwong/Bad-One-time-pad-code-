import enchant 
d = enchant.Dict("en_US")
n=2
l1='7FC84F8DD054A217B29110BD3B02A4AEFF2E5E3A92B4D9C0AC44'
l1x=[l1[i:i+n] for i in range(0, len(l1), n)]
l2='7BC455848307A01FB8930FF83044E5A5E16B537292ECC7D2A144'
l2x=[l2[i:i+n] for i in range(0, len(l2), n)]
l3='6DC9509BD04EB956B7D410F83716E1BDAD2F487982A1D5DDAC44'
l3x=[l3[i:i+n] for i in range(0, len(l3), n)]
l4='7BC04D9C9C42AC04B99A17BD2305F7E9FE24076983A5D3D8A144'
l4x=[l4[i:i+n] for i in range(0, len(l4), n)]
l5='6ACE548D9F49AF56BD9A0CEA2744E5A5E16B547F94BED5C7AB44'
l5x=[l5[i:i+n] for i in range(0, len(l5), n)] 
l6='7ED4578E9955AF56BF8743F53105F6ADAD22493A99A3C2C7B044'
l6x=[l6[i:i+n] for i in range(0, len(l6), n)]
l7='6ACE548DD045A304B28743FE350AA4BAE226426884ADC5DFAC44'
l7x=[l7[i:i+n] for i in range(0, len(l7), n)]


char1=[0x39]
First=[0x3d,0x3c,0x3a,0x39,0x38,0x2f,0x2e,0x2c,0x2b,0x29,0x28]
char2=[0xac,0xad,0xa1,0xa2,0xa3,0xa5,0xa6,0xa7]
char3=[0x27,0x26,0x25,0x24,0x23,0x22,0x21,0x20,0x3f,0x3e,0x3d,0x3c,
       0x3b,0x3a,0x39,0x38]
char4=[0xef,0xe9,0xe8,0xeb,0xea,0xfd,0xfe,0xf4,0xf7]
for one in range(len(char1)):
    key = one
    letter=int('0x'+l5x[0],16)^char1[one]
    
    nextletter=int('0x'+l2x[0],16)^char1[one]
    letter= chr(letter)
    nextletter= chr(nextletter)
    
    print('trying this letter: '+ letter)
    line=[letter]
    line2=[nextletter]
    for two in range(len(char2)):
        letter2=int('0x'+l5x[1],16)^char2[two]
        letter2= chr(letter2)
        #print(letter+letter2)

        nextletter2=int('0x'+l2x[1],16)^char2[two]
        nextletter2= chr(nextletter2)
        #print(nextletter+nextletter2)
        
        for three in range(len(char3)):
            letter3=int('0x'+l5x[2],16)^char3[three]
            letter3= chr(letter3)
            #print(letter+letter2+letter3)
            
            nextletter3=int('0x'+l2x[2],16)^char3[three]
            nextletter3= chr(nextletter3)
            #print(nextletter+nextletter2+nextletter3)
            #print('----')
            
            for four in range(len(char4)):
                letter4=int('0x'+l5x[3],16)^char4[four]
                letter4= chr(letter4)

                nextletter4=int('0x'+l2x[3],16)^char4[four]
                nextletter4= chr(nextletter4)

                if d.check(str(letter+letter2+letter3+letter4)) == True:
                    print('----')
                    print(letter+letter2+letter3+letter4)

                
                if d.check(str(nextletter+nextletter2+nextletter3+nextletter4)) == True:
                    print(nextletter+nextletter2+nextletter3+nextletter4)
                    print('----')
    
    print('-----')
    
    
line=[]
for i in range(len(keys)):
    letter= int('0x'+l1x[i],16)^keys[i]
    line.append(chr(letter))
print(''.join(line))



##line=[]
##for i in range(len(keys)):
##    letter= int('0x'+l2x[i],16)^keys[i]
##    line.append(chr(letter))
##print(''.join(line))
##line=[]
##for i in range(len(keys)):
##    letter= int('0x'+l3x[i],16)^keys[i]
##    line.append(chr(letter))
##print(''.join(line))
##line=[]
##for i in range(len(keys)):
##    letter= int('0x'+l4x[i],16)^keys[i]
##    line.append(chr(letter))
##print(''.join(line))
##line=[]
##for i in range(len(keys)):
##    letter= int('0x'+l5x[i],16)^keys[i]
##    line.append(chr(letter))
##print(''.join(line))
##line=[]
##for i in range(len(keys)):
##    letter= int('0x'+l6x[i],16)^keys[i]
##    line.append(chr(letter))
##print(''.join(line))
##line=[]
##for i in range(len(keys)):
##    letter= int('0x'+l7x[i],16)^keys[i]
##    line.append(chr(letter))
##print(''.join(line))
##line=[]
