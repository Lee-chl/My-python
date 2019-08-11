g=open('data.txt','r')
e=open('result.txt','w')
for d in g:
      x,z,y,w,s=d.split()
      sum=(int(z)+int(y)+int(w)+int(s))
      avg=sum/4
      e.write(str(sum)+ ' ' +str(avg)+' '+d.strip()+'\n')



g.close()
e.close()
