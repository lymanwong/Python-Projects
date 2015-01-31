# define global variables
import simplegui

counter = 0
ticker = 0
wins = 0
tries = 0
tenth_of_second = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(counter):
    global tenth_of_second
    tenth_of_second = int(counter % 10)
    seconds = int((counter/10) % 10)
    tenths = int((counter/100) % 6)
    minutes = int(counter / 600)
    return str(minutes)+":"+str(tenths)+str(seconds)+ "."+str(tenth_of_second)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global clock_ticking, tries, ticker
    if ticker == 0:
        timer.start()
        tries += 1
        ticker = 1

        def stop_button():
            global clock_ticking, ticker
            if ticker == 1:
                timer.stop()
                if tenth_of_second == 0:
                    global wins
                    ticker = 0
                    wins = wins + 1
                    return wins
                else:
                    ticker = 0

#def reset():
def reset_button():
    timer.stop()
    global counter
    counter = 0
    global ticker
    ticker = 0
    global tries
    tries = 0
    global wins
    wins = 0

# define event handler for timer with 0.1 sec interval
def start():
    global counter
    counter += .1
    format(counter)

# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(counter)), [75,100], 36, "White")
    canvas.draw_text(str(wins)+"/"+ str(tries), [150,25], 25, "White")

# create frame
frame = simplegui.create_frame("Home", 200, 200)
timer = simplegui.create_timer(10, start)
button1 = frame.add_button("Start", start_button)
button2 = frame.add_button("Stop", stop_button)
button3 = frame.add_button("Reset", reset_button)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
