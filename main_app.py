# main_app.py
import tkinter as tk
from calculator_module import CalculatorWindow

class MainApplication:
    """Главное окно приложения с меню."""
    def __init__(self, root):
        self.root = root
        self.root.title("Главное меню")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Единый стиль (перекликается с модулем калькулятора)
        self.root.configure(bg="#e0e0e0")
        self.font = ("Arial", 12)

        self.create_widgets()

        # Переменная для хранения окна калькулятора
        self.calculator_window = None

    def create_widgets(self):
        """Создает виджеты главного окна."""
        # Заголовок
        title_label = tk.Label(self.root,
                               text="Моё приложение",
                               font=("Arial", 20, "bold"),
                               bg="#e0e0e0")
        title_label.pack(pady=30)

        # Рамка для кнопок
        button_frame = tk.Frame(self.root, bg="#e0e0e0")
        button_frame.pack(expand=True)

        # Кнопка для открытия калькулятора
        calc_button = tk.Button(button_frame,
                                text="🧮 Открыть калькулятор",
                                font=self.font,
                                width=25,
                                height=2,
                                bg="#2196F3",  # Синий цвет
                                fg="white",
                                activebackground="#1976D2",
                                command=self.open_calculator)
        calc_button.pack(pady=10)

        # Кнопка выхода
        exit_button = tk.Button(button_frame,
                                text="❌ Выход",
                                font=self.font,
                                width=25,
                                height=2,
                                bg="#9e9e9e",
                                fg="white",
                                activebackground="#757575",
                                command=self.root.quit)
        exit_button.pack(pady=10)

    def open_calculator(self):
        """Открывает окно калькулятора."""
        if self.calculator_window is None or not self.calculator_window.window.winfo_exists():
            # Создаем новый экземпляр калькулятора
            self.calculator_window = CalculatorWindow(self.root)
            self.calculator_window.show()
        else:
            # Если окно уже существует, просто показываем его
            self.calculator_window.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()