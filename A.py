with open("write.txt","w") as f:
    f.write(''.join(__import__('random').choice('\u2571\u2572') for i in range(50*24)))