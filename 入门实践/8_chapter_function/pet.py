def describe_pet(animal_type='dog', pet_name='da huang'):
    print('\n I have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title())

# 位置实参传值
describe_pet('haster', 'harry')

# 关键字实参传值
describe_pet(animal_type = 'haster0000', pet_name='harry000')

# 使用默认值
describe_pet()

