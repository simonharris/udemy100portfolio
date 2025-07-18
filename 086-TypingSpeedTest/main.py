import tkinter as tk

from faker import Faker

from config import (
    ENTRY as E,
    GAME as G,
    TIMER as T,
    WINDOW as W
)


# lib -------------------------------------------------------------------------


def _normalise(text: str) -> str:
    return text.replace('.', '').replace('\n', '').lower()


def init_text():
    fake = Faker()
    sample_text = _normalise(fake.text(max_nb_chars=G['num_chars']))

    text_target.config(state=tk.NORMAL)
    text_target.delete('1.0', tk.END)
    text_target.insert(tk.END, sample_text)
    text_target.config(state=tk.DISABLED)

    text_typed.delete('1.0', tk.END)


def endgame():
    global running

    print('GAME OVER LOL')
    running = False


def start_timer():
    print("starting timer")
    # populate label, maybe
    # ...
    decrement_timer()


def decrement_timer():
    global time_left

    # wait 1 sec
    window.after(1000, decrement_timer)

    # decrement var
    time_left.set(time_left.get() - 1)


# event handlers --------------------------------------------------------------


def click_start():
    global running

    init_text()
    text_typed.focus_force()
    button_start.config(state=tk.DISABLED)
    button_pause.config(state=tk.NORMAL)
    button_stop.config(state=tk.NORMAL)
    start_timer()
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

# timer stuff
time_left = tk.IntVar()
time_left.set(G['time_allowed'])


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
text_target = tk.Text(window, background='lightgray', highlightthickness=1,
                    wrap=tk.WORD, font=(E['font_name'], E['font_size'], 'normal'),
                    height=E['height'], width=E['width'])
text_target.grid(column=1, row=2, columnspan=10)

text_target.config(foreground="black")
# text_area.insert(tk.END, "This is some sample text that you can't edit.")
text_target.config(state=tk.DISABLED)


# the typing box
text_typed = tk.Text(window, background='white', highlightthickness=1,
                    wrap=tk.WORD, font=(E['font_name'], E['font_size'], 'normal'),
                    height=E['height'], width=E['width'])
text_typed.grid(column=1, row=3, columnspan=10)

text_typed.config(foreground="black")
text_typed.insert(tk.END, "")
text_typed.config(insertbackground='black')
text_typed.config(state=tk.NORMAL)


# the timer
label_time = tk.Label(window,
                      textvariable=time_left,
                      font=(T['font_name'], T['font_size'])
                    )
label_time.grid(row=5, columnspan=12)
label_time_unit = tk.Label(window,
                      text=f"seconds",
                      font=(T['font_name'], 12)
                    )
label_time_unit.grid(row=6, columnspan=12)


window.mainloop()
