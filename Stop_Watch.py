# "Stopwatch: The Game"
# http://www.codeskulptor.org/#user40_3wY2ARreJe_19.py
import simplegui

# define global variables
time_elapsed = 0
num_success = 0
num_attempt = 0
started = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minute = int(t/600)
    second = int((t % 600)/10)
    tenth_sec = t % 10
    
    if second < 10:
        sec_str = "0" + str(second)
    else:
        sec_str = str(second)
    
    return (str(minute) + ":" + sec_str 
            + "." + str(tenth_sec))

def format_score(s,a):
    return str(s) + "/" + str(a)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global started
    timer.start()
    started = True
    
def stop():
    global time_elapsed, started
    global num_success, num_attempt
    
    timer.stop()
    if started: 
        num_attempt += 1
        if (time_elapsed % 10) == 0:
            num_success += 1
    started = False

def reset():
    global time_elapsed, started
    global num_success, num_attempt
    timer.stop()
    time_elapsed = 0
    num_success = 0
    num_attempt = 0
    started = False
    
# define event handler for timer with 0.1 sec interval
def increment():
    global time_elapsed
    time_elapsed += 1

# define draw handler
def display_time(canvas):
    global time_elapsed, num_success, num_attempt
    canvas.draw_text(format(time_elapsed),(110,170),
                     80,"White")
    canvas.draw_text(format_score(num_success,num_attempt),
                (280,60),50,"Green")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 400, 300)
frame.add_button("Start", start, 150)
frame.add_button("Stop", stop, 150)
frame.add_button("Reset", reset, 150)

# register event handlers
timer = simplegui.create_timer(100, increment)
frame.set_draw_handler(display_time)

# start frame
frame.start()
