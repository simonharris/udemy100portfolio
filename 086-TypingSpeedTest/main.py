import tkinter as tk

from faker import Faker

from config import ENTRY as E, GAME as G, WINDOW as W


# lib -------------------------------------------------------------------------


def _normalise(text: str) -> str:
    return text.replace('.', '').replace('\n', '').lower()


def init_text():
    fake = Faker()
    sample_text = _normalise(fake.text(max_nb_chars=G['num_chars']))

    text_area.config(state=tk.NORMAL)
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, sample_text)
    text_area.config(state=tk.DISABLED)


def endgame():
    global running

    print('GAME OVER LOL')
    running = False


# event handlers --------------------------------------------------------------


def click_start():
    global running

    init_text()
    type_area.focus()
    button_start.config(state=tk.DISABLED)
    button_pause.config(state=tk.NORMAL)
    button_stop.config(state=tk.NORMAL)
    running = True


def click_pause():
    global running

    if running:
        button_pause.config(text='Unpause')
        running = False
    else:
        button_pause.config(text='Pause')
        running = True


def click_stop():
    button_start.config(state=tk.NORMAL)
    button_pause.config(state=tk.DISABLED, text='Pause')
    button_stop.config(state=tk.DISABLED)
    endgame()


# UI setup --------------------------------------------------------------------


# init state
running = False


# window
window = tk.Tk()
window.title(W['title'])
window.config(padx=W['padx'], pady=W['pady'], bg=W['bg'])
window.geometry(W['geometry'])


# the settings panel

frame_settings = tk.Frame(window, background='magenta')
frame_settings.grid(row=1, column=0, columnspan=12)


# the row of buttons

frame_buttons = tk.Frame(window, background='white')
frame_buttons.grid(row=1, column=0, columnspan=12)

button_start = tk.Button(frame_buttons, text='Start',
                         command=click_start,
                         highlightthickness=0, bd=0)
button_start.grid(column=2, row=0, columnspan="2")

button_pause = tk.Button(frame_buttons, text='Pause',
                         command=click_pause,
                        highlightthickness=0, bd=0,
                        state=tk.DISABLED,
                        )
button_pause.grid(column=4, row=0, columnspan="2")

button_stop = tk.Button(frame_buttons, text="Stop",
                        command=click_stop,
                        highlightthickness=0, bd=0,
                        state=tk.DISABLED,
                        )
button_stop.grid(column=6, row=0, columnspan="2")


# the text to be typed
text_area = tk.Text(window, background='lightgray', highlightthickness=1,
                    wrap=tk.WORD, font=(E['font_name'], E['font_size'], 'normal'),
                    height=E['height'], width=E['width'])
text_area.grid(column=1, row=2, columnspan=10)

text_area.config(foreground="black")
# text_area.insert(tk.END, "This is some sample text that you can't edit.")
text_area.config(state=tk.DISABLED)


# the typing boox
type_area = tk.Text(window, background='white', highlightthickness=1,
                    wrap=tk.WORD, font=(E['font_name'], E['font_size'], 'normal'),
                    height=E['height'], width=E['width'])
type_area.grid(column=1, row=3, columnspan=10)

type_area.config(foreground="black")
type_area.insert(tk.END, "")
type_area.config(state=tk.NORMAL)

window.mainloop()
