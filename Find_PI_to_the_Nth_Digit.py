import math

print('Note : Please choose number between 0 to 50!')
a = True
b = True
while a:
    try:
        b = True
        inpPI = int(input('Please Enter number between 0 to 50 PI values: '))
        if (inpPI > 0 and inpPI < 50):
            print ('PI value {:0.{}f}'.format(math.pi,inpPI))
            while b:
                st = str(input('Press q for exit and r for rerun'))
                if st=='q':
                    print('Thanks you visiting !')
                    a = False
                    break
                elif st=='r':
                    b = False
                else:
                    print('Press q for exit and r for rerun')
        else:
            print('Please enter number only 0 to 50')
            continue
    except:
        pass
    
