#採用4-4部分方法 如果j的分數有合格(分數==j長度),表示i和j顛倒比對符合
wordlist=['5566', '6655', 'boltzmann','erw', 'gibbs', 'hilbert',
'lagrange', 'laplace', 'q2e342qe4', 'sbbig', 'treblih','wre' ]
reverse_group=[]
for i in wordlist:
    for j in wordlist:
        score=0
        if not len(i)==len(j):
            continue
        for k in range(len(i)):
            
            if i[k]==j[len(j)-k-1]:
                pass
            else:
                break
            score=score+1
        if score==len(j):
            reverse_group.append(i)
        

