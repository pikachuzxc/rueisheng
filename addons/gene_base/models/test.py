# -*- coding:utf-8 -*-

# 方法part1
# 1.如果有重複命名的方法會以最後面的方法為主
# 2.在方法內傳入的變數可以帶入預設值，會提升你方法的安全度和各容易閱讀
# def pet(pet='dog'):
# print (pet())

# 3.方法除了可以傳入變數之外，還能傳入方法
# 4.在使用變數回傳不能使用在方法宣告的變數，必須在方法外宣告才能回傳該變數
# 5.如果在方法內打上 """  我是大明星 """，可以用 print(方法.__doc__) 把這段文字叫出來

# ----------------------------------------------------
# 方法part2
# 6.如果在方法輸入的引數宣告像*args，*nums，後面所有的值(型別不限)會進入其中並變成一個tuple，
# def fun1(num1,num2,*args):
# print(fun1(4,5,6,7,8,9))
# -> args = (6,7,8,9)
# 7.在方法輸入宣告像這樣的引數 **kwargs，**kwargs會變成一個dict存一堆key和value
# def special_greeting(**kwargs):
#     return f"{kwargs['David']} David!"
# special_greeting(David='Hello')

# def display_names(first,second):
# name = {"first":"colt","second":"Rusty"}
# display_names(**name)

#-------------------------------------------
# lambda用來丟引述後回傳一個值，簡單方法的寫法
# add_values = lambda x,y: x+y
# print(add_values(10,20))

# map是能夾帶方法和一個引數的寫法

#範例1:

# l = [1,2,3,4]
# doubles = list(map(lambda x: x*2,l))
# --> doubles = [2,4,6,8]

#範例2:
# names = [
#     {'first':'Rusty','last':'Steele'},
#     {'first':'Colt','last':'Steele'},
# ]
# first_names = list(map(lambda x: x['first'], names))
# --> first_names = ['Rusty','Colt']

# filter是種過濾的方法，透過lambda方法下條件並只讀取條件為真的值

# l = [1,2,3,4]
# evens = list(filter(lambda x: x % 2 == 0, 1))
# --> evens = [2,4]

#額外:一個複雜的寫法filter和map一起

#範例:

# name = ['Lassie','Colt','Rusty']
# list(map(lambda name: f"Your instructor is {name}",filter(lambda value:len(value) < 5, name)))
# --> ['Your instructor is Colt']

# all:只要裡面的值為真值 all(num) = True ，否則 all(num) = False
#
# all([0,1,2,3]) --> False
#
# any:裡面沒有值為false，有值為真

# any([0,1,2,3]) --> True

def is_all_strings(lst):
    return all([type(l) == str for l in lst])


# --------------------------------------------------------------------------------

# -----以下需要用python 3 來驗證------

# 1

# def add(a,b):
#     return a+b
# def math (a,b,fn = add):
#     return fn(a,b)

# 我忘了如何得到使用者key的值和print 變數



