from itertools import cycle
from random import randrange
from tkinter import Tk, Canvas, messagebox, font
import winsound

# Game Settings
canvas_width = 800
canvas_height = 400
egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.95
catcher_color = 'blue'
catcher_width = 100
catcher_height = 100
paused = False
score = 0
lives_remaining = 3
level = 1
high_score = 0

# Initialize the game window
win = Tk()
win.title("Egg Catcher Game")
c = Canvas(win, width=canvas_width, height=canvas_height, background='deep sky blue')
c.create_rectangle(-5, canvas_height - 100, canvas_width + 5, canvas_height + 5, fill='sea green', width=0)
c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
c.pack()

# UI Elements
color_cycle = cycle(['light blue', 'light pink', 'light yellow', 'light green', 'red', 'blue', 'green', 'black'])
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height
catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2, start=200, extent=140,
                       style='arc', outline=catcher_color, width=3)
score_text = c.create_text(10, 10, anchor='nw', font=('Arial', 18, 'bold'), fill='darkblue', text='Score: ' + str(score))
lives_text = c.create_text(canvas_width - 10, 10, anchor='ne', font=('Arial', 18, 'bold'), fill='darkblue',
                           text='Lives: ' + str(lives_remaining))
level_text = c.create_text(canvas_width / 2, 10, anchor='n', font=('Arial', 18, 'bold'), fill='darkblue',
                           text='Level: ' + str(level))
high_score_text = c.create_text(canvas_width / 2, 30, anchor='n', font=('Arial', 18, 'bold'), fill='darkblue',
                                text='High Score: ' + str(high_score))

eggs = []

# Functions
def play_sound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)

def play_background_music():
    winsound.PlaySound('background_music.wav', winsound.SND_ASYNC | winsound.SND_LOOP)

def create_eggs():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    win.after(egg_interval, create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        c.move(egg, 0, 10)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    if not paused:
        win.after(egg_speed, move_eggs)

def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    play_sound('egg_drop.wav')
    lose_a_life()
    if lives_remaining == 0:
        play_sound('game_over.wav')
        messagebox.showinfo('GAME OVER!', 'Final Score: ' + str(score))
        win.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text='Lives: ' + str(lives_remaining))

def catch_check():
    global lives_remaining
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if catcher_x < egg_x < catcher_x2 and catcher_y2 - egg_y2 < 40:
            eggs.remove(egg)
            c.delete(egg)
            increase_score(egg_score)
    for power_up in c.find_withtag("power-up"):
        (power_x, power_y, power_x2, power_y2) = c.coords(power_up)
        if catcher_x < power_x < catcher_x2 and catcher_y2 - power_y2 < 40:
            c.delete(power_up)
            lives_remaining += 1
            c.itemconfigure(lives_text, text='Lives: ' + str(lives_remaining))
    if not paused:
        win.after(100, catch_check)

def increase_score(points):
    global score, egg_speed, egg_interval, level, high_score
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    if score > high_score:
        high_score = score
        c.itemconfigure(high_score_text, text='High Score: ' + str(high_score))
    if score % 100 == 0:  # Every 100 points, increase level
        level += 1
        c.itemconfigure(level_text, text='Level: ' + str(level))
    play_sound('catch_egg.wav')
    c.itemconfigure(score_text, text='Score: ' + str(score))

def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 0:
        c.move(catcher, -20, 0)

def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width:
        c.move(catcher, 20, 0)

def toggle_pause(event):
    global paused
    if not paused:
        win.after_cancel(move_eggs)
        win.after_cancel(create_eggs)
        win.after_cancel(catch_check)
        paused = True
    else:
        move_eggs()
        create_eggs()
        catch_check()
        paused = False

# Key Bindings
c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.bind("<p>", toggle_pause)
c.focus_set()

# Game Loop Initialization
win.after(1000, create_eggs)
win.after(1000, move_eggs)
win.after(1000, catch_check)
play_background_music()

# Start the Game
win.mainloop()
