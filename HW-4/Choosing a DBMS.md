### Выбор системы управления распределенной базой данных

#### Бизнес-сценарий.
Представим, что у нас есть интернет-магазин электроники. У магазина есть несколько складов, разнесенных по разным городам. За каждым складом физически закреплена своя 
база данных.
Базы данных содержат информацию как об имеющихся товарах, так и об проданных. Таким образом, мы имеем распределенную сеть баз данных. 

Пользователь на сайте, а также внутренние аналитики компании должны иметь возможность получать информацию об имеющихся и проданных товарах с любого склада в единых интерфейсах. Таким образом, у нас возникает потребность в использования Систем Управления Распределенными Базами Данных. 

В данном сценарии мы не будем касаться документооборота, хранения накладных, чеков и прочего. Нас интересут только позиции товаров, поэтому выбор будем осуществлять из SQL СУБД.

##### На что будем ориентироваться при выборе

* Использование SQL синтаксиса	
* Требования к надежности, потому что магазин должен работать без перебоев
* Масштабируемость по нагрузке на чтение
* Качество и полнота документации
* Скорость техподдержки
* Простота в использовании
* Популярность (популярное решение упростит эксплуатацию и найм сотрудников)


##### Выберем конкурсантов
Будем сравнивать три СУБД:
* CockroachDB
* Yugabyte DB
* YDB

### Замечания по критериям
Среди критериев есть те, по которым провести корректное сравнение не представляется возможным. Например, масштабируемость. Разработчики каждой из СУБД обещают масштабируемость для разных типов нагрузок, в том числе для массовых запросов на чтение. Конечно, в идеальном случае необходимо провести тестирование каждой СУБД в тех сценариях, в которых они будут функционировать в рамках нашего интернет магазина. Поэтому будем считать, что по данному критерию все конкурсанты нам подходят. Аналогично с надежностью и отказоустойчивостью.   

### Перейдем к оценке конкурсантов

### CockroachDB
* Поддерживает классический синтаксис PostgreSQL
* Данная СУБД разрабатывалась с упором на надежность и по праву считается одной из самых надежных
* Использует многократно проверенный движок хранения данных RocksDB
* Имеет самую простую настройку
* Популярное решение
 

### YDB
* Используется собственный диалект SQL - YQL
* Отечественный разработчик
* Молодой продукт. На данный момент не самое популярное и протестированное решение
* Позволяет построить более гибкую экосистему управления данными
* Жирный плюс - наличие русскоязычной документации как для YDB, так и для YQL

### Yugabyte
* Прямой конкурент CockroachDB
* Поддерживает классический синтаксис PostgreSQL
* Отказоустойчива, но по некоторым тестам все же уступает CockroachDB
* Популярное решение


### Вывод

В результате сравнения для данного бизнес-сценария, считаю что нужно остановить свой выбор на **CockroachDB**, которое удовлетворяет всем изначально озвученным требованиям по надежности, масштабируемости и простоте использования. 