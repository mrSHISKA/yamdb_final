# yamdb_final

<img src="https://github.com/mrSHISKA/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg" alt="Yamdb_workflow" style="max-width: 100%;">

### Краткое описание финального проекта по API:

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Произведению может быть присвоен жанр из списка предустановленных.
Добавлять произведения, категории и жанры может только администратор. Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.

### Настроен CI/CD

Запуск Flake8 и тестов, обновление образа DockerHub, деплой на сервер и автоматическая отправка сообщения в telegram в случае успеха.

### Полная документация API: http://84.201.138.179/redoc/

## Начало работы

1. Клонируйте репозиторий.
```
git clone <адрес репозитория>
```
2. Для работы с проектом локально - установите вирутальное окружение и зависимости.
```
python -m venv venv
pip install -r requirements.txt 
```
### Подготовка удаленного сервера для развертывания приложения

Для работы с проектом на удаленном сервере должен быть установлен Docker и docker-compose.
Установка docker на сервер:
```
sudo apt install docker.io 
```
Установка docker-compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
Затем необходимо задать правильные разрешения, чтобы сделать команду docker-compose исполняемой:
```
sudo chmod +x /usr/local/bin/docker-compose
```
Чтобы проверить успешность установки, запустите следующую команду:
```
docker-compose --version
```
Создайте папку проекта на удаленном сервере и скопируйте туда файлы docker-compose.yaml, Dockerfile, default.conf:
```
scp ./<FILENAME> <USER>@<HOST>:/home/<USER>/yamdb_final/
```
### Подготовка репозитория на GitHub

Для использования Continuous Integration и Continuous Deployment необходимо в репозитории на GitHub прописать Secrets - переменные доступа к вашим сервисам.
Переменые прописаны в workflows/yamdb_workflow.yaml

* DOCKER_PASSWORD, DOCKER_USERNAME - для загрузки и скачивания образа с DockerHub 
* USER, HOST, PASSPHRASE, SSH_KEY - для подключения к удаленному серверу 
* TELEGRAM_TO, TELEGRAM_TOKEN - для отправки сообщений в Telegram
## Технологии используемые в проекте
Python, Django, Django REST Framework, PostgreSQL, Nginx, Docker, GitHub Actions
## Развернутый проект можно посмотреть по ссылке:

http://84.201.138.179/api/v1/

### Разработчики:
**[Максим Титов](https://github.com/mrSHISKA)**. Настройка CI/CD проекта. Модели, view и эндпойнты: произведения, категории, жанры. Импорт из csv.
### Команда с прошлого спринта:
**[Дмитрий Тепикин](https://github.com/gatitobonito/)**. Управление пользователями: система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail.

**[Виктория Семеркова](https://github.com/vunrise/)**. Модели, view и эндпойнты: отзывы, комментарии, рейтинг произведений.
