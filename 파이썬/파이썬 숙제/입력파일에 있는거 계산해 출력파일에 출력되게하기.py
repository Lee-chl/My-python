fa=open('입력파일.txt','r')
aa=open('출력파일.txt','w')
list=[]
aa.write("성적출력\n")
aa.write("2017.11.14"+" "+" 이예지\n")
for b in fa:
    no=b[0:3]
    name=b[3:18]
    kor=int(b[18:21])
    eng=int(b[21:24])
    mat=int(b[24:27])
    sum=kor+eng+mat
    ave=sum/3
    t='%3d %3s %-15s %3d %3d %3d %6.2f' % (sum,no,name,kor,eng,mat,ave)
    

    list.append(t)   
list.sort(reverse=True)



option=1
for choice in list:
    aa.write(str(option)+'등'+' '+choice+'\n') 
    option+=1

fa.close()
aa.close()

