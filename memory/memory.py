import simplegui
import random
state = 0
deck_1 = []
deck_2 = []
memory_deck = []
Turns = 0
width = 50
exposed = [False,False,False,False,False,False,
False,False, False,False,False,False,
False,False,False,False]
saved_index = []
card1 = 0
card2 = 0

dictionary = {}
# helper function to initialize globals
def new_game():
    global deck_1, deck_2, memory_deck, Turns, exposed
    deck_1 = range (1,9)
    random.shuffle(deck_1)
    deck_2 = range (1,9)
    random.shuffle(deck_2)
    memory_deck = deck_1 + deck_2
    Turns = 0
    exposed = [False, False, False, False, False, False,
    False, False, False, False, False, False,
    False, False,False, False]
    saved_index = []
    card1 = 0
    card2 = 0
    print memory_deck

# define event handlers
def mouseclick(pos):
    global index, state, saved_index, exposed, Turns, memory_deck, card1, card2
    index = pos[0] // 50
    if not exposed[index]:
        if state == 0:
            exposed[index] = True
            saved_index.append(index)
            card1 = memory_deck[saved_index[0]]
            state = 1
        elif state == 1:
            exposed[index] = True
            saved_index.append(index)
            card2 = memory_deck[saved_index[1]]
            state = 2
            Turns += 1
            if card1 == card2:
                exposed[saved_index[0]] = True
                exposed[saved_index[1]] = True
                state = 0
                saved_index = []
            elif state == 2:
                if card1 != card2:
                    exposed[saved_index[0]] = False
                    exposed[saved_index[1]] = False
                    saved_index = []
                    exposed[index] = True
                    card1 = memory_deck[index]
                    saved_index.append(index)
                    state = 1
                else:
                    return

# cards are logically 50x100 pixels in size
def draw(c):
    for num in memory_deck:
        c.draw_line([(memory_deck.index(num)*50)-3,0],[(memory_deck.index(num)*50)-3,100], 5, "White")
        c.draw_line([(memory_deck.index(num)*50)+395,0],[(memory_deck.index(num)*50)+395,100], 5, "White")

    # draw card numbers
    for num in range(len(memory_deck)):
        num_pos=[10+50*num,62]
        if exposed[num] == True:
            c.draw_text(str(memory_deck[num]), num_pos, 42, 'White', 'serif')
        elif exposed[num] == False:
            c.draw_line([num*50,100],[num*50+44,100], 200, "Green")

            label.set_text("Turns = "+str(Turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# start the game
new_game()
frame.start()
