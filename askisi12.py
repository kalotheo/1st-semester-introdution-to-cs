#set a list of the lower english alphabet
Alist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#open file keimeno.txt
f = open("text.txt", "r")

#reads it and then makes it a list
text=f.read()
aList=list(text)

#make all characters in the list lower
list_lower = []
for x in aList:
	list_lower.append(x.lower())

#count all times each letter is used in the list
a = aList.count('a')
b = aList.count('b')
c = aList.count('c')
d = aList.count('d')
e = aList.count('e')
f = aList.count('f')
g = aList.count('g')
h = aList.count('h')
i = aList.count('i')
j = aList.count('j')
k = aList.count('k')
l = aList.count('l')
m = aList.count('m')
n = aList.count('n')
o = aList.count('o')
p = aList.count('p')
q = aList.count('q')
r = aList.count('r')
s = aList.count('s')
t = aList.count('t')
u = aList.count('u')
v = aList.count('v')
w = aList.count('w')
x = aList.count('x')
y = aList.count('y')
z = aList.count('z')

#sum the times used
sum=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z

#make each variable float, divide it with sum
#and then multiply it with 100 to give percentage of each letter
percent_a=(float(a)/float(sum))*100
percent_b=(float(b)/float(sum))*100
percent_c=(float(c)/float(sum))*100
percent_d=(float(d)/float(sum))*100
percent_e=(float(e)/float(sum))*100
percent_f=(float(f)/float(sum))*100
percent_g=(float(g)/float(sum))*100
percent_h=(float(h)/float(sum))*100
percent_i=(float(i)/float(sum))*100
percent_j=(float(j)/float(sum))*100
percent_k=(float(k)/float(sum))*100
percent_l=(float(l)/float(sum))*100
percent_m=(float(m)/float(sum))*100
percent_n=(float(n)/float(sum))*100
percent_o=(float(o)/float(sum))*100
percent_p=(float(p)/float(sum))*100
percent_q=(float(q)/float(sum))*100
percent_r=(float(r)/float(sum))*100
percent_s=(float(s)/float(sum))*100
percent_t=(float(t)/float(sum))*100
percent_u=(float(u)/float(sum))*100
percent_v=(float(v)/float(sum))*100
percent_w=(float(w)/float(sum))*100
percent_x=(float(x)/float(sum))*100
percent_y=(float(y)/float(sum))*100
percent_z=(float(z)/float(sum))*100

print ("Statistics of each letter")
#prints the Statistics
print ("a:",percent_a ,"%")
print ("b:",percent_b ,"%")
print ("c:",percent_c ,"%")
print ("d:",percent_d ,"%")
print ("e:",percent_e ,"%")
print ("f:",percent_f ,"%")
print ("g:",percent_g ,"%")
print ("h:",percent_h ,"%")
print ("i:",percent_i ,"%")
print ("j:",percent_j ,"%")
print ("k:",percent_k ,"%")
print ("l:",percent_l ,"%")
print ("m:",percent_m ,"%")
print ("n:",percent_n ,"%")
print ("o:",percent_o ,"%")
print ("p:",percent_p ,"%")
print ("q:",percent_q ,"%")
print ("r:",percent_r ,"%")
print ("s:",percent_s ,"%")
print ("t:",percent_t ,"%")
print ("u:",percent_u ,"%")
print ("v:",percent_v ,"%")
print ("w:",percent_w ,"%")
print ("x:",percent_x ,"%")
print ("y:",percent_y ,"%")
print ("z:",percent_z ,"%")

#create a new list with the percentages of each letter
blist=[percent_a,percent_b,percent_c,percent_d,percent_e,percent_f,percent_g,percent_h,percent_i,percent_j,percent_k,percent_l,percent_m,percent_n,percent_o,percent_p,percent_q,percent_r,percent_s,percent_t,percent_u,percent_v,percent_w,percent_x,percent_y,percent_z]

#create two new empty lists winthout percentage
dlist=[]
elist=[]

#check each letter if it is the most or less frequent
for i in range(len(blist)):

	if blist[i]!=0:
		dlist.append(blist[i])
		elist.append(Alist[i])

max_percent=max(dlist)
min_percent=min(dlist)
position_max=dlist.index(max_percent)
position_min=dlist.index(min_percent)

#list with the letter and the biggest number
flist=[elist[position_max],max_percent]

#list with the letter and the smallest number
glist=[elist[position_min],min_percent]

print ("\n", flist,glist)
#replace the most frequent character with the less used character
for i in range(len(list_lower)):

	if list_lower[i]==flist[0]:
		list_lower.remove(list_lower[i])

		list_lower.insert(i,glist[0])
	elif list_lower[i]==glist[0]:
		list_lower.remove(list_lower[i])

		list_lower.insert(i,flist[0])

#upper all the letters of the text
list_upper=[]
for x in list_lower:
	list_upper.append(x.upper())

#join method to get the elements of the list out of it
print ("\n"," ".join(list_upper))
