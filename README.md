Добро пожаловать в наш проект! Этот проект использует Docker для управления сервисами и базой данных. В этом файле описаны основные команды для запуска и управления приложением.

## Запуск приложения

Для запуска приложения используйте следующую команду:

```sh
make app
```

# Для завершения работы приложения используйте:

```sh
make app-down
```

## Логирование

# Чтобы включить логирование приложения, используйте:

```sh
make app-logs
```

## Запуск базы данных

# Для запуска отдельно базы данных используйте:

```sh
make storages
```
# Эти команды поддерживают аналогичные постфиксы для управления состоянием:

make storages-down - остановка базы данных

make storages-logs - просмотр логов базы данных

## Требования

Docker
Make
