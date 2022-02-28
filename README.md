# db-hack
В файле `scripts.py` собраны скрипты, меняющие данные электронного дневника школы.

## Использование
- Эксперименты проводились над сайтом электронного дневника [школы](https://github.com/devmanorg/e-diary).
- В README подробно указано, как развернуть сайт, и как он работает. 
- Установите у себя сайт дневника, следуя инструкциям в его репозитории.
- Необходимо подключить БД.  
- Для ввода скриптов используйте Django-shell. Удобнее работать с [Django-extensions](https://github.com/django-extensions/django-extensions).
- Запустите улучшенную версию Django-shell:
```python
$ python manage.py shell_plus
```
- Теперь нужно выполнить несколько импортов:
```python
>>> import random
```
Модуль `random` пригодится для выбора случайной похвалы.
```python
>>> from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
```
Модули пригодятся для отлавливания исключений.
```python
>>> from commendations import commendations
```
В `commendations.py` лежит 30 вариантов похвалы ученика. 
- Чтобы воспользоваться функцией из `scripts.py`, скопируйте ее в Django-shell. Запустите со своими аргументами. 
- Перейдите на сайт [дневника](http://127.0.0.1:8000/), найдите ученика, для которого внесли изменения. Проверьте их.

## Краткое описание функций
Далее описание функций из `scripts.py`

### get_child_object(child_name)
Принимает на вход фамилию и имя ученика. В случае неверного или неоднозначного ввода, обработает исключение, выведет сообщение об ошибке. Функция вызывается в других функциях. Возвращает запись указанного ученика из модели. 
Пример работы функции при вызове ее в `fix_marks`:

![image](https://user-images.githubusercontent.com/77130336/154846078-99f915a0-7e3d-4d2e-a975-b59ad39e5636.png)

### fix_marks(child_name)
Принимает на вход фамилию и имя ученика. Меняет все двойки и тройки ученика на пятерки. 
Пример:

![image](https://user-images.githubusercontent.com/77130336/155797496-07d5ecd5-5f46-45f7-953b-35c32fd0a1cf.png)

Было

![image](https://user-images.githubusercontent.com/77130336/155797002-2e62582f-224f-4a58-b435-9c1d021c90ff.png)

Стало

![image](https://user-images.githubusercontent.com/77130336/155797632-b6323ab9-b0d4-4186-bd7c-21e019b0fdd3.png)

### delete_chastisements(child_name)
Принимает на вход фамилию и имя ученика. Удаляет все замечания ученика.

Пример неудачи:

![image](https://user-images.githubusercontent.com/77130336/154846512-dee21f10-7dcd-4e9a-9d3a-a23ad3c9670c.png)

Пример удачный:

![image](https://user-images.githubusercontent.com/77130336/154846548-26ffd703-3eb3-4925-b51f-2656a9f9e999.png)

![image](https://user-images.githubusercontent.com/77130336/154846565-13078f9e-72bb-4f42-91a3-fc88e936f7ce.png)

![image](https://user-images.githubusercontent.com/77130336/154846577-c021414b-53c2-45f6-9fa4-593237a34ee5.png)


### create_commendation(child_name, subject_title)
Принимает на вход фамилию и имя ученика и предмет. Создает одну уникальную похвалу ученику по указанному предмету. 
Дата похвалы совпадает с датой проведения предмета. 

Пример:

![image](https://user-images.githubusercontent.com/77130336/154847067-d40c9c53-2d76-4945-aefc-9681326675f6.png)

![image](https://user-images.githubusercontent.com/77130336/154847090-0c7d932c-e074-4425-b667-c047471fcc84.png)
