---
title: zapret-discord-youtube
date: 2025-06-22T15:29:14+08:00
draft: False
image: https://images.unsplash.com/photo-1646315026047-c424f211e5bd?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NTA1NzcyNTl8&ixlib=rb-4.1.0
tags: ['github',Discord, YouTube, Windows, bypass, blocking, strategies, WinDivert, service]
categories: ['github']
---

# [Flowseal/zapret-discord-youtube](https://github.com/Flowseal/zapret-discord-youtube)

<div align="center">

# <img src="https://cdn-icons-png.flaticon.com/128/5968/5968756.png" height=28 /> <a href="https://github.com/Flowseal/">Flowseal</a><a href="https://github.com/Flowseal/zapret-discord-youtube">/zapret-discord-youtube</a> <img src="https://cdn-icons-png.flaticon.com/128/1384/1384060.png" height=28 />

*"Plug & Play"* обход блокировок иностранных платформ, <img src="https://cdn-icons-png.flaticon.com/128/5968/5968756.png" height=11 /> **Discord** и <img src="https://cdn-icons-png.flaticon.com/128/1384/1384060.png" height=11 /> **YouTube** для Windows

Альтернатива https://github.com/bol-van/zapret-win-bundle  
Также, вы можете материально поддержать разработчика zapret [тут](https://github.com/bol-van/zapret?tab=readme-ov-file#%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B0)
</div>

> [!CAUTION]
>
> ### АНТИВИРУСЫ
> WinDivert может вызвать реакцию антивируса.
> WinDivert - это инструмент для перехвата и фильтрации трафика, необходимый для работы zapret.
> Замена iptables и NFQUEUE в Linux, которых нет под Windows.
> Он может использоваться как хорошими, так и плохими программами, но сам по себе не является вирусом.
> Драйвер WinDivert64.sys подписан для возможности загрузки в 64-битное ядро Windows.
> Но антивирусы склонны относить подобное к классам повышенного риска или хакерским инструментам.
> В случае проблем используйте исключения или выключайте антивирус совсем.
>
> **Выдержка из [`readme.md`](https://github.com/bol-van/zapret-win-bundle/blob/master/readme.md#%D0%B0%D0%BD%D1%82%D0%B8%D0%B2%D0%B8%D1%80%D1%83%D1%81%D1%8B) репозитория [bol-van/zapret-win-bundle](https://github.com/bol-van/zapret-win-bundle)*

> [!IMPORTANT]
> Все бинарные файлы в папке [`bin`](./bin) взяты из [zapret-win-bundle/zapret-winws](https://github.com/bol-van/zapret-win-bundle/tree/master/zapret-winws). Вы можете это проверить с помощью хэшей/контрольных сумм. Проверяйте, что запускаете, используя сборки из интернета!

## ⚙️Использование

1. Загрузите архив (zip/rar) со [страницы последнего релиза](https://github.com/Flowseal/zapret-discord-youtube/releases/latest)

2. Распакуйте содержимое архива по пути, который не содержит кириллицу/спец. символы

3. Запустите нужный файл

## ℹ️Краткие описания файлов

- [**`general.bat ...`**](./general.bat) - запуск со стратегией для обхода блокировок  
  **Работоспособность той или иной стратегии зависит от многих факторов. Пробуйте разные стратегии (ALT, МГТС и другие), пока не найдёте рабочее для вас решение**

- [**`service.bat`**](./service.bat) - вспомогательные скрипты:
  - <ins>**`Install Service`** - установка любой стратегии в автозапуск (services.msc)</ins>
  - **`Remove Services`** - удаление стратегии и WinDivert из служб
  - **`Check Status`** - проверка статуса обхода и служб (стратегии на автозапуске и WinDivert)
  - **`Run Diagnostics`** - диагностика на распространённые причины, по которым zapret может не работать.  
  В конце можно очистить кэш <img src="https://cdn-icons-png.flaticon.com/128/5968/5968756.png" height=11 /> `Discord`, что может помочь, если он неожиданно перестал работать
  - **`Check Updates`** - проверка на обновления
  - **`Switch Game Filter`** - переключение режима обхода для игр (и других сервисов, использующих UDP и TCP на портах выше 1023).  
  **После переключения требуется перезапуск стратегии.**  
  В скобках указан текущий статус (включено/выключено).
  - **`Switch ipset`** - переключение режима обхода сервисов из `ipset-all.txt`.  
  Полезно при тестировании, если не работает то, что не заблокировано.  
  В скобках указан текущий статус (загружен список/пустой список).
  - **`Update ipset list`** - обновление списка `ipset-all.txt` актуальным из репозитория


## ☑️Распространенные проблемы

### Не работает <img src="https://cdn-icons-png.flaticon.com/128/5968/5968756.png" height=18 /> Discord

- См. [#252](https://github.com/Flowseal/zapret-discord-youtube/discussions/252)

### Не работает <img src="https://cdn-icons-png.flaticon.com/128/1384/1384060.png" height=18 /> YouTube

- См. [#251](https://github.com/Flowseal/zapret-discord-youtube/discussions/251)

### После запуска стратегии ничего не происходит

- После запуска стратегии (отдельным bat файлом, не через service), должен открыться winws.exe (обход), который можно увидеть в панели задач.  
Если этого не произошло, то см. [#522](https://github.com/Flowseal/zapret-discord-youtube/issues/522)

### Обход не работает

> [!IMPORTANT]
> **Стратегии блокировок со временем изменяются.**
> Определенная стратегия обхода zapret может работать какое-то время, но если меняется способ блокировки или обнаружения обхода блокировки, то она перестанет работать.
> В репозитории представлены множество различных стратегий для обхода. Если ни одна из них вам не помогает, то вам необходимо создать новую, взяв за основу одну из представленных здесь и изменив её параметры.
> Информацию про параметры стратегий вы можете найти [тут](https://github.com/bol-van/zapret/blob/master/docs/readme.md#nfqws).

- Убедитесь, что адрес ресурса записан в списках доменов или IP. Подробнее [тут](https://github.com/bol-van/zapret?tab=readme-ov-file#%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B0)

- Попробуйте в `service.bat` переключить `Switch Game Filter` и `Switch ipset`. На разных стратегиях они могут работать по-разному. **Подробнее, что они делают, [тут](https://github.com/Flowseal/zapret-discord-youtube?tab=readme-ov-file#%E2%84%B9%EF%B8%8F%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B8%D0%B5-%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D1%8F-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2)**

- Проверьте другие стратегии (**`ALT`**/**`МГТС`** и другие)

- Обновите файлы в папке [`bin`](./bin), взяв новые из [zapret-win-bundle/zapret-winws](https://github.com/bol-van/zapret-win-bundle/tree/master/zapret-winws)

- См. [#765](https://github.com/Flowseal/zapret-discord-youtube/issues/765)

### Требуется цифровая подпись драйвера WinDivert (Windows 7)

- Замените файлы `WinDivert.dll` и `WinDivert64.sys` в папке [`bin`](./bin) на одноименные из [zapret-win-bundle/win7](https://github.com/bol-van/zapret-win-bundle/tree/master/win7)

### При удалении с помощью [**`service.bat`**](./service.bat), WinDivert остается в службах

1. Узнайте название службы с помощью команды, в командной строке Windows (Win+R, `cmd`):

```cmd
driverquery | find "Divert"
```

2. Остановите и удалите службу командами:

```cmd
sc stop {название, которые вы узнали в шаге 1}

sc delete {название, которые вы узнали в шаге 1}
```

### Не нашли своей проблемы

* Создайте её [тут](https://github.com/Flowseal/zapret-discord-youtube/issues)

## 🗒️Добавление адресов прочих заблокированных ресурсов

Список блокирующихся адресов для обхода можно расширить, добавляя их в:
- [`list-general.txt`](./lists/list-general.txt) для доменов (поддомены автоматически учитываются)
- [`ipset-all.txt`](./lists/ipset-all.txt) для IP и подсетей

## ⭐Поддержка проекта

Вы можете поддержать проект, поставив :star: этому репозиторию (сверху справа этой страницы)

Также, вы можете материально поддержать разработчика zapret [тут](https://github.com/bol-van/zapret?tab=readme-ov-file#%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B0%D1%82%D1%8C-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%D0%B0)

<a href="https://star-history.com/#Flowseal/zapret-discord-youtube&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Flowseal/zapret-discord-youtube&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Flowseal/zapret-discord-youtube&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Flowseal/zapret-discord-youtube&type=Date" />
 </picture>
</a>

## ⚖️Лицензирование

Проект распространяется на условиях лицензии [MIT](https://github.com/Flowseal/zapret-discord-youtube/blob/main/LICENSE.txt)

## 🩷Благодарность участникам проекта

[![Contributors](https://contrib.rocks/image?repo=Flowseal/zapret-discord-youtube)](https://github.com/Flowseal/zapret-discord-youtube/graphs/contributors)

💖 Отдельная благодарность разработчику [zapret](https://github.com/bol-van/zapret) - [bol-van](https://github.com/bol-van)
