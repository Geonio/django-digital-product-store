##Интернет магазин цифровых товаров на Django##
***
![alt text](Screenshot_1.png "Главная страница сайта")​
Главная страница сайта
***
![alt text](Screenshot_2.png "Форма проверки оплаты")​
Форма проверки оплаты
***
![alt text](Screenshot_3.png "Админ панель")​
Админ панель
***
<b>Оплата принимается через QIWI кошелек.</b>
***
<h4>Установка и настройки</h4>

Выполните команду 
<pre>pip3 install -r requirements.txt</pre>
<br>
В самом проекте отредактируйте файл
<pre>config.py</pre>
<br>
Установите секретный ключь и введите данные дя подключении к базе данных.
<pre>

SECRET_KEY = 'There is a secret key'
"""SETTING MySQL"""

db_host = 'mysql server ip address'
db_login = 'mysql server login'
db_password = 'mysql server password'
db_name = 'mysql server basedata name'
</pre>

Далее нужно создать таблицы в базе данных
<br>
Выполняем команды которые приведены ниже
<pre>
python3 manage.py makemigrations
python3 manage.py migrate
</pre>
Затем создаём профиль для администратора
<pre>
python3 manage.py createsuperuser
</pre>

После устновки при попытке зайти на сайт вас будет перебрасывать на страницу администратора.
Вам надо будет полностью настроить сайт что бы он заработал.
