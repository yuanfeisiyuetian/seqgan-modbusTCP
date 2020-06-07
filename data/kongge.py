with open('train00.txt', 'r+') as filehandler:
    with open('train.txt','w') as filehandler2:
        filehandler2.write(''.join([f+' ' for fh in filehandler for f in fh]))