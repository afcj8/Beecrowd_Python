a = str(input())    # Animal 1
b = str(input())    # Animal 2
c = str(input())    # Animal 3

if (a == 'vertebrado'):
    if (b == 'ave'):
        if (c == 'carnivoro'):
            print('aguia')
        else:
            print('pomba')
    else:
        if (c == 'onivoro'):
            print('homem')
        else:
            print('vaca')
else:
    if (b == 'inseto'):
        if (c == 'hematofago'):
            print('pulga')
        else:
            print('lagarta')
    else:
        if (c == 'hematofago'):
            print('sanguessuga')
        else:
            print('minhoca')