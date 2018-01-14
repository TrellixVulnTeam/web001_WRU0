#-*-coding:utf-8-*-
GoodsList = [
    {"苹果":800},
    {"华为":500},
    {"Vivo":200},
    {"小米":100},
    {"魅族":50},
    {"金立":10},
]
ShopingList = []
print("欢迎登录购物系统")
print()
#Salary = input('请输入您的工资进行购物操作:')
print("想要显示所有商品，请输入p")
while True:
    Choice_Goods = input("请选择你想要买的商品:")
    if Choice_Goods == "p" or Choice_Goods == "P":
        for i in GoodsList:
            print(GoodsList.index(i),i)
    elif Choice_Goods == 1:
        Salary = Salary - 800
        ShopingList.append("苹果")

