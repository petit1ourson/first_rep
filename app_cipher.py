import tkinter as tk
from tkinter import ttk
import string

# def cleae_text(**kwargs):
#     for name in kwargs:
#         name.delete(1.0, tk.END)

def clicked(hide, show): # Общая функция для возврата к предыдущему фрейму
    hide.grid_forget() # Фрейм, который скрывается
    show.grid() # Фрейм, который отображается

def encrypt_text(): # функция, которая шифрует текст

    user_text_input = user_text.get("1.0", tk.END)
    user_rotn_input = user_rotn.get("1.0", tk.END)
    user_language = lang_var_encrypt.get()

    result_str = ''
    if user_language == 'Русский':
        for i in user_text_input:
                if i in string.punctuation or i in ' ':
                    result_str += i
                    continue

                ascii_sym = ord(i) + int(user_rotn_input)
                if i.isupper() and ascii_sym > 1071:
                    result_str += chr(ascii_sym - 32)
                elif i.islower() and ascii_sym > 1103:
                    result_str += chr(ascii_sym - 32)
                else:
                    result_str += chr(ascii_sym)
    elif user_language == 'Английский':
         for i in user_text_input:
            if i in string.punctuation or i in ' ':
                result_str += i
                continue


            ascii_sym = ord(i) + int(user_rotn_input)

            if i.isupper() and ascii_sym > 90:
                result_str += chr(ascii_sym - 26)
            elif i.islower() and ascii_sym > 122:
                result_str += chr(ascii_sym - 26)
            else:
                result_str += chr(ascii_sym)


    user_result.config(state=tk.NORMAL)
    user_result.delete(1.0, tk.END)
    user_result.insert(tk.END, result_str)
    user_result.config(state=tk.DISABLED)

# Функция, которая дешифрует текст
def decrypt_text():

    user_text_input = user_text_de.get("1.0", tk.END)
    user_rotn_input = user_rotn_de.get("1.0", tk.END)
    user_language = lang_var_decrypt.get()

    result_de_str = ''
    if user_language == 'Русский':
        for i in user_text_input:
            if i in string.punctuation or i in ' ':
                result_de_str += i
                continue


            ascii_subtraction = ord(i) - int(user_rotn_input) # номер по аски - число сдвига

            if i.isupper() and ascii_subtraction < 1040:
                result_de_str += chr(ascii_subtraction + 32)
            elif i.islower() and ascii_subtraction < 1072:
                result_de_str += chr(ascii_subtraction + 32)
            else:
                result_de_str += chr(ascii_subtraction)

    elif user_language == 'Английский':
        for i in user_text_input:
            if i in string.punctuation or i in ' ':
                result_de_str += i
                continue


            ascii_subtraction = ord(i) - int(user_rotn_input)

            if i.isupper() and ascii_subtraction < 65:
                result_de_str += chr(ascii_subtraction + 26)
            elif i.islower() and ascii_subtraction < 97:
                result_de_str += chr(ascii_subtraction + 26)
            else:
                result_de_str += chr(ascii_subtraction)

    user_result_de.config(state=tk.NORMAL)
    user_result_de.delete(1.0, tk.END)
    user_result_de.insert(tk.END, result_de_str)
    user_result_de.config(state=tk.DISABLED)

window = tk.Tk()
window.title("APP Caesar's Cipher")
window.geometry('600x300')

# Главный фрейм
main_frame = tk.Frame(window)
main_label1 = tk.Label(main_frame, text = "Добро пожаловать в APP Caesar's Cipher")
main_label1.grid(column=1, row=1)
encrypt_button = tk.Button(main_frame,
                           text="Зашифровать",
                           width=20,
                           height=3,
                           command=lambda: clicked(main_frame,encrypt_frame)
                           ,
                           )
encrypt_button.grid(column=1, row=2)
decrypt_button = tk.Button(main_frame,
                           text="Расшифровать",
                           width=20,
                           height=3,
                           command=lambda: clicked(main_frame,decrypt_frame)
                           )
decrypt_button.grid(column=1, row=3)
main_frame.grid() # показ контейнера

# Фрейм зашифровки
encrypt_frame = tk.Frame(window)
encrypt1 = tk.Label(encrypt_frame, text="Шифрование текста")
encrypt1.grid(column=2, row=1)

# Выбор языка шифровки
lang_en_label = tk.Label(encrypt_frame, text="Выберите язык шифровки")
lang_en_label.grid(column=1, row=2)
languages_encrypt = ["Русский", "Английский"]
lang_var_encrypt = tk.StringVar(value=languages_encrypt[0]) # сюда передаётся выбранная позиция

combobox_encrypt = ttk.Combobox(encrypt_frame, textvariable=lang_var_encrypt, values=languages_encrypt, state='readonly')
combobox_encrypt.grid(column=2, row=2)

return_main = tk.Button(encrypt_frame,
                        text="Вернуться в гланое меню",
                        command=lambda: clicked(encrypt_frame, main_frame)
                        )
return_main.grid(column=2, row=7)
encrypt2 = tk.Label(encrypt_frame, text="Введите текст")
encrypt2.grid(column=1, row=3)
user_text = tk.Text(encrypt_frame, width=20, height=2)
user_text.grid(column=2, row=3)
encrypt3 = tk.Label(encrypt_frame, text="Ввеедите число сдвига")
encrypt3.grid(column=1, row=4)
user_rotn = tk.Text(encrypt_frame, width=20, height=2)
user_rotn.grid(column=2, row=4)
button_encrypt = tk.Button(encrypt_frame,
                           text="Зашифровать",
                           command=encrypt_text)
button_encrypt.grid(column=2, row=5)
encrypt3 = tk.Label(encrypt_frame, text="Зашифрованный текст")
encrypt3.grid(column=1, row=6)
user_result = tk.Text(encrypt_frame, width=20, height=2)
user_result.grid(column=2, row=6)


# Фрейм Расшифровка текса
decrypt_frame = tk.Frame(window)
decrypt1 = tk.Label(decrypt_frame, text="Расшифровка текста")
decrypt1.grid(column=1, row=1)

# Выбор языка шифровки
lang_de_label = tk.Label(decrypt_frame, text="Выберите язык шифровки")
lang_de_label.grid(column=1, row=2)

languages_decrypt = ["Русский", "Английский"]
lang_var_decrypt = tk.StringVar(value=languages_decrypt[0]) # сюда передаётся выбранная позиция

combobox_decrypt = ttk.Combobox(decrypt_frame, textvariable=lang_var_decrypt, values=languages_decrypt, state='readonly')
combobox_decrypt.grid(column=2, row=2)

return_main_de = tk.Button(decrypt_frame,
                        text="Вернуться в гланое меню",
                        command=lambda: clicked(decrypt_frame, main_frame)
                        )
return_main_de.grid(column=2, row=7)
decrypt2 = tk.Label(decrypt_frame, text="Введите текст")
decrypt2.grid(column=1, row=3)
user_text_de = tk.Text(decrypt_frame, width=20, height=2)
user_text_de.grid(column=2, row=3)
encrypt3_de = tk.Label(decrypt_frame, text="Введите число сдвига")
encrypt3_de.grid(column=1, row=4)
user_rotn_de = tk.Text(decrypt_frame, width=20, height=2)
user_rotn_de.grid(column=2, row=4)
button_decrypt = tk.Button(decrypt_frame,
                           text="Расшифровать",
                           command=decrypt_text)
button_decrypt.grid(column=2, row=5)
decrypt3 = tk.Label(decrypt_frame, text=("Расшифрованный текст"))
decrypt3.grid(column=1, row=6)
user_result_de = tk.Text(decrypt_frame, width=20, height=2)
user_result_de.grid(column=2, row=6)


window.mainloop()
