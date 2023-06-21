# Интерактивный тренажер по SQL
## Полезные ссылки
- [SQL ACADEMY](https://sql-academy.org/ru)
- [Бесплатный тренажер на английском](https://sqlbolt.com/)
- Шпаргалки по SQL [раз](https://www.sqltutorial.org/wp-content/uploads/2016/04/SQL-cheat-sheet.pdf), [два](https://learnsql.com/blog/sql-basics-cheat-sheet/sql-basics-cheat-sheet-ledger.pdf)
- [Оконные функции в SQL](https://leftjoin.ru/files/window_functions_cheatsheet.pdf)
- [Конспект по курсу](https://github.com/IsFilimonov/LearningPath/tree/main/2021/Stepik_Interactive-SQL-Simulator)
- [Еще Конспект по курсу](https://github.com/EMIR1HUB/All_Conspectus/blob/main/SQL/1.2_base_SelectData.md)
- [Курс по SQL на ютубе](https://www.youtube.com/playlist?list=PLtPJ9lKvJ4oh5SdmGVusIVDPcELrJ2bsT)
- Статья на Хабре [Как изучить SQL за 2 месяца с нуля. План обучения](https://habr.com/ru/articles/709116/) со множеством полезных ссылок.
- [Курс · Hadoop. Основы](https://www.youtube.com/playlist?list=PLrCZzMib1e9rPxMIgPri9YnOpvyDAL9HD)
- [Курс · Базы данных](https://www.youtube.com/playlist?list=PLrCZzMib1e9r6c-j8aW1JuETSyCBp9iAg)
- [Курс · Базы данных (весна 2017)](https://www.youtube.com/playlist?list=PLrCZzMib1e9oOFQbuOgjKYbRUoA8zGKnj)

## Рекомендуемый алгоритм успешного прохождения каждого шага курса

1. Прочитайте текстовый материал, он достаточно короткий и всегда имеет всю необходимую информацию для выполнения практического задания.
2. Eсли по тексту теории встречаются примеры - скопируйте и вставьте их в окно кода, запустите запрос, не отправляя на проверку (нажать черную кнопку Запустить код). Проанализируйте результат, если он (результат) является неожиданным или не понятным - еще раз вернитесь к теории и еще раз ее прочитайте.
3. Теперь можно приступать к выполнению практического задания. Прежде всего внимательно прочитайте формулировку, разберитесь, что именно нужно сделать (без этого совершенно нет смысла писать код SQL);
4. Если задание понятно - можно приступать к реализации запроса, тут два варианта - либо Вы полностью напишете запрос на SQL, либо поищите среди примеров похожий, скопируйте его и начинайте его корректировать (скорее всего, когда пройдете десяток шагов, вариант с копированием отпадет, как ненужный).
5. Отправьте запрос на проверку.  Результата может быть два - либо запрос написан верно, и он проходит - можно переходить к следующему шагу. Либо запрос система не пропускает, в нем допущена ошибка, но "кто не ошибается, тот ничего и не делает...", ошибки это обязательный и полезный элемент в процессе обучения;
6. Начинайте отлаживать (исправлять) запрос, причем если Вам удастся это сделать самостоятельно - значит Вы  действительно разобрались с материалом шага, можно переходить к следующему. Если же ошибки исправить не удается,  не спешите паниковать, читать и писать комментарии, лезть в Интернет - просто вернитесь к 1 или 2-му пункту этого алгоритма.
7. Если же все-таки теория и примеры не помогают, воспользуйтесь памяткой о типичных ошибках и способах их исправления (приведена ниже),  примерно половина ошибок связана с описанными в ней пунктами и, привыкнув каждый раз проверять свой запрос, Вы сбережете себе много часов и нервов (проверено на опыте).
8. Когда Вы напишете правильный запрос, его можно опубликовать в решениях, посмотреть решения других студентов и обсудить свое.
9. В комментариях можно давать подсказки или делиться тем, что вызвало у Вас наибольшие трудности, только без спойлеров!
10. Очень полезно прочитать вопрос другого обучающегося и, если Вы точно знаете ответ, самостоятельно ответить на его вопрос - это еще один способ закрепления материала, причем очень действенный (тоже проверено на опыте).
11. После выполнения заданий каждого модуля, Вы будете получать ссылку на текстовый конспект этого модуля, по которому удобно ориентироваться по пройденному материалу.

## Памятка о типичных ошибках и способах их исправления

1. Приведите синтаксис запроса к общепринятому:
- если у вас есть время, стоит изучить [руководство по стилю SQL](https://www.sqlstyle.guide/ru/)
- можете [отформатировать](https://codebeautify.org/sqlformatter) ваш запрос с помощью, например
- в любом случае, информации и примеров в курсе достаточно для того, чтобы писать запросы корректно.
2. Проверьте, что ключевые слова, названия столбцов и значения в ячейках, которые необходимо найти, написаны правильно. Особенно обратите внимание, чтобы в русских названиях столбцов не было английских букв.

3. Проверьте, что:
- количество открывающихся скобок равно количеству закрывающихся;
- запятые разделяют перечисление столбцов, но не ключевые слова;
- запросы разделяются точкой с запятой.
4. Проверьте, что последовательность команд указана верно (она отличается от последовательности выполнения команд в запросе):
<img width="1272" alt="image" src="https://github.com/luta-wolf/Python_solved_tasks/assets/58044383/41979faa-d601-464d-9e60-acc9a8e40aae">

5.  Если запрос включает подзапросы, выполните сначала подзапросы и удостоверьтесь, что получаете ожидаемый результат.
6. Прочитайте комментарии под заданием: большинство трудностей уже обсуждалось не один раз.


## Основные понятия реляционных баз данных
- `отношение`  – это структура данных целиком, набор записей (в обычном понимании – таблица) , в  примере –это Сотрудник;
- `кортеж` – это каждая строка , содержащая данные (более распространенный термин – запись ), например, <001, Борин С.А, 234-01-23, программист>, все кортежи в отношении - должны быть различны;
- `мощность` – число кортежей в таблице (проще говоря, число записей), в данном случае 3, мощность отношения может быть любой (от 0 до бесконечности), порядок следования - кортежей - неважен;
- `атрибут` – (заголовок столбца) это столбец в таблице (более распространенный термин – поле ), в примере – Табельный номер, Фамилия И.О., Телефон, Должность)
- `размерность` – это число атрибутов в таблице, в данном случае – 4; размерность отношения должна быть больше 0, порядок следования атрибутов существенен;
- `домен атрибута` – (значение отдельной ячейки (поля)) это допустимые значения (неповторяющиеся), которые можно занести в поле , например для атрибута Должность домен – {инженер, программист}.
<img width="837" alt="image" src="https://github.com/luta-wolf/Python_solved_tasks/assets/58044383/3d2045b5-603a-4624-abc1-8b6157092210">

### Основные типы данных SQL:
<img width="988" alt="image" src="https://github.com/luta-wolf/Python_solved_tasks/assets/58044383/8a30e527-46d0-484d-b3ef-424857905475">

### Создание таблицы
- ключевые слова : CREATE TABLE
- имя создаваемой таблицы;
- открывающая круглая скобка «(»;
- название поля и его описание, которое включает тип поля и другие необязательные характеристики;
- запятая;
- название поля и его описание;
- ...
- закрывающая скобка «)».
Пример. Создадим таблицу genre следующей структуры:
    CREATE TABLE genre(
        genre_id INT PRIMARY KEY AUTO_INCREMENT,
        name_genre VARCHAR(30)
    );

### Вставка записи в таблицу
Для занесения новой записи в таблицу используется SQL запрос, в котором указывается в какую таблицу, в какие поля заносить новые значения. Структура запроса:

- ключевые слова INSERT INTO (ключевое слово INTO можно пропустить);
- имя таблицы, в которую добавляется запись;
- открывающая круглая скобка «(»;
- список полей через запятую, в которые следует занести новые данные;
- закрывающая скобка «)»;
- ключевое слово VALUES;
- открывающая круглая скобка «(»;
- список значений через запятую, которые заносятся в соответствующие поля, при этом текстовые значения заключаются в кавычки, числовые значения записываются без кавычек, в качестве разделителя целой и дробной части используется точка;
- закрывающая скобка «)».
    INSERT INTO таблица(поле1, поле2)
    VALUES (значение1, значение2);
При составлении списка полей и списка значений необходимо учитывать следующее:

1. количество полей и количество значений в списках должны совпадать;
2. должно существовать прямое соответствие между позицией одного и того же элемента в обоих списках, поэтому первый элемент списка значений должен относиться к первому столбцу в списке столбцов, второй – ко второму столбцу и т.д.;
3. типы данных элементов в списке значений должны быть совместимы с типами данных соответствующих столбцов таблицы ( целое число можно занести в поле типа DECIMAL, обратная операция - недопустима);
4. новые значения нельзя добавлять в поля, описанные как PRIMARY KEY AUTO_INCREMENT;
5. рекомендуется заполнять все поля записи, если же поле пропущено, значение этого поля зависит от установленных по умолчанию значений, если значения не установлены - на данной платформе вставляется пустое значение (NULL).

## Выборка всех данных из таблицы
Для того чтобы отобрать все данные из таблицы используется SQL запрос следующей структуры:
- ключевое слово SELECT;
- символ « *» ;
- ключевое слово FROM;
- имя таблицы.
    SELECT *
    FROM book;

## Выборка отдельных столбцов
Для того чтобы отобрать данные из определенных столбцов таблицы используется SQL запрос следующей структуры:
- ключевое слово SELECT ;
- список столбцов таблицы через запятую;
- ключевое слово FROM ;
- имя таблицы.
    SELECT title, amount FROM book;

## Присвоение новых имен столбцам при формировании выборки
- ключевое слово SELECT ;
- имя столбца;
- ключевое слово AS ;
- новое название столбца (можно русскими буквами), выводимое в результате запроса, но это должно быть одно слово, если название состоит из двух слов – соединяйте их подчеркиванием, например, Количество_книг;
- запятая;
- имя столбца;
- .... 
- ключевое слово FROM ;
- имя таблицы.
    SELECT title AS Название, amount
    FROM book;

## Выборка данных с созданием вычисляемого столбца
    SELECT title, author, price, amount,
         price * amount AS total
    FROM book;
<img width="1037" alt="image" src="https://github.com/luta-wolf/luta-wolf/assets/58044383/f3da7620-0460-4dea-936d-4d7cff1cc05b">

## Выборка данных, вычисляемые столбцы, логические функции
Запрос:

    SELECT title, amount, price,
        ROUND(IF(amount < 4, price * 0.5, IF(amount < 11, price * 0.7, price * 0.9)), 2) AS sale,
        IF(amount < 4, 'скидка 50%', IF(amount < 11, 'скидка 30%', 'скидка 10%')) AS Ваша_скидка
    FROM book;
Результат:

    +-----------------------+--------+--------+--------+-------------+
    | title                 | amount | price  | sale   | Ваша_скидка |
    +-----------------------+--------+--------+--------+-------------+
    | Мастер и Маргарита    | 3      | 670.99 | 335.50 | скидка 50%  |
    | Белая гвардия         | 5      | 540.50 | 378.35 | скидка 30%  |
    | Идиот                 | 10     | 460.00 | 322.00 | скидка 30%  |
    | Братья Карамазовы     | 2      | 799.01 | 399.51 | скидка 50%  |
    | Стихотворения и поэмы | 15     | 650.00 | 585.00 | скидка 10%  |
    +-----------------------+--------+--------+--------+-------------+