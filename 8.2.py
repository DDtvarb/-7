import random
def rectp(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    perimeter = 2 * (width + height)
    return perimeter

def rects(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    area = width * height
    return area

# Пример использования функций
x1 = random.randint(1,5)
y1 = random.randint(1,5)
x2 = random.randint(1,5)
y2 = random.randint(1,5)
print("x1 =",(x1) ,"y1 =",(y1), "x2 =" ,(x2), "y2 =",(y2))

p = rectp(x1, y1, x2, y2)
s = rects(x1, y1, x2, y2)

print("Периметр прямоугольника:", p)
print("Площадь прямоугольника:", s)
