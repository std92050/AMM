#從word.txt抓出來再排序
def word():
    words=open('word.txt')
    group=[]
    for line in words:
        group.append(line[:-1])
    group.sort()
    return group

#有在group裡就回答in
def in_bisect(words2):
    group=word()
    if words2 in group:
        print('in')
    elif words2=='END':
        pass
    else:
        print('not in')





