import logging
import sys
import os

from validator import validate_login, validate_registration

LOG_DIR = "Logs"
LOG_FILE = os.path.join(LOG_DIR, "file_txt.log")


def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | [%(levelname)-7s] | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
        ],
    )


def main():
    setup_logging()
    logging.info("Логгер успешно сконфигурирован")
    logging.info("Приложение запущено")


    while True:
        login = input("Введите логин: ")

        error = validate_login(login)

        if error is None:
            break

        print(error)
        logging.warning(f"Ошибка ввода логина: {error}")

    while True:
        password = input("Введите пароль: ")


        success, message = validate_registration(login, password, password)

        if not success:
            print(message)
            logging.warning(f"Ошибка ввода пароля: {message}")
            continue


        while True:
            confirm = input("Повторите пароль: ")

            if confirm == password:
                break

            print("Пароль и подтверждение не совпадают")
            logging.warning("Ошибка подтверждения пароля")

        break

    from validator import mask_password

    logging.info(
        f"Запрос на регистрацию. Логин='{login}', "
        f"пароль={mask_password(password)}, "
        f"подтверждение={mask_password(confirm)}"
    )

    logging.info(f"Результат: True. Сообщение: '{message}'")

    print(success)
    print(message)


if __name__ == "__main__":
    main()