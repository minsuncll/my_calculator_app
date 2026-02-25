# calculator_module.py
import tkinter as tk
from tkinter import messagebox

class CalculatorWindow:
    """Класс, представляющий окно калькулятора."""
    def __init__(self, parent_window):
        self.parent = parent_window

        # Создание нового окна (Toplevel)
        self.window = tk.Toplevel(parent_window)
        self.window.title("Калькулятор")
        self.window.geometry("350x450")
        self.window.resizable(False, False)

        # Перехватываем закрытие окна, чтобы корректно вернуться в главное меню
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # --- Единый стиль ---
        self.bg_color = "#f0f0f0"
        self.btn_bg = "#ffffff"
        self.btn_fg = "#000000"
        self.btn_active_bg = "#d9d9d9"
        self.entry_bg = "#ffffff"
        self.entry_fg = "#000000"
        self.font = ("Arial", 14)

        self.window.configure(bg=self.bg_color)

        # --- Переменная для хранения ввода/вывода ---
        self.input_var = tk.StringVar()

        # --- Создание интерфейса ---
        self.create_widgets()

        # Центрируем окно относительно родителя
        self.center_window()

    def center_window(self):
        """Центрирует окно калькулятора относительно главного окна."""
        self.window.update_idletasks()
        parent_x = self.parent.winfo_x()
        parent_y = self.parent.winfo_y()
        parent_width = self.parent.winfo_width()
        parent_height = self.parent.winfo_height()

        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()

        x = parent_x + (parent_width // 2) - (window_width // 2)
        y = parent_y + (parent_height // 2) - (window_height // 2)

        self.window.geometry(f"+{x}+{y}")

    def create_widgets(self):
        """Создает все виджеты в окне калькулятора."""
        # --- Поле ввода (Entry) ---
        entry_frame = tk.Frame(self.window, bg=self.bg_color)
        entry_frame.pack(pady=10)

        entry = tk.Entry(entry_frame,
                         textvariable=self.input_var,
                         font=("Arial", 20),
                         width=18,
                         bd=5,
                         bg=self.entry_bg,
                         fg=self.entry_fg,
                         justify='right')
        entry.pack()

        # --- Рамка для кнопок ---
        buttons_frame = tk.Frame(self.window, bg=self.bg_color)
        buttons_frame.pack()

        # Список кнопок
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        row = 0
        col = 0
        for btn_text in buttons:
            # Определяем команду для кнопки
            if btn_text == 'C':
                cmd = self.clear_input
            else:
                # Для цифр и операторов используем лямбда-функцию,
                # передавая текст кнопки как аргумент по умолчанию (fix для замыкания)
                cmd = lambda x=btn_text: self.add_to_input(x)

            # Создание кнопки
            button = tk.Button(buttons_frame,
                               text=btn_text,
                               font=self.font,
                               width=4,
                               height=2,
                               bg=self.btn_bg,
                               fg=self.btn_fg,
                               activebackground=self.btn_active_bg,
                               command=cmd)
            button.grid(row=row, column=col, padx=2, pady=2)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # --- Кнопка "=" (занимает два столбца) ---
        equal_button = tk.Button(buttons_frame,
                                 text="=",
                                 font=self.font,
                                 width=10,  # Примерно два столбца
                                 height=2,
                                 bg="#4CAF50",  # Зеленый цвет для выделения
                                 fg="white",
                                 activebackground="#45a049",
                                 command=self.calculate_result)
        equal_button.grid(row=row, column=0, columnspan=4, padx=2, pady=10, sticky='ew')

        # --- Кнопка "Назад в меню" ---
        back_button = tk.Button(self.window,
                                text="← Назад в меню",
                                font=self.font,
                                bg="#f44336",  # Красный цвет
                                fg="white",
                                activebackground="#d32f2f",
                                command=self.on_close)
        back_button.pack(pady=5)

    def add_to_input(self, value):
        """Добавляет символ (цифру или оператор) в поле ввода."""
        current = self.input_var.get()
        # Простая защита от двух точек подряд
        if value == '.' and '.' in current.split()[-1] if current else False:
            return
        self.input_var.set(current + value)

    def clear_input(self):
        """Очищает поле ввода."""
        self.input_var.set("")

    def calculate_result(self):
        """Вычисляет выражение из поля ввода."""
        try:
            expression = self.input_var.get()
            if not expression:
                return

            # Важно: eval() используется для простоты, но в реальных проектах
            # лучше использовать безопасный парсер выражений.
            result = eval(expression)

            # Округляем до 10 знаков, чтобы избежать длинных хвостов
            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)

            self.input_var.set(str(result))
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль!")
            self.input_var.set("")
        except Exception:
            messagebox.showerror("Ошибка", "Некорректное выражение!")
            self.input_var.set("")

    def on_close(self):
        """Закрывает окно калькулятора и показывает главное окно."""
        self.window.destroy()
        self.parent.deiconify()  # Показываем главное окно

    def show(self):
        """Метод для отображения окна и скрытия главного."""
        self.parent.withdraw()  # Прячем главное окно
        self.window.deiconify()  # Показываем окно калькулятора