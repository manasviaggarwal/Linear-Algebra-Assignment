#from __future__ import print_function
import os
import numpy as np 
import sys
import random
import timeit
# def part=one()
b=[]
n1=[]
k=[]
c=[]
a=[]


if len(sys.argv)<3 or len(sys.argv)>3:
	print('Invalid agr')
	sys.exit(0)
fname=sys.argv[2]
f1=open(fname,'r')
	#lines=f1.readlines()
if sys.argv[1]=='-part=one':
	k=[4,4]
	f=open(os.getcwd()+'/output_problem1_part1.txt', 'w')
else:
	k=[int(i) for i in f1.readline().strip().split(" ")]
	f=open(os.getcwd()+'/output_problem1_part2.txt', 'w')
a=[float(j) for j in f1.readline().strip().split(" ")]
b=[[]]
b=[[float(j) for j in f1.readline().strip().split(" ")] for i in range(k[0])]
for i in range(0,k[0]):
	b[i].append(float(a[i])) 

#print(np.linalg.solve(b,a))

c=[float(j) for j in f1.readline().strip().split(" ")]
cs=len(b) #no of rows
rs=len(b[0]) #no of cols
pivot=0
max1=0
m1=0
k1=0

for i in range(0,min(cs,rs)):
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
	pivot=b[i][i]
	if pivot!=0:
		for j1 in range(0,rs):
			b[i][j1]=b[i][j1]/float(pivot)
	
		for x in range(i+1,cs): #make below rows zero
		#A = []
			k1=b[x][i]
			for y in range(0,rs):
				b[x][y]=b[x][y]-b[i][y]*k1

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
			pivot=b[i][j1]
			if b[i][j1]!=0:
				for j2 in range(0,rs):
					b[i][j2]=b[i][j2]/float(pivot)
	
				for x in range(i+1,cs): 
					k=b[x][j1]
					for y in range(0,rs):
						b[x][y]=b[x][y]-b[i][y]*k
				m1=j1
				j1=rs
				break
			
	i=m1
# for i in range(0,cs):
# 	for j in range(0,rs):
# 		b[i][j]=float("%0.2f" %b[i][j])
t1=0
for i in range(cs-1,-1,-1):
	for t in range(0,rs):
		#print(b[i][t])
		if(b[i][t]!=0):
			#print(t)
			t1=t
			break
	t=t1
	#print(t1,i)			
	for b1 in range(i-1,-1,-1):
		i1=b[b1][t]
		#print(i1)
		for t1 in range(0,rs):	
			b[b1][t1]=b[b1][t1]-i1*b[i][t1]

for i in range(0,cs):
	for j in range(0,rs):
		b[i][j]=float("%0.3f" %b[i][j])
# for i in range(0,cs):
# 	   print(b[i][0:rs]) 
rank1=0
for i in range(cs):
	j=i
	while(j<rs and b[i][j]==0):
		j=j+1
	if(j<rs and b[i][j]!=0):
		rank1=rank1+1
rank2=0
pivot_col=[]
free_col=[]
for i in range(cs):
	j=i
	while(j<rs-1 and b[i][j]==0):
		j=j+1
	if(j<rs-1 and b[i][j]!=0):
		pivot_col.append(j)
		rank2=rank2+1

for i in range(0,rs-1):
	if i not in pivot_col:
		free_col.append(i)
if(rank1!=rank2):
	f.write("NOT POSSIBLE, SNAPE IS WICKED!")
	print("NOT POSSIBLE, SNAPE IS WICKED!")
else:
	ex=0
	if(rank2==rs-1):
		for i in range(0,rank2):
			if(int((b[i][rs-1]))>c[i]):
				#print("SNAP IS WICKED!")
				ex=1
		if(ex==0):
			f.write("EXACTLY ONE!\n")
			print("EXACTLY ONE!")
			for i in range(0,rank2):
				f.write(str(b[i][rs-1]))
				f.write(" ")
				print b[i][rs-1],
		else:
			f.write("NOT POSSIBLE, SNAPE IS WICKED!\n")
			print("NOT POSSIBLE, SNAPE IS WICKED!")
	else:
		piv={}
		f.write("MORE THAN ONE!\n")
		print("MORE THAN ONE!")
		# free_col=[]
		itr=0
		piv1={}
		while(itr!=1000):
			for i in free_col:
				piv1[i]=random.randint(1,c[i])
				#piv1[i]=0
		
			for p in range(cs-1,-1,-1):
				for j in range(p,rs-1):
					if b[p][j]!=0:
						piv1[j]=b[p][rs-1]
						for l in range(j+1,rs-1):
							piv1[j]=piv1[j]-(b[p][l]*piv1[l])
						break
			ch=0
			for i in pivot_col:
				if piv1[i]<0 or piv1[i]>c[i]:
					ch=1
			
			for i in range(0,rs-1):
				
				if(ch!=1):
					f.write(str(piv1[i])+" ")
					print piv1[i],
			
			if(ch!=1):
				f.write("\n")
				print 	
				break
			else:
				itr=itr+1
			
		for i in range(cs-1,-1,-1):
			
			if i in pivot_col:
				piv[i]=str(b[i][rs-1])
				for j in range(i+1,rs-1):
					if(b[i][j]!=0):
						piv[i]=piv[i]+"-"+"("+str(b[i][j])+")"+"*X"+str(j)
		j=0
		print '[',
		f.write('[ ')	
		for i in range(cs-1):
			if i not in pivot_col:
				f.write("X")
				f.write(str(i)+", ")
				print "X",i,",",
			else:
				f.write(piv[i]+", ")
				print piv[i],",",
			j=i
		j=j+1
		if j not in pivot_col:
			f.write("X")
			f.write(str(j)+" ")
			print "X",j,
		else:
			f.write(piv[j]+" ")
			print(piv[j])
		print ']'
		f.write(']')
f.close()
sys.exit(0)
f1.close()

