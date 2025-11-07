import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

class AHP_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Система поддержки принятия решений - Шкала отношений")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Данные
        self.criteria = ["Стоимость", "Инфраструктура", "Климат", "Доступность"]
        self.alternatives = ["Турция", "Китай", "Грузия", "Таиланд"]
        self.matrix_data = np.array([
            [1, 2, 3, 4],
            [1, 2, 2, 3],
            [3, 2, 1, 3],
            [2, 3, 4, 1]
        ])
        
        self.create_interface()
        self.calculate_results()
    
    def create_interface(self):
        # Основной фрейм
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Заголовок
        title_label = ttk.Label(main_frame, 
                               text="🎯 Система поддержки принятия решений\nМетод анализа иерархий (шкала отношений)",
                               font=('Arial', 16, 'bold'),
                               justify='center')
        title_label.pack(pady=(0, 20))
        
        # Контейнер для основного содержимого
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Левая панель - матрица
        left_frame = ttk.LabelFrame(content_frame, text="Матрица оценок альтернатив", padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Правая панель - результаты
        right_frame = ttk.LabelFrame(content_frame, text="Результаты работы алгоритма", padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        # Создаем матрицу
        self.create_matrix_table(left_frame)
        
        # Создаем область результатов
        self.create_results_area(right_frame)
        
        # Кнопки управления
        self.create_control_buttons(left_frame)
        
        # Методы аттестирования
        self.create_methods_list(right_frame)
    
    def create_matrix_table(self, parent):
        # Создаем фрейм для таблицы
        table_frame = ttk.Frame(parent)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Создаем Treeview для матрицы
        columns = ["Альтернативы"] + self.alternatives
        self.matrix_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=6)
        
        # Настраиваем заголовки
        for col in columns:
            self.matrix_tree.heading(col, text=col, anchor='center')
            if col == "Альтернативы":
                self.matrix_tree.column(col, width=120, anchor='center')
            else:
                self.matrix_tree.column(col, width=100, anchor='center')
        
        # Добавляем данные
        for i in range(4):
            row_data = [f"Альтернатива {i+1}"] + [str(self.matrix_data[i][j]) for j in range(4)]
            self.matrix_tree.insert("", "end", values=row_data)
        
        # Полоса прокрутки
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.matrix_tree.yview)
        self.matrix_tree.configure(yscrollcommand=scrollbar.set)
        
        self.matrix_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def create_results_area(self, parent):
        # Фрейм для результатов
        results_frame = ttk.Frame(parent)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Текстовое поле для результатов
        self.results_text = tk.Text(results_frame, height=12, width=50, font=("Consolas", 11),
                                   bg='#f8f9fa', relief='solid', bd=1)
        self.results_text.pack(fill=tk.BOTH, expand=True)
    
    def create_control_buttons(self, parent):
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, pady=(15, 0))
        
        # Кнопки
        self.calculate_btn = ttk.Button(button_frame, text="Рассчитать", 
                                       command=self.calculate_results)
        self.calculate_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = ttk.Button(button_frame, text="Очистить все", 
                                   command=self.clear_all)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        self.edit_btn = ttk.Button(button_frame, text="Изменить", 
                                  command=self.edit_matrix)
        self.edit_btn.pack(side=tk.LEFT, padx=5)
        
        self.delete_btn = ttk.Button(button_frame, text="Удалить", 
                                    command=self.delete_selected)
        self.delete_btn.pack(side=tk.LEFT, padx=5)
        
        # Выбор метода
        methods_frame = ttk.Frame(button_frame)
        methods_frame.pack(side=tk.RIGHT, padx=5)
        
        ttk.Label(methods_frame, text="Метод:").pack(side=tk.LEFT)
        self.method_var = tk.StringVar(value="Метод отношений")
        methods_combo = ttk.Combobox(methods_frame, textvariable=self.method_var,
                                    values=["Метод отношений", "Процедура Борда", "Минимальное расстояние",
                                           "Разушение контуров", "Процедура Коулленда", "Модиф. процедура Коулленда"],
                                    state="readonly", width=20)
        methods_combo.pack(side=tk.LEFT, padx=5)
    
    def create_methods_list(self, parent):
        # Фрейм для методов
        methods_frame = ttk.LabelFrame(parent, text="Методы аттестирования")
        methods_frame.pack(fill=tk.X)
        
        methods = [
            "• Разушение контуров",
            "• Процедура Борда", 
            "• Процедура Коулленда",
            "• Модиф. процедура Коулленда",
            "• Метод отношений",
            "• Минимальное расстояние"
        ]
        
        for method in methods:
            ttk.Label(methods_frame, text=method, font=('Arial', 10)).pack(anchor='w', padx=10, pady=2)
    
    def calculate_weights(self):
        """Расчет весов методом анализа иерархий"""
        matrix = self.matrix_data
        n = len(matrix)
        
        # Нормализация по столбцам
        normalized = matrix / matrix.sum(axis=0)
        # Веса как среднее по строкам
        weights = normalized.mean(axis=1)
        
        return weights
    
    def calculate_results(self):
        try:
            weights = self.calculate_weights()
            
            # Ранжирование
            ranked_indices = np.argsort(weights)[::-1]
            
            # Суммовое расстояние
            total_distance = np.sum(np.abs(self.matrix_data - weights.reshape(-1, 1)))
            
            # Обновляем текстовое поле с результатами
            self.results_text.delete(1.0, tk.END)
            
            results = "Результат работы алгоритма:\n\n"
            weights_str = "[" + "; ".join([f"{w:.3f}" for w in weights]) + "]"
            results += f"Вектор предпочтений: {weights_str}\n"
            results += f"Суммовое расстояние: {total_distance:.2f}\n\n"
            results += "Места:\n"
            
            for i, idx in enumerate(ranked_indices):
                results += f"Место {i+1}: {self.alternatives[idx]};\n"
            
            self.results_text.insert(1.0, results)
            
            # Диалог с ЛПР
            best_alternative = self.alternatives[ranked_indices[0]]
            response = messagebox.askyesno(
                "Рекомендация системы", 
                f"СИСТЕМА РЕКОМЕНДУЕТ: {best_alternative}\n\n"
                f"Согласны ли вы с рекомендацией системы?"
            )
            
            if response:
                messagebox.showinfo("Решение принято", "✅ Окончательное решение принято!")
            else:
                messagebox.showinfo("Пересмотр", "🔄 Рекомендуется пересмотреть оценки в матрице")
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка расчета: {e}")
    
    def clear_all(self):
        # Сбрасываем матрицу к исходным значениям
        self.matrix_data = np.array([
            [1, 2, 3, 4],
            [1, 2, 2, 3],
            [3, 2, 1, 3],
            [2, 3, 4, 1]
        ])
        self.update_matrix_display()
        self.calculate_results()
        messagebox.showinfo("Очистка", "Матрица очищена!")
    
    def delete_selected(self):
        selected = self.matrix_tree.selection()
        if selected:
            self.matrix_tree.delete(selected)
            messagebox.showinfo("Удаление", "Выбранная строка удалена!")
        else:
            messagebox.showwarning("Внимание", "Выберите строку для удаления!")
    
    def edit_matrix(self):
        # Создаем окно редактирования
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Редактирование матрицы")
        edit_window.geometry("400x300")
        edit_window.transient(self.root)
        edit_window.grab_set()
        
        ttk.Label(edit_window, text="Выберите ячейку для редактирования:", 
                 font=('Arial', 11)).pack(pady=10)
        
        # Выбор строки и столбца
        selection_frame = ttk.Frame(edit_window)
        selection_frame.pack(pady=10)
        
        ttk.Label(selection_frame, text="Строка:").grid(row=0, column=0, padx=5)
        row_var = tk.StringVar(value="1")
        row_combo = ttk.Combobox(selection_frame, textvariable=row_var,
                                values=["1", "2", "3", "4"], state="readonly", width=10)
        row_combo.grid(row=0, column=1, padx=5)
        
        ttk.Label(selection_frame, text="Столбец:").grid(row=0, column=2, padx=5)
        col_var = tk.StringVar(value="Турция")
        col_combo = ttk.Combobox(selection_frame, textvariable=col_var,
                                values=self.alternatives, state="readonly", width=10)
        col_combo.grid(row=0, column=3, padx=5)
        
        # Поле для нового значения
        ttk.Label(edit_window, text="Новое значение:").pack(pady=5)
        value_var = tk.StringVar()
        value_entry = ttk.Entry(edit_window, textvariable=value_var, width=10, font=('Arial', 12))
        value_entry.pack(pady=5)
        
        def apply_edit():
            try:
                row = int(row_var.get()) - 1
                col = self.alternatives.index(col_var.get())
                new_value = int(value_var.get())
                
                self.matrix_data[row, col] = new_value
                self.update_matrix_display()
                self.calculate_results()
                
                messagebox.showinfo("Успех", "Значение успешно изменено!")
                edit_window.destroy()
                
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректное целое число!")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при редактировании: {e}")
        
        # Кнопки
        button_frame = ttk.Frame(edit_window)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Применить", command=apply_edit).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Отмена", command=edit_window.destroy).pack(side=tk.LEFT, padx=10)
    
    def update_matrix_display(self):
        # Очищаем текущие данные
        for item in self.matrix_tree.get_children():
            self.matrix_tree.delete(item)
        
        # Добавляем обновленные данные
        for i in range(4):
            row_data = [f"Альтернатива {i+1}"] + [str(self.matrix_data[i][j]) for j in range(4)]
            self.matrix_tree.insert("", "end", values=row_data)

def main():
    try:
        root = tk.Tk()
        app = AHP_GUI(root)
        root.mainloop()
    except Exception as e:
        print(f"Ошибка запуска: {e}")

if __name__ == "__main__":
    main()