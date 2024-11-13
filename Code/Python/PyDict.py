@//////////////////////////////////////КЛЮЧЕВЫЕ СЛОВА В МУЛЬТИ-КАТЕГОРИИ
"Ключевые слова в мульти-категории, это такой синтаксис, которые можно использовать как тип данных, оператор, или"
"ключевое-слово - в зависимости от ситуации."
True          Истина, 1, да
False         Ложь , 0, нет
None          Нету, ничего, ложь
Ellipsis(...) Пропустить, игнорировать

@//////////////////////////////////////ВСТРОЕННАЯ ДИНАМИЧЕСКАЯ ТИПИЗАЦИЯ ДАННЫХ

10, -20 - Целые числа, int

3.14, 1.5e2 - Числа с плавающей точкой, float

65, 97, 49, 32, b"\x01": "A", "a", "1", " ", 1 - символы и числа в byte виде, bytes

@//////////////////////////////////////ВСТРОЕННЫЕ СТРУКТУРЫ ДАННЫХ

1+2j, 3.5-5.2j Комплексные числа, complex

[1, 2, 3, 4]

(1, 2, 3, 4)

{1, 2, 3, 4}

{"math": 90, "physics": 85, "chemistry": 75}

"BeholdeR"
b"BeholdeR"

@//////////////////////////////////////ПОПУЛЯРНЫЕ ПОЛЬЗОВАТЕЛЬСКИЕ СТРУКТУРЫ ДАННЫХ
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return not self.items



class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if self.items:
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return not self.items



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_at_end(self):
        if self.head:
            if not self.head.next:
                self.head = None
            else:
                current = self.head
                while current.next.next:
                    current = current.next
                current.next = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        def _insert(node, data):
            if not node:
                return Node(data)
            if data < node.data:
                node.left = _insert(node.left, data)



@//////////////////////////////////////ВСТРОЕННЫЕ ФУНКЦИИ И МЕТОДЫ
#ФУНКЦИИ ПРЕОБРАЗОВАНИЯ ТИПОВ ДАННЫХ
int(x)
    #Преобразует данные x в целые числа. Принимает:
       "Float   - дроби округляются."
        пример:
            int(9.4) -> 9
            int(9.5) -> 10

       "Complex - вернет вещественное число, но вызовет ошибку, если не использовать метод '.real'."
        пример:
            int(x)           -> ВЫДАСТ ИСКЛЮЧЕНИЕ. Комплексное число нельзя на прямую конвертировать в целое число. Нужно 
                                извлечь его с помощью .real и конвертировать получившийся float в int. Пример:
                                int(x).real
            int(3+4j).real   -> 3
            int("3+4j").real -> 3

       "String  - символы цифер переводит в число, иначе исключение."
        пример:
            int("abcABC") -> ВЫДАСТ ИСКЛЮЧЕНИЕ. Обычные и заглавные буквы не являются числами.
            int("%$^&#*") -> ВЫДАСТ ИСКЛЮЧЕНИЕ. Особые символы не являются числами.
            int("3.14")   -> ВЫДАСТ ИСКЛЮЧЕНИЕ. Символ точки не является частью целого числа, так что прежде чем превращать его
                             в int, нужно превратить его в float. Пример:
                             int(float("3.14"))
            int("65")     -> 65
            int("-65")    -> -65

       "Bool    - Правда превращается в 1, а Ложь в 0."
        пример:
            int(True)  -> 1
            int(False) -> 0

       "Bytes   - что бы преобразовать переведенные в байты данные в целое число, нужно что бы данные которые были переведены"
       "изначально были равны целому числу."
        пример:
            int(bytes(посимвольный_список_строки_данных).decode("кодировка"(Если пусто - равно "utf-8". Рекомендую оставлять пустой))) 
            -> закодированное целое число. Если изначально закодированно было не целое число, тогда ВЫДАСТ ИСКЛЮЧЕНИЕ

bytes() #
list() - это функция в Python, которая создает список из переданных ей элементов.
tuple() - это функция в Python, которая создает кортеж из переданных ей элементов.
set() - это функция в Python, которая создает множество из переданных ей элементов.
dict() - это функция в Python, которая создает словарь из переданных ей элементов.
Stack()   #Вот это случайно добавил, это вызов пользовательских структур, они не являются внутренним синтаксисом, а объявлено в коде локально, сверху. Я их на время оставлю белыми, чтобы выделить. За одно, кстати, поработаю над цветовой схемой кода, на будущее.
Queue()
LinkedList()
BinaryTree()
range() - это встроенная функция в Python, которая создает последовательность чисел с определенным шагом. Она часто используется в циклах для итерации по определенному диапазону значений.
len() - это встроенная функция в Python, которая возвращает количество элементов в объекте, таком как строка, список, кортеж или словарь.
abs() - это встроенная функция в Python, которая возвращает абсолютное значение числа, то есть его значение без учета знака.
all() - это встроенная функция в Python, которая возвращает True, если все элементы итерируемого объекта истинны, и False в противном случае.
any() - это встроенная функция в Python, которая возвращает True, если хотя бы один элемент итерируемого объекта истинен, и False в противном случае.
ascii() - это встроенная функция в Python, которая возвращает строковое представление объекта, используя только ASCII-символы.
bin() - это встроенная функция в Python, которая преобразует целое число в его двоичное представление в виде строки.
callable() - это встроенная функция в Python, которая проверяет, можно ли вызвать объект как функцию. Она возвращает True, если объект является вызываемым (функцией, методом, классом и т. д.), и False в противном случае.
chr() - это встроенная функция в Python, которая возвращает символ (строку из одного символа), соответствующий указанному Unicode коду.
dir() - это встроенная функция в Python, которая возвращает список всех атрибутов и методов объекта, переданного в качестве аргумента. Если аргумент не указан, возвращается список имен в текущей области видимости.
divmod() - это встроенная функция в Python, которая возвращает частное и остаток от деления двух чисел.
enumerate()
eval() - это встроенная функция в Python, которая выполняет строку как выражение Python и возвращает результат.
exec() - это встроенная функция в Python, которая выполняет строку или код Python, переданный ей в качестве аргумента.
filter() - это встроенная функция в Python, которая фильтрует элементы итерируемого объекта согласно заданному условию, определенному в функции
format() - это встроенная функция в Python, которая форматирует строку согласно указанному формату и возвращает отформатированную строку.
getattr()
hasattr()
hash()
help()
id()
input()
isinstance()
issubclass()
iter()
map()
max()
min()
next()
ord()
pow()
globals()
frozenset()
complex()
bytearray()
memoryview()
object()
print()
breakpoint()
locals()
reversed()
round()
setattr()
sorted()
compile()
open()
repr()
slice()
sum()
vars()
zip()
hex()
oct()
super()
delattr()
property()
classmethod()
staticmethod()

@//////////////////////////////////////ЛОГИЧЕСКИЕ И АРИФМЕТИЧЕСКИЕ ОПЕРАТОРЫ
+ 
-
*
/
//
%
**
=
+=
-=
*=
/=
//=
%=
**=
=>
->
<<
>>
&
|
~
^
==
!=
>
<
>=
<=
<<=
>>=
&=
|=
^=
not
and
or
is
is not
in
not in

@//////////////////////////////////////КЛЮЧЕВЫЕ СЛОВА
global
nonlocal
self.var_name
type
print
if
with  as
elif
else
for
while
break
continue
pass
try
except
finally
raise
assert
def
del
class
import
from
with
yield
async def
await
return
lambda x:x+2

@//////////////////////////////////////ПРОЧИЕ СПЕЦ-СИМВОЛЫ
@
#Комментарий, который игнорируется компилятором
:
,
.
;

@//////////////////////////////////////ИДЕНТИФИКАТОРЫ(НАЗВАНИЕ ПЕРЕМЕННЫХ, ФУНКЦИЙ И КЛАССОВ)
global = 1      НЕ ПРАВИЛЬНО
a@ = 0          НЕ ПРАВИЛЬНО
Global = 1                   Правильно
Еще примеры:                              Идентификаторам нельзя дать название служебного слова/функции или символа. Но зато символ нижнего регистра, и верхнего - это разные символы!
class = True    НЕ ПРАВИЛЬНО
myClass = True               Правильно

1variable = 'a' НЕ ПРАВИЛЬНО
variable1 = 'a'              Правильно    Идентификаторам нельзя дать название, которое начинается с числа или недопустимого символа.

_ = 998         НЕ ПРАВИЛЬНО
__ = 998                     Правильно    Идентификаторам нельзя дать название нижнего подчеркивания. Зато можно несколькими подчеркиваниями, и больше! И разное количество создаст разные переменные.

print_this_to_screen = 56    Правильно    Несколько слов можно разделить знаком подчеркивания. Такой метод называется snake_case(змеиный регистр).
