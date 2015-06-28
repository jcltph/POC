# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user40_rv3uzO4EOc_29.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH/2, HEIGHT/2]
    x_vel = random.randrange(120, 240)/60
    y_vel = random.randrange(60, 180)/60
    
    if direction == RIGHT:
        ball_vel = [x_vel, -y_vel]
    else:
        ball_vel = [-x_vel, -y_vel]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
    spawn_ball(random.choice([RIGHT, LEFT]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]   
    
    # collide and reflect off the top & bottom of the canvas
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
        
    # spawn new ball if the ball hit the gutter 
    # determine whether paddle and ball collide    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] >= paddle1_pos - PAD_HEIGHT/2 and
            ball_pos[1] <= paddle1_pos + PAD_HEIGHT/2):
            ball_vel[0] = -1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            spawn_ball(RIGHT)
            score2 += 1
            
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if (ball_pos[1] >= paddle2_pos - PAD_HEIGHT/2 and
            ball_pos[1] <= paddle2_pos + PAD_HEIGHT/2):
            ball_vel[0] = -1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            spawn_ball(LEFT)
            score1 += 1
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel >= PAD_HEIGHT/2 and
        paddle1_pos + paddle1_vel <= HEIGHT - PAD_HEIGHT/2):
        paddle1_pos += paddle1_vel
    
    if (paddle2_pos + paddle2_vel >= PAD_HEIGHT/2 and
        paddle2_pos + paddle2_vel <= HEIGHT - PAD_HEIGHT/2):
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos - PAD_HEIGHT/2],
                        [PAD_WIDTH, paddle1_pos - PAD_HEIGHT/2],
                        [PAD_WIDTH, paddle1_pos + PAD_HEIGHT/2],
                        [0, paddle1_pos + PAD_HEIGHT/2]],
                        1,"White","White")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos - PAD_HEIGHT/2],
                        [WIDTH, paddle2_pos - PAD_HEIGHT/2],
                        [WIDTH, paddle2_pos + PAD_HEIGHT/2],
                        [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT/2]],
                        1,"White","White")
    
    
    # draw scores
    canvas.draw_text(str(score1), [0.3*WIDTH,HEIGHT/4],50,"Green")
    canvas.draw_text(str(score2), [0.65*WIDTH,HEIGHT/4],50,"Green")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 4
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = acc
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

def reset():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', reset, 150)

# start frame
new_game()
frame.start()
