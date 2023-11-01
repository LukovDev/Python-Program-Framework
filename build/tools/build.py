#
# build.py - Компилирует вашу программу в бинарный файл при помощи pyinstaller.
#


# Импортируем:
if True:
    import os
    import sys
    import json
    import shutil


# Очищаем консоль:
def clear_console() -> None:
    if sys.platform == "win32": os.system("cls")
    elif sys.platform == "darwin":
        os.system("clear && printf '\\e[3J'")
    else: os.system("clear")


# Сборка проекта:
def building() -> None:
    print(f"{' COMPILATION FILE: ':-^96}")
    os.system(f"set PYTHONOPTIMIZE={optimization_level}")
    os.system(f"pyinstaller {flags} -n=\"{program_name}\" ../../{main_file}")
    print("\n\n> COMPILATION IS SUCCESSFUL!")
    print(f"{'─'*96}\n\n")


# Финальные штрихи:
def final() -> None:
    print("Deleting temporary build files...")
    if os.path.isdir("../out/"): shutil.rmtree("../out/")
    if os.path.isdir("build"): shutil.rmtree("build")
    for file in os.listdir():
        if file.endswith(".spec"): os.remove(file)
    if os.path.isdir("./dist/"):
        shutil.copytree("./dist/", "../out/", dirs_exist_ok=True)
        shutil.rmtree("./dist/")
        shutil.copytree(f"../../{data_folder}", f"../out/{os.path.basename(os.path.normpath(data_folder))}")


# Если этот скрипт запускают:
if __name__ == "__main__":
    clear_console()  # Очищаем консоль.

    # Читаем конфигурационный файл сборки:
    with open("../config.json", "r+", encoding="utf-8") as f: config = json.load(f)

    # Преобразование данных конфигурации в переменные:
    if True:
        main_file          = config["main-file"]
        program_icon       = config["program-icon"]
        program_name       = config["program-name"]
        console_disabled   = config["console-disabled"]
        data_folder        = config["data-folder"]
        pyinstaller_flags  = config["pyinstaller-flags"]
        optimization_level = config["optimization-level"]

        # Генерация флагов компиляции:
        flags = ""
        for flag in pyinstaller_flags: flags += f"{flag} "
        if console_disabled:           flags +=  "--noconsole "
        if program_icon is not None:   flags += f"--icon=../../{program_icon} "

    building()  # Собираем проект.
    final()     # Удаляем мусор и собираем всё в одну папку.

    print("\n\nDone!\nBuild in folder: /build/out/")
