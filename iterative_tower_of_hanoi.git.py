
A=[3,2,1]
B=[]
C=[]

last_disk=-1
def move(s,d):
    global last_disk
    if len(s)==0:
       return
    if last_disk==s[-1] or (len(d) and d[-1]<s[-1])  :
       return

    d+=  [s[-1]]  # move top disk in source to distination 
    last_disk=s[-1] # save last disk number 
    del s[-1] # delete top disk from source list
    
    print A,B,C 
      #source -> distination
while len(A)!=len(C):

    
    if len(A) % 2 !=0 :
       move(A,C)
    else:
       move(A,B)

   
    if len(B) % 2 !=0 :
       move(B,C)
    else:
       move(B,A)

  
    if len(C) % 2 !=0 :
       move(C,B)
    else:
       move(C,A)

        


