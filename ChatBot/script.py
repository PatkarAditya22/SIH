dis = ['allergy','anemia','cold','asthma','alzheimers','pregnancy','hyperthyroid','hypothyroid','diabetes','HIV AIDS']
f = open("food.txt",'r')
f1 = open("newf.txt",'w')
f2 = open("ques.txt",'r')
t = "\"" + "tag" + "\"" + ":"
p = "\"" + "pattern" + "\"" + ":"
r = "\"" + "responses" + "\"" + ":"

prevent = f.readlines()
quest = f2.readlines()
f.close()
f2.close()
for i in range(len(dis)):
    sec_half = ""
    for x in quest:
        half = "\"" + str(x) + " " + str(dis[i]) + "\"" + ","
        sec_half = sec_half + half
    final = "{" + str(t) + "\"" + "foods to be avoided in " + str(dis[i]) + "\"" + " ," + "\n" + str(p) + " [" + sec_half + "]" + "," + "\n" + str(r) + " [[" +  "\"" + str(prevent[i]) + "\"" + "]]" + "\n" + "}," + "\n"
    f1.write(final)

f1.close()



