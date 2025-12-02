# пункт а
height = float(input())
if height < 0 or height > 300:
     raise ValueError ("Некорректный рост")
else:
    print ("Рост введен корректно")

# пункт б
weight = float(input())
if weight < 0 or weight > 500:
     raise ValueError ("Некорректный вес")
else:
    print ("Вес введен корректно")

# пункт с
temp = float(input())
if temp < -273.15:
    raise ValueError ("Некорректная температура")
else:
    print ("Температура введена корректно")
