## Современные технологии в программировании

### Экстра - Лекция. Виртуальная машина Python
---
### Содержание

- Компиляция, интерпретация и Python
- Модель компиляции и выполнения Python
- Процесс компиляции Python
- Токенизация и разбор
- Программное дерево и абстрактное синтаксическое дерево
- Таблицы символов
- Граф потока управления
- ...продолжение следует
---
### Является ли Python интерпретируемым языком?

---
### Является ли Python интерпретируемым языком?
#### Хотя Python обычно не считают компилируемым языком, на самом деле он им является.


Во время компиляции некоторый исходный код Python преобразуется в байт-код,который может выполняться виртуальной машиной.

---
#### Является ли Python интерпретируемым языком?

#### Хотя Python обычно не считают компилируемым языком, на самом деле он им является.


Во время компиляции некоторый исходный код Python преобразуется в байт-код,который может выполняться виртуальной машиной.
<div style="margin-top: 50px;"> 
<section>{img_2}</section>
</div>
---


### Компиляция: Традиционный подход

<div style="margin-top: 50px;"> 
<section>{img_3}</section>
</div>

---
### Компиляция: Традиционный подход
#### Компилятор как "черный ящик"
<div style="margin-top: 50px;"> 
<section>{img_4}</section>
</div>

---

### Компиляция: Продвинутый подход
<div style="margin-top: 50px;"> 
<section>{img_5}</section>
</div>

#### Компилятор как набор ресурсов


---

## Подход Python

#### Итак, в заключение:

- Модель выполнения Python предполагает компиляцию в код ("байт-код") для специализированной виртуальной машины.

- Реализация Python позволяет **прямой** доступ (API) ко всем фазам компиляции и ромежуточным структурам данных.

---

### Модель компиляции/выполнения Python


- Разбор исходного кода Python в дерево синтаксического анализа (parse tree).

- Преобразование синтаксического дерева в абстрактное синтаксическое дерево (AST).

...продолжение 

---
- Генерация таблицы символов.
- Генерация объекта кода из AST.
    - Преобразование AST в граф потока управления.
    - Генерация объекта кода из графа потока управления.
- Объект кода Python выполняется под управлением виртуальной машины Python.

---

### Процесс компиляции Python
#### Очень традиционный способ
<div style="margin-top: 50px;"> 
<section>{img_6}</section>
</div>


---

### 1 - я фаза: Токенизация

##### Функция токенизации разбивает содержимое исходного модуля на легальные токены Python ("лексическая грамматика"). Сгенерированные токенизатором токены передаются парсеру...
<div style="margin-top: 30px;"> 
<section>{img_7}</section>
</div>
---

### 1 - я фаза: Токенизация
##### Лексическая грамматика Python: неформальный взгляд

**Идентификаторы:**
Имена, определенные программистом: имена функций и переменных, имена классов и т.д.
(Правила идентификаторов указаны в документации Python.)
**Операторы:**
Специальные символы: +, *оперирующие данными значениями и производящие результаты.
**Разделители:**
Группировка выражений, предоставление пунктуации и присваивания: (, ), {, }, =, *= и т.д.
---

*Литералы:**
Символы, предоставляющие постоянное значение некоторого типа.
Строковые и байтовые литералы: "Fred", b"Fred", числовые литералы: целочисленные
литералы: 2 , литералы с плавающей точкой: 1e100и мнимые литералы: 10j.
**Комментарии:**
Строковые литералы, начинающиеся с символа решетки и заканчивающиеся в конце физической
строки.
**NEWLINE:**
Специальный токен, обозначающий конец логической строки.
**INDENT, DEDENT:**
Токены, представляющие уровни отступа, которые группируют составные операторы.

---


#### 2 - я фаза: Построение программного дерева (деревьев)
<div style="margin-top: 50px;"> 
<section>{img_8}</section>
</div>

---
#### 2 - я фаза: Построение программного дерева (деревьев)
<div style="margin-top: 50px;"> 
<section>{img_9}</section>
</div>
---

#### 2 - я фаза: Построение программного дерева (деревьев)
<div style="margin-top: 50px;"> 
<section>{img_10}</section>
</div>
---

#### 2 - я фаза: Построение программного дерева (деревьев)
<div style="margin-top: 50px;"> 
<section>{img_11}</section>
</div>
---


### Грамматика Python
```python
stmt: simple_stmt | compound_stmt
simple_stmt: small_stmt
small_stmt: expr_stmt |
| global_stmt

(';' small_stmt)* [';'] NEWLINE
del_stmt | pass_stmt | flow_stmt | import_stmt
| nonlocal_stmt | assert_stmt
expr_stmt: testlist_star_expr ( augassign (yield_expr|testlist) |
( '=' (yield_expr|testlist_star_expr))* )
testlist_star_expr: (test|star_expr) (',' (test|star_expr))* [',']
augassign: '+='|'-='|'*='|'@='|'/='|'%=‘|'&='|'|='|'^='|'<<='|'>>='|'**='|'//='
del_stmt: 'del' exprlist
pass_stmt: 'pass'
flow_stmt: break_stmt | continue_stmt | return_stmt | raise_stmt | yield_stmt
break_stmt: 'break'
continue_stmt: 'continue'
return_stmt: 'return' [testlist]
yield_stmt: yield_expr
raise_stmt: 'raise' [test ['from' test]]
import_stmt:
import_name:
import_from:

import_name | import_from
'import' dotted_as_names
('from' (('.'|'...')* dotted_name | ('.'|'...')+)
'import' ('*' | '(' import_as_names ')'
import_as_name: NAME ['as' NAME]
dotted_as_name: dotted_name ['as' NAME]
| import_as_names))

(',' import_as_name)* [',']
(',' dotted_as_name)*

import_as_names: import_as_name
dotted_as_names: dotted_as_name
dotted_name: NAME ('.' NAME)*
global_stmt: 'global' NAME (',' NAME)*
nonlocal_stmt: 'nonlocal' NAME (',' NAME)*
assert_stmt: 'assert' test [',' test]
```

#### Грамматика расширенной формы
Бэкуса-Наура (EBNF) для Python:
модуль Grammar/Grammar

---
### Синтаксическое дерево Python

```python
import parser
from pprint 
import pprint
   source = " def quad(a): return a*a\n"
   st = parser.suite(source)
pprint(parser.st2list(st))
```

Модуль parser Python обеспечивает
ограниченный доступ
к дереву разбора блока кода Python

---


### Синтаксическое дерево Python

```python
[257,
 [269,
  [295,
   [263,
     [1, 'def'],
     [1, 'quad'],
     [264, [7, '('],
     [11, ':'],
     [304,
      [270,
       [271,
        [278,
         [281,
           [1, 'return'],
           [331,
            [305,
              [309,
                [310,
                  [311,
                   [312,
                     [315,
                       [316,
                         [317,
                           [318,
                             [319,
                               [320,
                               [321, [322,[323, [324, [1, 'a']]]]],
                               [16, '*'],
                               [321, [322,[323, [324, [1, 'a']]]]]]]]]]]]]]]]]]]],
        [4, '']]]]]],
[4, ''],
[0, '']]
```

---

Модуль parser Python обеспечивает ограниченный доступ к дереву разбора блока кода Python
```python
import parser
from pprint import pprint
source =
"def quad(a): return a*a\n"
st = parser.suite(source)
pprint(parser.st2list(st))
```
Вау! Доступ к дереву разбора Python
из программы на Python!
---
### Синтаксическое дерево Python

##### Реализация узла дерева разбора (C)

```python
typedef struct _node
{
short n_type; # node type
char * n_str; # node name
int n_lineno; # line number
int n_col_offset; # offset within the line
int n_nchildren; # number of children nodes
struct _node* n_child; # the list of children
} node;
```

---

#### Python AST
``` python
def fizzbuzz(n):
if n % 3 == 0 and n % 5 == 0 :
    return 'FizzBuzz'
elif n%3 == 0:
    return 'Fizz'
elif n%5 == 0:
    return 'Buzz'
else:
    return str(n)
```

<div style="margin-top: 50px;"> 
<section>{img_12}</section>
</div>


---


### Абстрактное синтаксическое дерево Python

##### Пример: тот же источник, что и раньше

```python
import ast
source = "def quad(a): return a*a\n"
node = ast.parse(source,mode="exec")
ast.dump(node, annote_fields=True,
include_attributes=True)
```
#### Результат dump:

```python
Module (
    body = [
        FunctionDef (
            name = 'quad',
            args = arguments(
                args = [
                    arg(arg='a',annotation=None,lineno=1, col_offset=9)
                ],
                vararg = None, kwonlyargs=[], kw_defaults=[], kwarg=None,defaults = []
            ),
     body = [
        Return(
            value = BinOp(
                left = Name(id='a',ctx=Load(),lineno=1,col_offset=20),
                op = Mult(),
                right = Name(id='a',ctx=Load(),lineno=1,col_offset=22),lineno = 1, col_offset = 20
            ),
            lineno = 1, col_offset = 13
        )
    ],
    decorator_list=[], returns=None, lineno=1, col_offset=0
    )
    ]
    )
```
---
### Абстрактное синтаксическое дерево Python
##### С предыдущего слайда: отформатированная версия
```python
Module (
    body = [
        FunctionDef (
            name = 'quad',
            args = arguments(
                args = [
                    arg(arg='a',annotation=None,lineno=1, col_offset=9)
                ],
                vararg = None, kwonlyargs=[], kw_defaults=[], kwarg=None,defaults = []
            ),
     body = [
        Return(
            value = BinOp(
                left = Name(id='a',ctx=Load(),lineno=1,col_offset=20),
                op = Mult(),
                right = Name(id='a',ctx=Load(),lineno=1,col_offset=22),lineno = 1, col_offset = 20
            ),
            lineno = 1, col_offset = 13
        )
    ],
    decorator_list=[], returns=None, lineno=1, col_offset=0
    )
    ]
    )
```


---
### Абстрактное синтаксическое дерево Python
С реализацией узла AST

```python
struct _stmt {
    enum _stmt_kind kind;
    union {
        struct {
            identifier name;
            arguments_ty args;
            asdl_seq* body;
            asdl_seq* decorator_list;
            expr_ty returns;
        } FunctionDef;
        ...
        struct {
            identifier name;
            asdl_seq* bases;
            asdl_seq* keywords;
            asdl_seq* body;
            asdl_seq* decorator_list;
        } ClassDef;
        ...
    } v;
    int lineno;
    int col_offset
}
```

---

### 3 - я фаза: Построение таблиц символов

Таблица символов :
Набор имен в блоке кода и контекст, в
котором используются имена

<div style="margin-top: 50px;"> 
<section>{img_13}</section>
</div>

---
Блок кода - это фрагмент программного кода, который выполняется как единоецелое.

Примеры блоков кода: модули, функции и классы.

Больше примеров: команды, введенные интерактивно в REPL.

У блока кода есть несколько пространств имен , связанных с ним.

Блок кода модуля: имеет доступ к глобальному пространству имен.

Блок кода функции: имеет доступ к локальному и глобальному пространству
имен.



---
### Глобальные и локальные переменные в Python



```python
>>> a = (1)// a является глобальной переменной
>>> def f(): a += (^2) //a переменная, локальная для f
>>> f()
UnboundLocalError:
local variable 'a' referenced before assignment

>>> a = 1
>>> def f():
>>> a = 77 //локальная a создается и инициализируется
>>> f()
>>> a(1) //глобальная a остается нетронутым(локальная a исчезла)

>>> a = 1
>>> def f():
>>> global a
>>> a += 2
>>> f()
>>> a
3
```
---
### Глобальные и локальные переменные в Python

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1 # count привязан к имени из
                   # внешней области видимости
        return count
    return counter
```
---
### Глобальные и локальные переменные в Python

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1 # count привязан к имени из
                   # внешней области видимости
        return count
    return counter
```

```python
>>> counter_1 = make_counter()
>>> counter_2 = make_counter()
>>> counter_1()
1
>>> counter_1()
2
>>> counter_2()
1
>>> counter_2()
2
```

##### Здесь и counter_1,и counter_2 являются замыканиями : они захватывают разные версии переменной count

---

### Структура таблиц символов

Каждая таблица символов содержит:

- **Информацию о собственных именах**
- **Информацию о "дочерних" таблицах**
    **символов**
- **Информацию о контексте**

<div style="margin-top: 50px;"> 
<section>{img_14}</section>
</div>

---

### Структура таблиц символов

##### Структура одной таблицы символов
``` python
struct symtable {
    PyObject* st_filename; # name of file being compiled
    struct _symtable_entry* st_top;
                    # symbols declared within the module 
    PyObject* st_blocks; # symbol tables for inner code blocks
        # many other fields
};
```

---
### Структура таблиц символов
##### Структура одной записи таблицы символов

``` python
typedef struct _symtable_entry{
    PyObject* ste_name; # string: name of current block
    PyObject* ste_varnames; # list of function parameters
    PyObject* ste_children; # list of child blocks
    PyObject* ste_directives; # locations of global and
                             # nonlocal statements
    _Py_block_ty ste_type; # module, class, or function
    int ste_nested; # true if block is nested

} PySTEntryObject;
```



---

### 4 - я фаза: Построение CFG и байт-кода


Следующий шаг для компилятора -
сгенерировать объекты кода из AST,
включающие информацию, содержащуюся в
таблице символов

<div style="margin-top: 50px;"> 
<section>{img_15}</section>
</div>

---
Шаг 1
AST преобразуется в базовые блоки инструкций
байт-кода Python. Результат -граф потока
управления (CFG).

Шаг 2
Сгенерированный граф потока управления
уплощается с использованием
обхода в глубину с постфиксной нумерацией.

---

### Граф потока управления

- Минимальная часть конструкций языка, которая должна выполняться последовательно, называется базовым блоком.

- Базовые блоки имеют одну точку входа, но могут иметь несколько выходов.

- Базовые блоки и пути между ними неявно представляют граф - граф потока управления.

- Таким образом, CFG по сути состоит из базовых блоков и связей между этими базовыми блоками.

---

### Граф потока управления

##### Пример
``` python
def fizzbuzz(n):
if n % 3 == 0 and n % 5 == 0 :
    return 'FizzBuzz'
elif n%3 == 0:
    return 'Fizz'
elif n%5 == 0:
    return 'Buzz'
else:
    return str(n)
```
<div style="margin-top: 50px;"> 
<section>{img_16}</section>
</div>

---
### Граф потока управления


<div style="margin-top: 50px;"> 
<section>{img_17}</section>
</div>

---

## Python Byte Code

``` python
def cube(a):
    return a*a*a
from dis import dis
dis(cube) 
```
---
### Python Byte Code


``` python
def cube(a):
    return a*a*a
from dis import dis
dis(cube) 
```

#### 0 LOAD_FAST           0(a)
#### 2 LOAD_FAST           0(a)
#### 4 BINARY_MULTIPLY
#### 6 LOAD_FAST           0(a)
#### 8 BINARY_MULTIPLY
#### 10 RETURN_VALUE

---

## Python Byte Code
```python
def run_cube7():
    return cube(7)
    from dis import dis
dis(cube)
```

#### 2 0 LOAD_GLOBAL   0(cube)
#### 2 LOAD_CONST      1 (7)
#### 4 CALL_FUNCTION   1
#### 6 RETURN_VALUE


