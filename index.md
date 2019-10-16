---

layout: yandex2

style: |
    /* собственные стили можно писать здесь!! */


---

# ![](themes/yandex2/images/logo-{{ site.presentation.lang }}.svg){:.logo}

## {{ site.presentation.title }}
{:.title}

### ![](themes/yandex2/images/title-logo-{{ site.presentation.lang }}.svg){{ site.presentation.service }}

{% if site.presentation.nda %}
![](themes/yandex2/images/title-nda.svg)
{:.nda}
{% endif %}

<div class="authors">
{% if site.author %}
<p>{{ site.author.name }}{% if site.author.position %}, {{ site.author.position }}{% endif %}</p>
{% endif %}

{% if site.author2 %}
<p>{{ site.author2.name }}{% if site.author2.position %}, {{ site.author2.position }}{% endif %}</p>
{% endif %}

</div>

## Постановка задачи
{:.section}

<!-- ### Верхний колонтитул -->

## Интерфейс на трех языках

## RU
{:.fullscreen}

![](images/morda-ru.png)

## EN
{:.fullscreen}

![](images/morda-en.png)

## TR
{:.fullscreen}

![](images/morda-tr.png)

## Инструменты

1. Яндексовая библиотека интернационализации `@yandex‑int/i18n`
1. Проект в tanker.yandex-team.ru
1. `tanker‑kit` для синхронизации с танкером
1. Автоматика для ночной синхронизации

## Инструменты

1. Яндексовая библиотека i18n `@yandex‑int/i18n`
1. Проект в tanker.yandex-team.ru
1. `tanker‑kit` для синхронизации с танкером
1. Автоматика для ночной синхронизации
<!-- 
## Стандартный процесс

1. Разработчик добавляет новые фразы в dev-ветке
1. Задача (с новыми фразами) попадает в транк
1. Транк синхронизируется с мастер-веткой танкера
1. Фразы переводятся
1. Танкер синхронизируется с транком
1. PROFIT -->

## таймлайн
{:.images}

![](images/Frame 1.png)

## таймлайн
{:.images}

![](images/Frame 1 no text.png)

## таймлайн
{:.images}

![](images/Frame 2.png) 

## таймлайн
{:.images}

![](images/Frame 2 many arrows.png)

## таймлайн
{:.images}

![](images/Frame 3.png)

## к чему это приводит
{:.fullscreen}

![](images/failed translation.png)

## Проблема

- В продакшене есть непереведенные фразы
- Невозможно контролировать переводы конкретных частей функциональности (невозможно контролировать скорость и полноту)
- Гарантия, что в интерфейсе есть непереведенные места, равна 99.9%

## Что же делать
{:.section}

## Take control

Чтобы контролировать полноту и время работы над переводами нам нужен список фраз, поменявшихся в задаче

## Git control

Diff git'а показывает, что поменялось

## Проблема

- неуниверсально
- нужно парсить код, чтобы получить список конкретных фраз

## Решение

- tanker-kit настроен, можно использовать его парсер
- но ведь он выгружает ключи в танкер 🤔

## Эврика

**можно выгружать распаршенные фразы в ветку в танкере!**



## Длинная цитата переносится на несколько строк
{:.blockquote}

### Источник

## Заголовок

Основной текст

**Ключевая мысль**

- Маркированный список
- Маркированный список

1. Нумерованный список
2. Нумерованный список

### Источник

## Заголовок

Элементы появляются по очереди

1. {:.next}Нумерованный список
2. {:.next}Нумерованный список
3. {:.next}Нумерованный список
4. {:.next}Нумерованный список


### Источник

## Заголовок
{:.images}

![](themes/yandex2/images/images-one.svg)

### Источник

## Заголовок
{:.images .two}

![](themes/yandex2/images/images-two.svg)
*Текст*

![](themes/yandex2/images/images-two.svg)
*Текст*

### Источник

## Заголовок
{:.images .three}

![](themes/yandex2/images/images-three.svg)
*Текст*

![](themes/yandex2/images/images-three.svg)
*Текст*

![](themes/yandex2/images/images-three.svg)
*Текст*

### Источник

## Заголовок

![](themes/yandex2/images/image-right.svg)
{:.image-right}

Основной текст

**Ключевая мысль**

- Маркированный список
- Маркированный список

1. Нумерованный список
2. Нумерованный список

### Источник

## Заголовок

<!-- библиотека пиктограмм https://patterns.yandex-team.ru/presentations?typeIn=icons -->

![](themes/yandex2/images/icons.svg)
{:.icon-left}

Основной текст

**Ключевая мысль**

- Маркированный список
- Маркированный список

1. Нумерованный список
2. Нумерованный список

### Источник

## Заголовок
{:.icons}

<!-- библиотека пиктограмм https://patterns.yandex-team.ru/presentations?typeIn=icons -->

![](themes/yandex2/images/icons.svg)
*Текст*

![](themes/yandex2/images/icons.svg)
*Текст*

![](themes/yandex2/images/icons.svg)
*Текст*

### Источник

## Заголовок
{:.icons .four}

<!-- библиотека пиктограмм https://patterns.yandex-team.ru/presentations?typeIn=icons -->

![](themes/yandex2/images/icons.svg)
*Текст*

![](themes/yandex2/images/icons.svg)
*Текст*

![](themes/yandex2/images/icons.svg)
*Текст*

![](themes/yandex2/images/icons.svg)
*Текст*

### Источник

## Заголовок
{:.icons .five}

<!-- библиотека пиктограмм https://patterns.yandex-team.ru/presentations?typeIn=icons -->

![](themes/yandex2/images/icons.svg)
*Текст*

![](themes/yandex2/images/icons.svg)
*Текст*

![](themes/yandex2/images/icons.svg)
*Текст*

![](themes/yandex2/images/icons.svg)
*Текст*

![](themes/yandex2/images/icons.svg)
*Текст*

### Источник

## Заголовок будет скрыт
{:.fullscreen}

![](themes/yandex2/images/images-fullscreen.svg)

## Заголовок будет скрыт
{:.fullscreen}

![](themes/yandex2/images/images-fullscreen.svg)

<figure markdown="1">
Текст
</figure>

## Таблица

|  Locavore     |  Umami       |  Helvetica |  Vegan     |
+---------------|--------------|------------|------------+
|  Fingerstache<br/>The second line |  Kale        |  Chips     |  Keytar    |
|  Sriracha     |  Gluten-free |  Ennui     |  Keffiyeh  |
|  Thundercats  |  Jean        |  Shorts    |  Biodiesel |
|* Terry        |* Richardson  |* Swag      |* Blog      |

Текст

### Источник

## Исходный код (html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Shower</title> <!--Comment-->
    <link rel="stylesheet" href="screen.css">
</head>
<body>Hello!</body>
</html>
```

## Исходный код (js)

Пояснение для кода.

```js
var i, j, over, data = new Array(2, 34.12, 4.7, 0, 234, 5);
var test = false;

for (i = 1; i < data.length; i++) {
    over = data[i]; 
    for (j = i - 1; j >= 0 && data[j] > over; j--) {
        data[j + 1] = data[j];
    }
    data[j + 1] = over;
}
alert(data.join(','));
```

## Исходный код (css)

```css
.head {
    background-color: yellow;
}

.head__logo {
    background-image: url(images/logo.svg);
}

#test, body {
    font-weight: bold;
}

```

## Этот заголовок будет скрыт
{:.fullscreen}

```js
// исходный код (на весь экран)

var x = 10;
for (var i = 0; i < x; i++) {
    console.log('hello!');
}
```

## Контакты 
{:.contacts}

{% if site.author %}

<figure markdown="1">

### {{ site.author.name }}

{% if site.author.position %}
{{ site.author.position }}
{% endif %}

</figure>

{% endif %}

{% if site.author2 %}

<figure markdown="1">

### {{ site.author2.name }}

{% if site.author2.position %}
{{ site.author2.position }}
{% endif %}

</figure>

{% endif %}

<!-- разделитель контактов -->
-------

<!-- left -->
- {:.skype}author
- {:.mail}author@yandex-team.ru
- {:.github}author

<!-- right -->
- {:.twitter}@author
- {:.facebook}author

<!-- 

- {:.mail}author@yandex-team.ru
- {:.phone}+7-999-888-7766
- {:.github}author
- {:.bitbucket}author
- {:.twitter}@author
- {:.telegram}author
- {:.skype}author
- {:.instagram}author
- {:.facebook}author
- {:.vk}@author
- {:.ok}@author

-->
