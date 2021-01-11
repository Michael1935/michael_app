#if 嵌套
def number():
    money = 3
    site =1
    if money>=2:
        print("get in")
        if site>0:
            print("can sit")
        else:
            print("no more site")
    else:
        print("no money to take bus")

def maka_username(user, name, **job):
    lisrds = {}
    lisrds['user'] = user
    lisrds['name'] = name
    for key, value in job.items():
        lisrds[key] = value
    return lisrds

insdf = maka_username('wang', age=24, sex='man')
print(insdf)

