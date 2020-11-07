import csv
data=[]
with open('data.csv',encoding='utf8') as file:
    csvreader=csv.reader(file)
    for row in csvreader:
        temp=[]
        temp.extend([row[1].lower(),(row[0].split(',')[0])])
        data.append(temp)

choice='y'
while choice=='y' or choice=='yes':
    word = input('enter your word = ').lower()
    found=0
    for i in range(len(data)):
        if word==data[i][0]:
            found = found + 1
            print(f"{word}  :  {data[i][1]}")
    if found==0:
        print('no such word found in our DB\nkindly search for another word')
    print(f"press (y) to continue and (n) to exit")
    choice = input('your choice = ').lower()

    