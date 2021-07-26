import os
from tkinter import *
from tkinter import filedialog
try:
    from mutagen.mp3 import MP3
except:
    os.system('pip install mutagen')
    from mutagen.mp3 import MP3

try:
    import pygame
except:
    os.system('pip install pygame')
    import pygame

import time


file_dir = os.getcwd().replace('\\' , '/')

assets = f'{file_dir}/assets' 

music_folder = assets.__add__('/music')

global pause_button

print(assets)  #TODO Remove after relese

print(music_folder) #TODO Remove after relese

icon = f'{assets}/icon2.ico'

root = Tk()
root.title('Music Player')
root.iconbitmap(icon)
root.geometry('500x350')
# Py gamie
pygame.mixer.init()

#Grab Song length time info
def play_time():
    current_time = pygame.mixer.music.get_pos() / 1000
    
    converted_current_time = time.strftime("%M:%S" , time.gmtime(current_time))
    status_bar.config(text=converted_current_time)

    status_bar.after(1000 , play_time)
    #  Add one the current song  number
    song = song_box.get(ACTIVE)
    song = f'{music_folder}/{song}.mp3'
    # Use mutagen
    #Load the song
    song_mut = MP3(song)
    # get song_lenght
    song_length = song_mut.info.length
    converted_song_length = time.strftime("%M:%S" , time.gmtime(song_length))
    #output the result to the status bar
    status_bar.config(text=f'Time Elapsed {converted_current_time}  of  {converted_song_length}      ')
    


def add_song():
    song = filedialog.askopenfilename(initialdir=music_folder , title="Choose a song" , filetypes=((".mp3 songs" , "*.mp3") , ))
    song = song.split(music_folder)
    # lst = song.split(music_folder)
    song_box.insert(END , song[1].replace('/','').replace('.mp3',''))

def add_many_song():
    songs = filedialog.askopenfilenames(initialdir=music_folder , title="Choose at least 2 songs" , filetypes=((".mp3 songs" , "*.mp3") , ))
    for song in songs:
        song = song.split(music_folder)
        # lst = song.split(music_folder)
        song_box.insert(END , song[1].replace('/','').replace('.mp3',''))




#play selected song
def play():
    song = song_box.get(ACTIVE)
    print('Now playing:',song)
    root.title(f"Now Playing: {song}")
    song = f'{music_folder}/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
    
    #Call the play_time function
    play_time()

#stop all songs
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    status_bar.config(text="|"*10)

#create global pause varible
global paused
paused = False

#pause the current song
def pause(is_paused):
    
    global paused
    paused = is_paused

    #pause
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        pause_button = Button(controls_frame , image=pause_btn , borderwidth=0,command=lambda: pause(paused))
        pause_button.grid(row=0,column=3 , padx=10)

    else:
        pygame.mixer.music.pause()
        paused = True
        pause_button = Button(controls_frame , image=pause_btn2 , borderwidth=0,command=lambda: pause(paused))
        pause_button.grid(row=0,column=3 , padx=10)
#Play the next song
def next_song():
    next_one = song_box.curselection()
    # print(next_one)
    #  Add one the current song  number
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    print('Now playing:',song)
    root.title(f"Now Playing: {song}")
    song = f'{music_folder}/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
    #clear the startus bar 
    song_box.selection_clear(0 ,END)
    #activate song bar
    
    song_box.activate(next_one)
    # Set the active bar to Next song
    song_box.selection_set(next_one , last=None)
    

#play previeous song in playlist
def prev_song():
    next_one = song_box.curselection()
    # print(next_one)
    #  Add one the current song  number
    next_one = next_one[0]-1
    song = song_box.get(next_one)
    print("Now playing:",song)
    root.title(f"Now Playing: {song}")
    song = f'{music_folder}/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)
    #clear the startus bar 
    song_box.selection_clear(0 ,END)
    #activate song bar
    song_box.activate(next_one)
    # Set the active bar to Next song
    song_box.selection_set(next_one , last=None)
    

def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def delete_all_song():
    #Delete a song
    song_box.delete(0,END)
    #Stop music(if any)
    pygame.mixer.music.stop()


#create playlist box
song_box  = Listbox(root , bg="black" , fg='green' , width = '70',selectbackground="#3d82d1" ,selectforeground='yellow')
song_box.pack(padx=1,pady=6)

#define player control button images
back_btn = PhotoImage(file=f'{assets}/back.png')
forward_btn = PhotoImage(file=f'{assets}/forward.png')
play_btn = PhotoImage(file=f'{assets}/reload.png')
pause_btn = PhotoImage(file=f'{assets}/pause2.png')
pause_btn2 = PhotoImage(file=f'{assets}/play.png')
stop_btn = PhotoImage(file=f'{assets}/stop.png')

#Create player control frame

controls_frame = Frame(root)

controls_frame.pack()

#create play control images

back_button     = Button(controls_frame , image=back_btn, borderwidth=0 , command=prev_song)
forward_button  = Button(controls_frame , image=forward_btn, borderwidth=0 ,command=next_song)
play_button     = Button(controls_frame , image=play_btn , borderwidth=0 ,command=play)
pause_button    = Button(controls_frame , image=pause_btn , borderwidth=0,command=lambda: pause(paused))
stop_button     = Button(controls_frame , image=stop_btn , borderwidth=0 , command=stop)



back_button.grid(row=0,column=0 , padx=10)
forward_button.grid(row=0,column=1 , padx=10)
play_button.grid(row=0,column=2 , padx=10)
pause_button.grid(row=0,column=3 , padx=10)
stop_button.grid(row=0,column=4 , padx=10)
# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add 'Add Song' menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label = "Add Songs" ,menu = add_song_menu)
add_song_menu.add_command(label = "Add one song to play-list" , command= add_song)
add_song_menu.add_command(label = "Add many songs to play-list" , command= add_many_song)

#Add delete Song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs" , menu=remove_song_menu)
remove_song_menu.add_command(label="Delete the selected song from playlist." , command=delete_song)
remove_song_menu.add_command(label="Delete all songs from playlist.",command=delete_all_song )

#create a statusbar
status_bar = Label(root , text= '' , bd=1 , relief=GROOVE , anchor=E)
status_bar.pack(fill=X , side=BOTTOM, ipady=2)

# my_slider = ttk.Scale(root , from_ = 0 , to_ = 100, orient = HORIZONTAL , value = 0 ,command = None).pack(pady = 20)

root.mainloop()