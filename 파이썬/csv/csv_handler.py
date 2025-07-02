line_counter = 0 #파일의 줄 수 세는 변수
data_header = [] #data 필드값 저장 list
customer_list = [] #고객 개별 list 저장하는 list

with open("customers.csv","r") as customer_data: #customer.csv 파일을 customer_data 객체에 저장

    while True: #무한 루프
        data = customer_data.readline() #customer_data에서 한 줄씩 읽어옴
        if not data: break #읽어온 데이터가 없으면 루프 종료
        if line_counter == 0: #첫 번째 데이터는 데이터의 필드
            data_header = data.split(',')
        else:
            customer_list.append(data.split(',')) #일반 데이터는 customer_list에 저장 저장시 ,로 분리
        line_counter += 1

print("header:\t",data_header)  #필드값 출력
for i in range(0,10): #고객 데이터 10개 출력
    print("Data",i,"\t\t", customer_list[i])
print(len(customer_list)) #전체 데이터 크기 출력
