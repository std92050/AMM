
# coding: utf-8

# In[10]:


from scipy.optimize import curve_fit
import random
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
class Car:
    "sdfsf"

T=5000
l=500 #總長



p2=1 #進車機率
def f(l):
    return l[0]
#排序用的function 可不管
def prob(x):
    a=random.randint(1,10)
    if a<=x*10:
        return True
    else:
        return False
    # x的機率是true 1-x的機率是False
def ini(rho,V_max,d): #初始化道路的程式 d是車子的安全距離
   
    n=int(rho*l/(2*d)) #車子數量由密度 道路長 安全距離所決定 初始的位置會是d的整數倍
    S=[] #儲存某個時間點個個車子的狀態
    
    rad_lis=[]#用來生成隨機位置用的   
    for i in range(0,l):
    
        if i*d>l:
            break
        rad_lis.append(i*d)
    rad_x=random.sample(rad_lis,n)
    
    for i in range(n):
        x=Car()
        x.pos=rad_x[i]
        x.v=random.uniform(0,V_max)
        
        S.append([x.pos,x.v])
    S.sort(key=f) #由位置來排序 第一台車、第二台車....第n台車 
    for i in  range(n):
        if i>0 and S[i]<S[i-1]:
            print("rgdg")
    return S
   
def avg(x): #用來算平均用的
    
    for i in range(len(x)):
        if i==0:
            pass
        else:
            x[i]+=x[i-1]
    return x[len(x)-1]/len(x)

a=np.ndarray.tolist(np.random.normal(3,1.5,3000))
a=list(filter(lambda x:x>0.01,a))
def normal(): #Gaussian sampling
  
    s=random.sample(a,1)
    return s[0]
print("done")



# In[19]:


avgV=[] #個個時刻的平均速度
avgd=0
P=[] #所有時間所有狀態

t=[] #時間(長度和P一樣)
def traffic(rho,V_max,d):
    #n是車子數量 V_max速度上限 d 安全距離
    S=ini(rho,V_max,d)
    V=[] #計算平均速度用的
    global avgd
    avg_d=[]
    for j in range(T):
        
        V1=[]
        #每個時段內發生的事
       
        for i in range(len(S)):
            x=len(S)-1
            t.append(j) 
            P.append(S[x-i][0])
            a=normal()
            
        #每台車的狀況
            if i>0 :
                dx=S[x-i+1][0]-S[x-i][0] #前後車距
                if S[x-i][1]<V_max:
                   
                    if S[x-i][1]+1 <=dx-d : #(1)加速不會超過安全距離的話就+速
                       
                        if dx<=5*d :    #車距(預設5d)不夠大就會出現延遲時間
                            S[x-i][1]+=1/a
                        else:
                            S[x-i][1]+=1
                        
                    if S[x-i][1]>dx-d  :
                        #(2)速度超過安全距離的話就減速至跟距離一樣
                        S[x-i][1]=dx-d
                    if S[x-i][1]>=V_max:
                        S[x-i][1]=V_max
                else: #速度等於上限時
                    if S[x-i][1]>dx-d  :
                        #跟上面一樣
                        S[x-i][1]=dx-d
                    
                    
            if i>0 and S[x-i+1][0]<S[x-i][0]: #debug用的
                            
                print(S[x-i+1][0],S[x-i][0],S[x-i][1],j,i)
                break
            
        
            if i==0 and S[x-i][1]<V_max:
                S[x-i][1]+=1
                if S[x-i][1]>=V_max:
                    S[x-i][1]=V_max
                
                
           
            
           
        for k in range(len(S)):
            S[k][0]+=S[k][1]  #(4)更新車子的位置
            V.append(S[k][1]) #j時刻所有車的速度都丟進來
            V1.append(S[k][1])
            
            
            if S[k][0]>l: #若有車跑出去 大家集體往前移 在家新的車進來
                S.remove(S[len(S)-1])
                for a in range(len(S)):
                    S[a][0]+=d
                S.insert(0,[0,V_max]) 
            
            if k>0: #看一下大家有無保持安全間距
                
                avg_d.append(S[k][0]-S[k-1][0])
                
                if S[k][0]-S[k-1][0]<d:
                    print("no!",j,k,S[k][0],S[k-1][0],S[k-1][1])
            
        
        avgV.append(avg(V1)) #j時刻的平均速度
      
        
        
    avgd=avg(avg_d)
      
                
         
    
    avg_V=avg(V) #每個n對應到的平均速度
    
    return avg_V 
P=[]
t=[]
traffic(0.3,5,1.5)
plt.plot(avgV)


# In[16]:


#plt.figure(figsize=(20,25))
#plt.xlim(100,2500)
#plt.scatter(t,P) #X 時間    Y 位置


# In[92]:


#Vbar 和 ro
"""Vbar1=[] #蒐集各個n的平均速度
ro1=[] #密度

for i in range(10,500,10):
    Vbar1.append(traffic(i/500,5,1.5,2))
    ro1.append(i/500)
    print(i)
"""

Vbar2=[]
ro2=[] 

for i in range(10,500,10):
    Vbar2.append(traffic(i/500,5,1.5,3))
    ro2.append(i/500)
    print(i)
Vbar4=[] 
ro4=[] 

for i in range(10,500,10):
    Vbar4.append(traffic(i/500,5,1.5,4))
    ro4.append(i/500)
    print(i)
    
"""Vbar5=[] 
ro5=[] 
for i in range(10,500,10):
    Vbar5.append(traffic(i/500,5,1.5,5))
    ro5.append(i/500)
    print(i)
plt.scatter(ro1,Vbar1)"""
plt.scatter(ro2,Vbar2)
plt.scatter(ro4,Vbar4)
#plt.scatter(ro5,Vbar5)


# In[93]:


#流量對密度
"""q1=[]
for i in range(len(Vbar1)):
    q1.append(Vbar1[i]*ro1[i])
    print(i)"""
q2=[]
for i in range(len(Vbar2)):
    q2.append(Vbar2[i]*ro2[i])
    
q3=[]
for i in range(len(Vbar4)):
    q3.append(Vbar4[i]*ro4[i])
"""q4=[]
for i in range(len(Vbar5)):
    q4.append(Vbar5[i]*ro5[i])
plt.scatter(ro1,q1)"""
plt.scatter(ro2,q2)
plt.scatter(ro4,q3)
#plt.scatter(ro5,q4)


# In[10]:


plt.scatter(ro1,q1) 


# In[84]:


P=[] #所有時間所有狀態

t=[] #時間(長度和P一樣)
avgV=[]
a=traffic(0.3,5,1.5,5)
print(a)

plt.plot(avgV) #平均速度(Y) 時間(X) 


# In[59]:


P=[] #所有時間所有狀態

t=[] #時間(長度和P一樣)
avgV=[]
a=traffic(0.4,5,1.5,3)
print(a)
plt.plot(avgV) #平均速度(Y) 時間(X) 


# In[ ]:





# In[88]:


plt.plot(avgV) #平均速度(Y) 時間(X) 


# In[3]:


#給定密度下 平均速度(Y)和反應時間(X)的圖
Vbar=[]
dt=[]
for i in range(10,110,1):
    Vbar.append(traffic(0.5,5,1.5,i/10))
    dt.append(i/10)
    print(i)


# In[95]:


plt.scatter(dt,Vbar)


# In[ ]:





# In[ ]:





# In[78]:


Vbar4=[] 
ro4=[] 

for i in range(10,500,10):
    avgV=[]
    Vbar4.append(traffic(i/500,5,1.5,4))
    ro4.append(i/500)
    for j in range(1000):
        Vbar4.append(avgV[j])
        ro4.append(i/500)
    print(i)
plt.scatter(ro4,Vbar4)


# In[80]:


q=[]
for i in range(len(Vbar4)):
    q.append(Vbar4[i]*ro4[i])
plt.scatter(ro4,q)


# In[12]:


a=np.random.normal(3,1,1000)
x=random.sample(a,1)


# In[6]:





# In[1]:


get_ipython().system('jupyter nbconvert --to script hw3.ipynb')

