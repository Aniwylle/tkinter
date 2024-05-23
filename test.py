from tkinter import Tk, Label, simpledialog, messagebox, Button, font, Canvas

# Простое окно
root = Tk() # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна   
root.geometry("300x250") # устанавливаем размеры окна   
label = Label(text="Hello TKinter") # создаем текстовую метку
label.pack() # размещаем метку в окне
root.mainloop() # запускаем основной цикл

# Диалоги тет-а-тет
root = Tk()
query = simpledialog.askstring('Ваш вопрос', 'Сколько будет 2+2?') # Задаём вопрос 
messagebox.showinfo('Ответ', 'Вы ввели: ' + query)# Показываем сообщение
answer = messagebox.askyesno('Закончить', 'Вы уверены?')# Вопрос да или нет

if answer:
   print('До свидания.')

# Кнопки
root = Tk()
root.title("Обычная кнопка")
root.geometry("250x200")

myFont = font.Font(family='Georgia', size=30)

btn = Button(text="Button")
btn['font'] = myFont
btn.pack()
 
root.mainloop()

# Фигуры
root = Tk()
root.title('Фигуры')

canvas = Canvas(root, width=400, height=400)

oval = canvas.create_oval(35, 20, 365, 350, width=15, outline='blue', fill='black')
square = canvas.create_rectangle(35, 20, 365, 350, width=15, outline='yellow', fill='black')
triangle = canvas.create_polygon(35, 200, 365, 200, 200, 35, width=15, outline='red', fill='black')

canvas.pack()
root.mainloop()