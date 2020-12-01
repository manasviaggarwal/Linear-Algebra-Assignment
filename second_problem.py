#from __future__ import print_function
import os
import sys
import time
start_time=time.time()
import numpy as np
import timeit
Start_time=time.time()
if len(sys.argv)<2 or len(sys.argv)>2:
	print('Invalid agr')
	sys.exit(0)
fname=sys.argv[1]
f1=open(fname,'r')
f=open(os.getcwd()+'/output_problem2.txt', 'w')
k=[int(i) for i in f1.readline().strip().split(" ")]
#a=[float(j) for j in f1.readline().strip().split(" ")]
A=[[]]
A=[[float(j) for j in f1.readline().strip().split(" ")] for i in range(k[0])]
# ainv = np.linalg.inv(A)
# print("numpi ", ainv)
#pd=set()
m=len(A)
n=len(A[0])
max1=0
m1=0
b  = [[0 for x in range(m)] for y in range(n)]
for i in range(0,m):
   
   for j in range(0,n):
      
       for k in range(0,m):
           b[i][j]+= A[i][k] * A[k][j]
for i in range(0,m):
    for j in range(0,n):
        p=A[i][j]
        b[i].append(p)
pd=[]
cs=len(b) #no of rows
rs=len(b[0]) #no of cols
#print(cs,rs)
pivot=0
k1=0
for i in range(0,min(cs,rs)): #will iterate for every possible pivot
	j=i 
	pivot=b[i][i]
	m=i+1
	max1=abs(b[i][i])
	m1=i
	for i3 in range(i+1,cs):
		if(abs(b[i3][i])>max1):
			max1=abs(b[i3][i])
			m1=i3
	b[i],b[m1]=b[m1],b[i]
	if m1!=i:
		pd.append("SWITCH "+str(i+1)+" "+str(m1+1))	
	pivot=b[i][i]
	if pivot!=0:
		for j1 in range(0,rs):
			b[i][j1]=b[i][j1]/float(pivot)
			#b[i][j1]=float("%0.12f" %b[i][j1])	
			jl=float(1/pivot)
			jl=float("%0.3f" %jl)	

		pd.append("MULTIPLY "+str(jl)+" "+str((i+1)))
		for x in range(i+1,cs):
			k1=b[x][i]
			for y in range(0,rs):
				b[x][y]=b[x][y]-b[i][y]*k1
				b[x][y]=float("%0.12f" %b[x][y])
			if k1!=0:
				k1=float("%0.3f" %k1)
				pd.append("MULTIPLY&ADD "+str((-k1))+" "+str(i+1)+" "+str(x+1))
	
	else:
		for j1 in range(i+1,rs-1):
			pivot=b[i][j1]
			max1=pivot
			m1=i
			for i3 in range(i,cs):
				if(b[i3][j1]>max1):
					
					max1=abs(b[i3][j1])
					m1=i3	
			b[i],b[m1]=b[m1],b[i]
			if m1!=i:	
				pd.append("SWITCH "+str(i+1)+" "+str(m1+1))
			pivot=b[i][j1]
			if b[i][j1]!=0:
				for j2 in range(0,rs):
					b[i][j2]=b[i][j2]/float(pivot)
					jl=float(1/pivot)
					jl=float("%0.3f" %jl)
					#b[i][j2]=float("%0.13f" %b[i][j2])	
				pd.append("MULTIPLY "+str(jl)+" "+str(int(i+1)))
				

				for x in range(i+1,cs): 
					k1=b[x][j1]
					for y in range(0,rs):
						b[x][y]=b[x][y]-b[i][y]*k1
						b[x][y]=float("%0.13f" %b[x][y])

					if k1!=0:
						k1=float("%0.3f" %k1)
						pd.append("MULTIPLY&ADD "+str((-k1))+" "+str(i+1)+" "+str(x+1))
				m1=j1
				j1=rs
				break				
		i=m1
check=0
# for i in range(0,cs):
# 	for j in range(0,rs):
# 		b[i][j]=float("%0.3f" %b[i][j])

if i in range(0,n):
	if abs(b[i][i]==0):
		check=1
if check==0:
	t1=0
	for i in range(cs-1,-1,-1):
		for t in range(0,n):
			if(b[i][t]!=0):
				t1=t
				break
		t=t1			
		for b1 in range(i-1,-1,-1):
			i1=b[b1][t]
			for t1 in range(0,rs):
				b[b1][t1]=b[b1][t1]-i1*b[i][t1]
				b[b1][t1]=float("%0.13f" %b[b1][t1])

			if i1!=0:
				i1=float("%0.3f" %i1)	
				pd.append("MULTIPLY&ADD "+str((-i1))+" "+str(i+1)+" "+str(b1+1))
rank1=0


for i in range(cs):
	if(abs(b[i][i])!=0):
		rank1=rank1+1
	
for i in range(0,cs):
	for j in range(0,rs):
		b[i][j]=float("%0.3f" %b[i][j])

if rank1==cs:
	f.write("YAAY! FOUND ONE!"+"\n")
	print("YAAY! FOUND ONE!")
	for i in range(0,cs):
		for jj in range(n,rs):
			f.write(str(b[i][jj])+" ")
			print b[i][jj], 
		f.write("\n")
		print
	for line in pd:
		f.write(str(line)+"\n")
		print line
else:
	f.write("ALAS! DIDN'T FIND ONE!\n")
	print("ALAS! DIDN'T FIND ONE!")
	for line in pd:
		f.write(str(line)+"\n")
		print line
#print time.time()-Start_time
