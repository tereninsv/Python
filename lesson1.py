print('Задание-1\n')
# Взять любую последовательность символов Юникода
# Написать функцию, которая принимает строку
# которая состоит только из английских букв и цифр
# и возвращает закодированное этой последовательностью
# что-то

def pool(start, end):
    start = int(start, 16)
    end = int(end, 16)
    pool = []

    while start <= end:
        pool.append(start)
        start += 1
    return pool


def translate(somethingstring, pool):
    newstring = ""
    for i in somethingstring:
        x = pool[i]
        x = chr(x)
        newstring += x
    return newstring


def detranslate(newstring):
    oldstring = ""
    for i in newstring:
        y = ord(i)
        z = pool.index(y)
        z = chr(z)
        oldstring += z
    return oldstring


somethingstring = input("введите английские буквы и цифры:")
somethingstring = somethingstring.encode("UTF-8")

pool = pool("2300", "23ff")

newstring = translate(somethingstring, pool)
print(f"закодировали в {newstring}")

# и написать обратную функцию, которая закодированную строку декодирует

oldstring = detranslate(newstring)
print(f"раскодироавали обратно и получили {oldstring}")

print('\nЗадание-2')
# Написать функции для создания тегов html
# Итогом должен быть набор функций, которые оборачивают текст в теги


# @a
# @div
# @p
# @set_text("Hello")
# def data():
#      return ""

# data() => <a><div><p>Hello</p></div></a>

def div(data):
    def wrapper():
        newdata = "<div>" + str(data()) + "</div>"
        return newdata

    return wrapper


def a(data):
    def wrapper():
        newdata = "<a>" + str(data()) + "</a>"
        return newdata

    return wrapper


def p(data):
    def wrapper():
        newdata = "<p>" + str(data()) + "</p>"
        return newdata

    return wrapper


def set_text(arg):
    def decor(data):
        def wrapper():
            is_string = arg
            return is_string

        return wrapper

    return decor


@a
@div
@p
@set_text("Hello")
def data():
    return ""


print(data())
