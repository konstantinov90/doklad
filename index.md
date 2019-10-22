---

layout: yandex2

style: |
    /* собственные стили можно писать здесь!!*/
    .red-alert {
        background: #f73434;
        border-radius: 9px;
        color: white;
        padding: 0 15px 5px;
    }


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

## Стандартные инструменты

1. Яндексовая библиотека интернационализации `@yandex‑int/i18n`
1. Проект в tanker.yandex-team.ru
1. `tanker‑kit` для синхронизации с танкером
1. Автоматика для ночной синхронизации

## Стандартный процесс

1. Разработчик добавляет новые фразы в dev-ветке
1. Задача (с новыми фразами) попадает в транк
1. Транк синхронизируется с мастер-веткой танкера
1. Фразы переводятся
1. Танкер синхронизируется с транком
1. PROFIT

## таймлайн
{:.fullscreen}

![](images/Frame 1.png)

## таймлайн
{:.fullscreen}

![](images/Frame 2.png) 

## таймлайн
{:.fullscreen}

![](images/Frame 2 many arrows.png)

## к чему это приводит
{:.fullscreen}

![](images/failed translation.png)

## таймлайн
{:.fullscreen}

![](images/Frame 3.png)

## Проблема

- Гарантия, что в интерфейсе есть непереведенные места, равна 99.9%
- Невозможно контролировать переводы конкретных частей функциональности (невозможно контролировать скорость и полноту)

## Что же делать
{:.section}

## В чем дело

1. Не можем контролировать полноту и скорость перевода
1. Работа над переводами начинается после попадания кода в транк

## таймлайн

{:.images}

![](images/Frame 4.png)

## Git control

Diff git'а показывает, что поменялось

## Github diff
{:.fullscreen}
![](images/github-diff.png)

## Arcanum diff
{:.fullscreen}
![](images/arcanum-diff.png)

## Проблема

- специфично для разных vcs
- не поможет отдавать фразы в работу до коммита

## Tanker API
{:.fullscreen}
![](images/tanker api.png)

## εὕρηκα!
{:.blockquote}

### Архимед

## Решение
- выгружать все фразы в ветку в танкере
- получать список фраз как diff между веткой и мастером
- отдавать фразы в работу переводчикам до коммита в транк

## Таймлайн
{:.images}

![](images/Frame 5.png) 

## Новый процесс

1. Разработчик добавляет новые фразы в dev-ветке
1. Когда активная разработка завершена - разработчик выгружает новые фразы в ветку в танкере
1. Получает дифф фраз сравнивая ветку с мастером
1. Создает задачу на перевод изменившихся фраз в ветке
1. Переводчики переводят, тестировщики тестируют
1. Разработчик мержит ветку с переводами и вливает пул-ревест
1. Можно релизить фичу - она уже переведена

## Автоматизируй это
{:.section}

## Новый процесс

1. Разработчик добавляет новые фразы в dev-ветке
1. Когда активная разработка завершена - разработчик выгружает новые фразы в ветку в танкере
1. Получает дифф фраз сравнивая ветку с мастером
1. Создает задачу на перевод изменившихся фраз в ветке
1. Переводчики переводят, тестировщики тестируют
1. Разработчик мержит ветку с переводами и вливает пул-ревест
1. Можно релизить фичу - она уже переведена

## Новый процесс

1. Разработчик добавляет новые фразы в dev-ветке
1. Когда активная разработка завершена - <span class="red-alert">разработчик выгружает новые фразы в ветку в танкере</span>
1. <span class="red-alert">Получает дифф фраз сравнивая ветку с мастером</span>
1. <span class="red-alert">Создает задачу на перевод изменившихся фраз в ветке</span>
1. Переводчики переводят, тестировщики тестируют
1. Разработчик <span class="red-alert">обновляет переводы в своей ветке</span>
1. Разработчик <span class="red-alert">мержит ветку с переводами</span> и вливает пул-ревест
1. Можно релизить фичу - она уже переведена

## Что нам нужно сделать

1. Научить tanker-kit выгружать в ветки
1. API для работы с ветками танкера
1. Автоматизировать тикеты в трекере

## Tanker-kit

потребовались доработки для работы с ветками

## [tanker-branch](https://github.yandex-team.ru/twilight/tanker-branch)
{:.shout}

## Si vis pacem, para bellum
{:.blockquote}

### Гай Юлий Цезарь

## Конфликты

```js
{
    "dna:declarations_filter/today-is/ru": {
        "form": {
            "a": "пЯтьница",
            "b": "Кровавый четверг",
            "resolved": null
        },
        "hash": "ea08bc....7bc77d3"
    }
}
```

## व्यायाम भी शरीर के लिए उतना ही आवश्यक है जितना ही हवा, पानी और भोजन।
{:.blockquote}

### Мохандас Карамчанд (Махатма) Ганди

## [tanker-gandhi](https://github.yandex-team.ru/twilight/tanker-gandhi)
{:.shout}

## tanker-gandhi
{:.fullscreen}
![](images/gandhi-1.png)

## tanker-gandhi
{:.fullscreen}
![](images/gandhi-2.png)

## tanker-gandhi
{:.fullscreen}
![](images/gandhi-3.png)

## tanker-gandhi
{:.fullscreen}
![](images/gandhi-4.png)

## [auto-issues](https://github.yandex-team.ru/twilight/auto-issues)
{:.shout}

## tanker-sync?
{:.shout}

## КОНЕЦ

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
