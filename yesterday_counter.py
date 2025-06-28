f = open("yesterday.txt", "r")
yesterday_lyrics = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyrics +=  line.strip() + "\n"
f.close()
#대소문자 구분 제거 
n_of_yesterday_upper = yesterday_lyrics.count("YESTERDAY")
n_of_yesterday_lower = yesterday_lyrics.count("yesterday")
print(f"Number of a Word 'Yesterday' : {n_of_yesterday_upper}, 'yesterday' : {n_of_yesterday_lower}")