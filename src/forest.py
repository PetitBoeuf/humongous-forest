from tkinter import * 
import random
import datetime 
import time

def create_forest():

    burn_button.config(state="disabled")

    for line in range(rows):

        forest_field.append([" "] * columns)

        for column in range(columns):

            afforestation_rate = random.randint(1,10)

            if afforestation_rate <= 7 : 
                color = 'green'
            else : 
                color = 'black'
            forest_field[line][column] = my_sublime_canvas.create_rectangle(column * cell_size,
                                                                            line * cell_size,
                                                                            column * cell_size + cell_size,
                                                                            line * cell_size + cell_size,
                                                                            outline = "",
                                                                            fill = color)


def display_little_forest(field):

    """
    textForet.delete("1.0", END)

    #print(len(field))
    for line in range(len(field)):
        #label['text'] = label['text'] + str(field[line])
        textForet.insert(END, str(field[line]) + "\n")
        #print(field[line])
    """
    

def arsoooooon(event):

    x1 = event.x    
    y1 = event.y
    column_current_click = x1 // cell_size
    line_current_click = y1 // cell_size 
    
    if my_sublime_canvas.itemcget(forest_field[line_current_click][column_current_click], "fill") == 'green' : 
        my_sublime_canvas.itemconfig(forest_field[line_current_click][column_current_click], fill = 'red')
        burn_button.config(state="normal")

def humongous_arson():
    
    """
    On va créer une étape de transition (willBecomeFire) car autrement la boucle du dessus sera infinie puisqu'elle
    mettra les voisins en feu, et quand on passera a la case d'après, celle-ci mettra ses voisins en feu
    etc car on vérifie le "fire".
    """ 
    if isThereFire():
        for line in range(rows):
            for column in range(columns):
                """
                REMETTRE CA SI ON VEUT QUE LES CENDRES REVIENNENT A L'ETAT 'NORMAL'
                if my_sublime_canvas.itemcget(forest_field[line][column], "fill") == 'gray' : 
                    my_sublime_canvas.itemconfig(forest_field[line][column], fill = 'black')

                """

                if my_sublime_canvas.itemcget(forest_field[line][column], "fill") == 'yellow' : 
                    my_sublime_canvas.itemconfig(forest_field[line][column], fill = 'gray')

                if my_sublime_canvas.itemcget(forest_field[line][column], "fill") == '#FF8C00' : 
                    my_sublime_canvas.itemconfig(forest_field[line][column], fill = 'yellow')                    

                """
                real version for below
                if my_sublime_canvas.itemcget(forest_field[line][column], "fill") == 'red' : 
                    my_sublime_canvas.itemconfig(forest_field[line][column], fill = 'gray')
                """
                
                if my_sublime_canvas.itemcget(forest_field[line][column], "fill") == 'red' : 
                    my_sublime_canvas.itemconfig(forest_field[line][column], fill = '#FF8C00')
                
                    if line != rows - 1 : 
                        """
                        if forest_field[line + 1][column] == "tree" : 
                            forest_field[line + 1][column] = "willBecomeFire"
                        """
                        if my_sublime_canvas.itemcget(forest_field[line + 1][column], "fill") == 'green' : 
                            my_sublime_canvas.itemconfig(forest_field[line + 1][column], fill = 'orange')

                    """
                    if forest_field[line - 1][column] == "tree" : 
                        forest_field[line - 1][column] = "fire"
                    """
                    if line != 0 : 
                        if my_sublime_canvas.itemcget(forest_field[line - 1][column], "fill") == 'green' : 
                            my_sublime_canvas.itemconfig(forest_field[line - 1][column], fill = 'red')

                    if column != columns - 1:
                        """
                        if forest_field[line][column + 1] == "tree" :  
                            forest_field[line][column + 1] = "willBecomeFire"
                        """
                        if my_sublime_canvas.itemcget(forest_field[line][column + 1], "fill") == 'green' : 
                            my_sublime_canvas.itemconfig(forest_field[line][column + 1], fill = 'orange')
                    
                    """
                    if forest_field[line][column - 1] == "tree" : 
                        forest_field[line][column - 1] = "willBecomeFire"
                    """
                    if column != 0:
                        if my_sublime_canvas.itemcget(forest_field[line][column - 1], "fill") == 'green' : 
                            my_sublime_canvas.itemconfig(forest_field[line][column - 1], fill = 'orange')

                """ 
                if forest_field[line - 1][column] == "willBecomeFire" :
                    forest_field[line - 1][column] = "fire"
                """
                if my_sublime_canvas.itemcget(forest_field[line - 1][column], "fill") == 'orange' : 
                    my_sublime_canvas.itemconfig(forest_field[line - 1][column], fill = 'red')
            
        for column in range(columns):
            """
            if forest_field[cell_number - 1][column] == "willBecomeFire" : 
                forest_field[cell_number - 1][column] = "fire"
            """
            if my_sublime_canvas.itemcget(forest_field[rows - 1][column], "fill") == 'orange' : 
                my_sublime_canvas.itemconfig(forest_field[rows - 1][column], fill = 'red')


        fire_window.after(spreading_speed,humongous_arson)

def lets_start_an_arson():
    if isThereFire() : 
        after_id = fire_window.after_idle(humongous_arson)        


def pause_arson():
    my_sublime_canvas.delete("all")
    window_creation()
    create_forest()

def check_clicked():
    if pause == True : 
        return True
    return False


def isThereFire():
    for line in range(rows):
        for column in range(columns):
            """
            if forest_field[line][column] == "fire" : 
                return True
            """
            fire_color_list = ['red', 'orange' , 'yellow']
            if my_sublime_canvas.itemcget(forest_field[line][column], "fill") in fire_color_list: 
                return True
    return False

def window_creation():
    
    fire_window.minsize(width_window,height_window)    
    fire_window.maxsize(width_window,height_window)  

    fire_window.title("Superbe simulateur de feux de forêt.")

    fire_window.rowconfigure(0, weight=2)
    fire_window.rowconfigure(1, weight=1)
    fire_window.rowconfigure(2, weight=1)
    fire_window.columnconfigure(0, weight=2)
    fire_window.columnconfigure(1, weight=1)


fire_window  = Tk()

#----------Parameters working--------

rows = 20
columns = 50
cell_size = 20
spreading_speed = 100


canvas_width = cell_size * columns + cell_size
canvas_height = cell_size * rows + cell_size

width_window = canvas_width
height_window = canvas_height + 45 


#----------Parameters working--------

#fter_id = None

window_creation()

my_sublime_canvas = Canvas(fire_window, width = canvas_width, height = canvas_height)
my_sublime_canvas.grid(row = 0, columnspan = 2)

my_sublime_canvas.bind('<Button-1>', arsoooooon)

burn_button = Button(fire_window, text="Burn everything.", state=DISABLED, command=lets_start_an_arson, height = 2)
burn_button.grid(row = 1, column = 0)

regenerate_button=Button(fire_window, text="Stop & generate a new forest.", command=pause_arson, height = 2)
regenerate_button.grid(row = 2, column = 0)

#Création de la matrice
forest_field = []
create_forest()


fire_window.mainloop()

