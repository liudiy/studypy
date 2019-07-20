def account_login():
    name =  input('name:')
    if name == '王三':
        print('攻击力5 防御力3 ')
    else:
        print('攻击力10 防御力9 ')

        account_login()
account_login()
