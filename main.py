#task1
print('task1')
def list1(list):
    listp = []
    print(list)
    for x in list:
        listp.append(-x)
    return listp

print(list1([1,2,3,4,5,6,7]))
print(list1([1,-2,3,4,5,-6,7]))
print('\n')


#task2
print('2-task')
print("siz bu yerdan o'zingiz yoqtirgan animeni topishingiz mumkun, yozish tartibi ms:your_name")
inp1 = input('qidiruv: ')
def ind(lst2):
    print(lst2)
    if inp1 in lst2:
        x = lst2.index(inp1)
        return f"siz kiritgan anime {x} indexda joylashgan!"

    return 'mavjud emas'

print(ind(['your_name','silent_voice','monster','vinland_saga','berserk','jujuste_kaisen','evangelion']))
print('\n')


#task3
print('3-task')
print("siz bu yerda kiritgan soningizni listda bor yoki yo'q bilishingiz mukun! ms:3 ")
inp2 = int(input('son:'))
def tp(list3):
    print(list3)
    if inp2 in list3:
        return True
    else:
        return False

print(tp([1,2,3,4,5,6,7,8,9,10]))
print(tp([1,2,2,1,1]))
print(tp([1,1,1,3]))
print(tp([]))
print('\n')


#task4
print('4-task')

def list_limit(list_l):
    print(list_l)
    for x in list_l:
        if x < 100:
            return True
        elif x > 100:
            return False


print(list_limit([5,57]))
print(list_limit([2,15]))
print(list_limit([0]))