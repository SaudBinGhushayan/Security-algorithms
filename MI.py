#!/usr/bin/env python
# coding: utf-8

# In[84]:


def MI(v, z):
    r1 = z
    r2 = v
    q = r1/r2
    r =  r1-(int(q)*r2)
    t1 = 0
    t2 = 1
    t = t1 -(int(q) * t2)
    print('step#1 q={}  r1={}  r2={}  r={}  t1={}  t2={}  t={}'.format(int(q), r1, r2, r, t1, t2, t))
    counter = 1
    while r > 0:
        r1 = r2
        r2 = r
        q = r1/r2
        r =  r1-(int(q)*r2)
        t1 = t2
        t2 = t
        t = t1-(int(q) * t2)
        print('step#{} q={}  r1={}  r2={}  r={}  t1={}  t2={}  t={}'.format(counter, int(q), r1, r2, r, t1, t2, t))
        counter += 1
    if r2 == 1:
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t
        print('       r1={}  r2={}  t1={}  t2={}'.format(r1, r2, t1, t2,))
        print('The mulitplication Inverse is possible and your value is {} '.format(t1))
    else:
        r1 = r2
        r2 = r
        t1 = t2
        t2 = t
        print('       r1={}  r2={}  t1={}  t2={}'.format(r1, r2, t1, t2,))
        print('The Multiplication inverse is not possible')

