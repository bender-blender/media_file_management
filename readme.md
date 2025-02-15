# Описание паттерна
Паттерн Адаптер (Adapter) — это структурный паттерн проектирования, который позволяет объектам с несовместимыми интерфейсами работать вместе. Он действует как "мост" между двумя несовместимыми интерфейсами, позволяя им взаимодействовать без изменения их кода.

## Цель паттерна
Целью паттерна Адаптер является:

- Обеспечение совместимости между классами с несовместимыми интерфейсами.
- Упрощение интеграции новых классов в существующую систему без изменения уже работающего кода.
- Снижение зависимости между классами, что делает систему более гибкой и расширяемой.

## Проблема, которую решает паттерн
Паттерн Адаптер решает проблему, когда:

- Существующий код использует один интерфейс, а новый код или библиотека предоставляет другой интерфейс.
- Необходимо интегрировать старые компоненты с новыми без изменения их исходного кода.
- Нужно обеспечить совместимость между различными системами или модулями.

## Когда использовать паттерн
Паттерн Адаптер рекомендуется использовать в следующих случаях:

- Когда необходимо интегрировать новые классы в существующую систему с несовместимыми интерфейсами.
- Когда нужно использовать сторонние библиотеки или API, которые не соответствуют вашему коду.
- Когда вы хотите создать универсальный интерфейс для работы с различными классами.


## Взаимодействие классов и методов

1.Интерфейс MediaPlayer определяет метод play(), который должен реализовываться всеми медиаплеерами.

2.Класс AudioPlayer реализует метод play() для воспроизведения mp3 файлов.

3.Класс VlcPlayer имеет метод play_vlc(), который не соответствует интерфейсу MediaPlayer.
    
4.Адаптер VlcAdapter реализует интерфейс MediaPlayer и использует экземпляр VlcPlayer для воспроизведения файлов формата VLC. Он преобразует вызовы метода play() в вызовы метода play_vlc().

5.Клиентский код создает экземпляры адаптируемых классов и использует адаптер для воспроизведения файлов.

