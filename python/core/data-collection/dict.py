"""
Dict: mutable, ordered, duplicate keys are not allowed, unindex, slicing not posible, can store any type of data

syntax: 

dict_name = dict()
dict_name = {
    'key1' : value1,
    'key2' : value2,
    'key3' : value3
}

"""

# dict = dict()

# print(type(dict))

contacts = {
    'A': {
            'ajay':{
                'phone': '9876543210',
                'email': 'ajay@gmail.com'
            },
            'aman':{
                'phone': '9999999999',
                'email': 'aman@gmail.com'
            },
            'anil':{
                'phone': '8888888888',
                'email': 'anil@gmail.com'
            }
        },
    'B': {
            'brijesh':{
                'phone': '7777777777',
                'email': 'brijesh@gmail.com'
            },
            'brahim':{
                'phone': '6666666666',
                'email': 'brahim@gmail.com'
            },
            'bhavan':{
                'phone': '5555555555',
                'email': 'bhavan@gmail.com'
            }
    },
    'C': {
            'chandan':{
                'phone': '4444444444',
                'email': 'chandan@gmail.com'
            },
            'chandravan':{
                'phone': '3333333333',
                'email': 'chandravan@gmail.com'
            },
            'chaitanya':{
                'phone': '2222222222',
                'email': 'chaitanya@gmail.com'
            }
    }
}

# print(contacts)
# print(contacts['C'])
# print(type(contacts['C']))
# print(contacts['C']['chaitanya'])
# print(contacts['C']['chaitanya']['phone'])

# print(contacts['A']['ajay']['email'])

# contacts['A']['ajay']['email'] = 'ajay1234@gmail.com'

# print(contacts['A']['ajay']['email'])


# print(dir(contacts))

fruits = {
    'apple': 10,
    'banana': 20,
    'cherry': 30,
    'date': 40,
    'elderberry': 50
}

new_vegs = {
    'potato': 30,
    'carrot': 20,
    'onion': 10,
    'spinach': 30,
    'tomato': 40,
    'apple': 100
}

# fruits.update(new_vegs)
# print(fruits)
# fruits.pop('date')
# fruits.popitem()
# print(fruits)

# print(fruits.get('apple'))

# print(fruits.keys())
# print(len(fruits.keys()))

# for key in fruits.keys():
#     print(key)

# print(fruits.values())

# for value in fruits.values():
    # print(value)

# print(fruits.items())

# for key, value in fruits.items():
#     print(f"{key} : {value}")




fruits = ['apple', 'guava', 'mango']
price = 100



# fruits_price = dict()

# print(fruits_price.fromkeys(fruits, price))

car = {
    'brand': 'Toyota',
    'model': 'Camry',
    'year': 2020,
    'color': 'Blue'
}

# car.setdefault('color', 'black')

# print(car)