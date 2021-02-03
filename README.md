# flask-app

(working with GitHub Actions)

Как работать с GitHub Actions/Workflow:

Workflow — это набор команд, которые выполнятся в виртуальном окружении после того, как произойдёт какое-то событие-триггер (например запушить код в репозиторий).
   
1. Зайдите в свой репозиторий на GitHub, перейдите во вкладку Actions, для 
   создания директории .github/workflows с шаблоном main.yml нажмите ссылку
   set up a workflow yourself
   
2. Перейдите в настройки репозитория Settings-Secrets-New secret
   
3. Задайте имя переменным и нажмите Add secret:
   
    DOCKER_USERNAME
   
    DOCKER_PASSWORD
   
    USER - сохраните имя пользователя для подключения к серверу
   
    HOST - сохраните IP-адрес вашего сервера
    
    SSH_KEY - приватный ключ от своего сервера
   
    PASSPHRASE - пароль при создании ssh-ключа
   
    TELEGRAM_TO - ID своего телеграм-аккаунта. Узнать свой ID можно у бота @userinfobot.
   
    TELEGRAM_TOKEN - токен вашего бота. Получить этот токен можно у бота @BotFather.