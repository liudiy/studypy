import People
import Monster
import Wuqi


def init():
    monster1 = Monster.Monster(200, 99, 5, 10000)
    monster2 = Monster.Monster(150, 0, 7, 230)
    monster3 = Monster.Monster(220, 0, 2, 250)
    monsters = [monster1, monster2, monster3]

    zhangsan = People.People('zhangsan', 100, 100, 230, 300)
    lisi = People.People('lisi', 100, 100, 234, 260)
    wanger = People.People('wanger', 100, 100, 123, 270)
    users = {'zhangsan': zhangsan, 'lisi': lisi, 'wanger': wanger}
    return monsters, users

def login(username, password):
    if password == '111':
        print('The password is wrong.')
    else: return username


def get_people_inf(username, users):
    return users[username]


def xunhuan(people:People, monsters):
    # 所有怪兽和某一个人战斗，人死了print end，没死直到战斗完
    for monster in monsters:
        shengyu = people.shengming - monster.gongjili_dao
        print(people.name + ':' + str(monster.gongjili_dao) + ', shengyu:' + str(shengyu))
        if shengyu <= 0:
            print(people.name + 'END')

def shegnji(people,monsters, XP_people):
    for monster in monsters:
        XP_people1 = monster.XP_monster + XP_people
        print(XP_people1)
        if XP_people1 >= 34 and  XP_people1 < 35:
            people.gongjili1 =  people.gongjili + 5
            people.shengming1 = people.shengming + 10
            people.fangyu1 = people.fangyu + 20
            print(people.name + ',攻击力:' + str(people.gongjili1) + ',生命:' + str(people.shengming1) + ',防御:' + str(people.fangyu1))
        elif XP_people1 >= 43:
            people.gongjili1 = people.gongjili + 6
            people.shengming1 = people.shengming + 20
            people.fangyu1 = people.fangyu + 30
            print(people.name + ',攻击力:' + str(people.gongjili1) + ',生命:' + str(people.shengming1) + ',防御:' + str(
                people.fangyu1))
        elif XP_people1 >= 56:
            people.gongjili1 = people.gongjili + 7
            people.shengming1 = people.shengming + 23
            people.fangyu1 = people.fangyu + 25

        else:
            print(people.name + ',攻击力:' + str(people.gongjili) + ',生命:' + str(people.shengming) + ',防御:' + str(
            people.fangyu))




def qianghua(people):
    knife = Wuqi.Wuqi(20,100)
    gun = Wuqi.Wuqi(30,200)
    weapon_AD = {'knife':20,'gun':30}
    weapon_money = {'knife':100, 'gun ':200}
    AD1 =  weapon_AD['knife'] + people.gongjili
    money_rest1 = people.money - weapon_money['knife']
    AD2 =  weapon_AD['gun'] + people.gongjili
    money_rest2 = people.money - weapon_money['gun ']
    return AD1, money_rest1, AD2, money_rest2


def xuanze(shuru, people, AD1, AD2, money_rest1, money_rest2):
    if shuru == 'dao':
        print(people.name + '攻击力:' + str(AD1)+ ',剩余金钱:' + str(money_rest1))
    else:
        print(people.name + '攻击力:' + str(AD2)+ ',剩余金钱:' + str(money_rest2))


def display_info(people:People):
    print("姓名：" + str(people.name))
    print("攻击力：" + str(people.gongjili))
    print("生命值：" + str(people.shengming))
    print("防御力：" + str(people.fangyu))

def main():
    monsters, users = init()
    shuru = '1'
    username = login("lisi", "11")
    XP_people = 0
    if username is not None:
        people = get_people_inf(username, users)
        display_info(people)
        xunhuan(people, monsters)
        shegnji(people, monsters, XP_people)
        AD1, money_rest1, AD2, money_rest2 = qianghua(people)
        xuanze(shuru, people, AD1, AD2, money_rest1, money_rest2)
    else:
        print('口令错误')


if __name__ == '__main__':
    main()



