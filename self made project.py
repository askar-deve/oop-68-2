comment = []
users_database = {}


class Userclass:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.status = 'Пользователь'

    def get_info(self):
        print(f'логин-{self.login},\nкласс-{self.status}')


class Admin(Userclass):
    def __init__(self, login, password, admin_code):
        super().__init__(login, password)
        self.admin_code = admin_code
        self.status = "admin"

    def get_info(self):
        print(f'логин-{self.login},\nкласс-{self.status}\n===============================================')


someuser = Userclass('userr', 'supreme')
askar = Admin('askar', 'dm', 'ADMINALLOW')
users_database[askar.login] = askar
users_database[someuser.login] = someuser

entry = 0
current_user = None

while True:
    while entry <= 0:
        print(f'===============================================================\n1)да\n2)нет\n0)выход из программы')
        account = input('есть ли у вас учетная запись? ')

        if account == '0':
            print("Программа завершена.")
            exit()
        if account == '1' or account =="да":
            user_login = input('введите свой логин: ')
            if user_login not in users_database:
                print('логин не найден!')
                continue
            user_password = input('введите свой пароль: ')
            if users_database[user_login].password == user_password:
                print('вход успешно выполнен!')
                current_user = users_database[user_login]
                entry += 1
        elif account == '2' or account == 'нет':
            print(f'==========================================================\nсоздайте новую учетную запись!')
            new_login = input(f'\nвведите новый логин: ')
            new_password = input('введите новый пароль: ')
            new_admin_code = input('введите токен если есть: ')

            if new_login not in users_database:
                if new_admin_code == 'ADMINALLOW':
                    users_database[new_login] = Admin(new_login, new_password, new_admin_code)
                    print('новый администратор добавлен!')
                else:
                    users_database[new_login] = Userclass(new_login, new_password)
                    print('аккаунт успешно добавлен!')
                account = '1'
    while entry > 0:
        print(f'\nВы вошли как: {current_user.login} [{current_user.status}]')
        print(f'1) да\n2) нет\nДля выхода напишите "exit" или "0"')
        answer = input(f'нравятся ли вам мои проекты? ')

        if answer == 'exit' or answer == '0':
            entry = 0
            exit()

        try:
            if answer == '1':
                print(
                    'спасибо, мы рады слышать ваши отзывы\n===========================================================================')
            elif answer == '2':
                print('пожалуйста, оставьте комментарий или жалобу ')
                report = input('комментарий: ')
                message = f"[{current_user.login}]: {report}"
                comment.append(message)

                print('ваш отзыв сохранен!')
                print('===========================================================================')
            elif answer == '/get_comments':
                if current_user.status == 'admin':
                    print('\n=== ВСЕ КОММЕНТАРИИ ===')
                    if not comment:
                        print('(список пуст)')
                    for x in comment:
                        print(x)
                else:
                    print('команда не найдена!')
                print('===========================================================================')
            elif answer == '/switch_acc':
                print('выполняется выход\n')
                entry = 0
            elif answer == '/get_info':
                current_user.get_info()
            else:
                print('Неверная команда или выберите 1 или 2.')
                print('===========================================================================')
        except ValueError:
            print('введите число')