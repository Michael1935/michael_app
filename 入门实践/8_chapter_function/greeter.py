# 属于python中字符串函数，返回’标题化‘的字符串，就是单词的开头为大写，其余为小写

def greeter_user(username):
    """显示简单的问候语"""
    print('hello world' + username.title() + '!')
    print('hello world' + username + '!')


greeter_user('wangyong')


def display_message(username):
    print(username + ' have learned funciton')

display_message('wangyong')