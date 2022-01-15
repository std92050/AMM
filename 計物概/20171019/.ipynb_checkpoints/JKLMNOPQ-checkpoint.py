prefixes = 'JKLMNOPQ'
suffix = 'ack'
index=0
while index<len(prefixes):

    if index==5 or index==7:
        print(prefixes[index]+'u' + suffix)
    else:
        print(prefixes[index]+ suffix)
    index=index+1
