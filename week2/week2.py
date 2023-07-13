print("===Task1===")
def find_and_print(messages):
    # write down your judgment rules in comments
    # 確定超過17歲的條件定義:18 years old、college student(假定是一般沒有跳級的大學生)、台灣法定年齡為18歲、下周可以投票給美國總統，代表他快要滿18歲(或是已經滿18歲)，那代表也超過17歲
    #不能確定年齡：只有打招呼的人(Mary, Jenny)
    
    # your code here, based on your own rules
    for name in messages:
        if "18 years old" in messages[name]:
            print (name)
        elif "college student"in messages[name]:
            print (name)
        elif "legal age in Taiwan"in messages[name]:
            print (name)
        elif "vote for Donald Trump next week"in messages[name]:
            print (name)
    
find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})





print("===Task2===")
def calculate_sum_of_bonus(data):
    # write down your bonus rules in comments
    # your code here, based on your own rules
    employees=data["employees"]
    bonustotal=0

    for employee in employees:
        salary=employee["salary"]
        performance=employee["performance"]
        role=employee["role"]

        if isinstance(salary,str) and salary.endswith("USD"):
            salary = int(salary[:-3]) * 30
        elif isinstance(salary, str) and "," in salary:
            salary = int(salary.replace(",", ""))
        else:
            salary = int(salary)
    #根據績效計算獎金比例:
    #"above average"：獎金比例為薪水的 10%。
    #"average"：獎金比例為薪水的 5%。
    #"below average"：獎金比例為薪水的 2%。
        bonuspercentage=0
        if performance =="above average":
            bonuspercentage += 0.1
        elif performance =="average":
            bonuspercentage += 0.05
        elif performance =="below average":
            bonuspercentage += 0.02
    #根據職位加給獎金:
    #"Engineer"：+新台幣800
    #"CEO"：+新台幣1000
    #"Sales"：+新台幣500
        rolebonus=0
        if role=="Engineer":
            rolebonus+=800
        elif role=="CEO":
            rolebonus+=1000
        elif role=="Sales":
            rolebonus+=600
        
        bonus=salary*bonuspercentage+rolebonus
        bonustotal+=bonus

    print(int(bonustotal))

calculate_sum_of_bonus({
    "employees":[
    {
    "name":"John",
    "salary":"1000USD",
    "performance":"above average",
    "role":"Engineer"
    },
    {
    "name":"Bob",
    "salary":60000,
    "performance":"average",
    "role":"CEO"
    },
    {
    "name":"Jenny",
    "salary":"50,000",
    "performance":"below average",
    "role":"Sales"
    }
    ]
    }) # call calculate_sum_of_bonus function

print("===Task3===")
def func(*data):
# your code here
    middleNameCount={}

    for name in data:
        nameParts=name.split(" ")
        middleName=nameParts[0][1]

        if middleName in middleNameCount:
            middleNameCount[middleName]['count']+=1
            middleNameCount[middleName]['name']=None

        else: 
            middleNameCount[middleName] = {
                'count': 1,
                'name': name
            }
    hasUniqueMiddleName = False

    for middleName, info in middleNameCount.items():
        if info['count'] == 1 :
            fullName = info['name']
            print(fullName)
            hasUniqueMiddleName = True

    
    if not hasUniqueMiddleName:
        print("沒有")


func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有




print("===Task4===")
def get_number(index):
# your code here
    n=0
    for i in range(1,index+1):
        if i%2==1:
            n+=4
        else: n-=1
    
    print(n)

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15
