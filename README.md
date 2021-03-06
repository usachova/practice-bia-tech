# **Цель:**

**Реализовать информационное приложение. Ресурс со статьями на различные тематики.**

## Особенности:

1. Должна быть реализована авторизация пользователя.
2. Предусмотреть, что может быть огромное количество статей.
3. Статьи разделены по темам (например, computer science, machine learning, data analytics, etc).
4. При добавлении статьи учесть, что у нее есть заголовок, текст, можно загрузить к статье изображение и добавить ее к существующей теме.
5. В списке статей отображается только их заголовок, список разделен по темам.
6. На списке статей реализовать серверную пагинацию.
7. У каждой статьи может быть много комментариев от разных пользователей.
8. Просмотр статьи предполагает отображение всей информации по статье, включая связанные с ней комментарии.
9. При удалении темы, должна удаляться связь статьи с этой темой. Статьи, относящиеся к удаленной теме должны остаться без темы.
10. При удалении статьи удаляются все комментарии связанные с ней.
11. Фильтр по темам статей на списке статей.
12. Поиск по заголовкам статей на списке.
13. Возможные роли: Админ, Читатель, Редактор

## Функциональность по ролям

### Админ

В рамках проекта может быть только один админ. Может все (почти все) :)

Доступно:

- Просматривать список всех статей.
- Просматривать каждую статью с комментариями.
- Создавать статьи.
- Редактировать статьи.
- Удалять статьи любого пользователя.
- Добавлять новую тему статей.
- Удалять темы статей.
- Редактироватьтемы статей.
- Добавлять комментарии к статьям.
- Редактировать свои комментарии к статьям.
- Удалять комментарии любого пользователя.

### Редактор

Пользователь с возможностями работы со статьями (добавление, редактирование и удаление)

Доступно:

- Просматривать список всех статей.
- Просматривать каждую статью с комментариями.
- Редактировать свою статью.
- Создавать статью.
- Удалять свою статью.
- Добавлять комментарии к статьям.
- Удалять и редактировать свои комментарии.

### Читатель

Пользователь, которому будет доступно только комментирование и просмотр статей.

Доступно:

- Просматривать список всех статей.
- Просматривать каждую статью с комментариями.
- Добавлять комментарии к статьям.
- Удалять и редактировать свои комментарии.

## Технологии необходимые для использования

- Фреймворки: django/flask
- БД: mysql/postgresql
- остальное по желанию, использование любых библиотек

## Важно

- фронт можно сделать самым примитивным.
- покрыть тестами основную функциональность.
- попробовать TDD подход на реализации хотя бы одной функциональности.

## Опционально, если станет скучно :)

- Добавить функциональность like/dislike для каждой статьи.
- Для поиска использовать elastic search
- Реализовать ассинхронную задачу на выгрузку статей за определенный период.
