import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from itertools import count, cycle
from datetime import datetime

class ImageLabel(tk.Canvas):  # класс для гифки
    def load(self, im):
        im = Image.open(im)  # путь до изображения
        frames = []  # сюда сохраняются кадры гиффки

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        self.first_frame = frames[0]  # Сохраняем первый кадр
        self.frames = cycle(frames)  # Создаем цикл из кадров
        self.delay = im.info['duration']
        self.create_image(0, 0, image=self.first_frame, anchor='nw', tags="IMG")

        if len(frames) == 1:
            self.itemconfig("IMG", image=self.first_frame)
        else:
            self.next_frame()

    def next_frame(self):
        if self.frames:
            self.itemconfig("IMG", image=next(self.frames))
            self.after(self.delay, self.next_frame)

def load_events():
    events = []
    with open('events.txt', 'r', encoding='utf-8') as f:
        for line in f:
            name, date_str = line.strip().split(',')
            date = datetime.strptime(date_str, '%Y-%m-%d')
            events.append((name, date))

    events.append(('сегодня сегодняшний день!!', datetime.now().strftime('%Y-%m-%d')))
    return events

def update_events(listbox):
    now = datetime.now().date()
    sorted_events = sorted(events, key=lambda e: datetime.strptime(e[1], '%Y-%m-%d') if isinstance(e[1], str) else e[1])
    listbox.delete(0, tk.END)
    for event in sorted_events:
        if isinstance(event[1], str):
            event_date = datetime.strptime(event[1], '%Y-%m-%d').date()
        else:
            event_date = event[1].date()

        days_left = (event_date - now).days

        if days_left < 0:
            listbox.insert(tk.END, f'прошло {-days_left} дней от {event[0]}')
            listbox.itemconfig(tk.END, {'fg': 'red'})  # Прошедшие события красным цветом
        elif days_left == 0:
            listbox.insert(tk.END, f'йоу чувак ты прям в моменте {event[0]}')
            listbox.itemconfig(tk.END, {'fg': 'orange'})  # События сегодня оранжевым цветом
        else:
            listbox.insert(tk.END, f'ждать осталось {days_left} дней до {event[0]}')
            listbox.itemconfig(tk.END, {'fg': 'lightblue'})  # Будущие события голубым цветом

if __name__ == '__main__':
    root = tk.Tk()
    root.title("БОЖЕ ПОМОГИ МНЕ ВЫЖИТЬ В ЭТОМ СУРОВОМ МИРЕ")
    root.geometry("800x500")
    icon = PhotoImage(file="images/alarm.png")
    root.iconphoto(False, icon)
    # root.wm_attributes("-topmost", True)
    # root.wm_attributes("-transparentcolor", "white")

    event_label = tk.Label(root, text="Планы по уничтожению человечества:", bg='#025719', font=("TkHeadingFont", "27", "bold"), foreground=('#ffcc00'), relief="ridge", cursor="heart")
    event_label.pack(side=tk.TOP, fill=tk.BOTH)

    # События
    events_listbox = tk.Listbox(root, font=("Courier", "15"), bg="black", cursor="coffee_mug")
    events_listbox.pack(side=tk.BOTTOM, fill=tk.BOTH)

    # Гифка
    lb = ImageLabel(root, width=800, height=437, cursor="gumby")
    lb.pack()
    file = ('images/giphy.gif')
    lb.load(file)

    events = load_events()

    update_events(events_listbox)
    root.after(86400000, update_events, events_listbox)  # Обновление событий раз в сутки

    root.mainloop()
