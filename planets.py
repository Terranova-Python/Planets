import tkinter as tk
from tkinter import ttk
from tkinter import *
import PIL
from PIL import ImageTk, Image

FULL_EARTH_DESC = 'Our home planet is the third planet from the Sun\n and the only place we know of so far that’s inhabited \nby living things.\n\n\nWhile Earth is only the fifth largest planet\nin the solar system, it is the only world\nin our solar system with liquid water on the surface.\nJust slightly larger than nearby Venus. Earth is\nthe biggest of the four planets closest to the Sun,\nall of which are made of rock and metal.\n\n\nThe name Earth is at least 1,000 years old.\nAll of the planets, except for Earth were named after Greek\nand Roman gods and goddesses.\nHowever, the name Earth is a Germanic word\nwhich simply means “the ground.”'
EARTH_FACT = '" Humans are the primary inahbitants of this beautiful planet, but they treat it very poorly... "'

FULL_JUPITER_DESC = 'Jupiter has a long history surprising \nscientists—all the way back to 1610 when Galileo Galilei \nfound the first moons beyond Earth. \nThat discovery changed the way we see the universe.\n\n\nFifth in line from the Sun, Jupiter is, \nby far, the largest planet in the solar system \nmore than twice as massive as all \nthe other planets combined.\n\n\nJupiter\'s familiar stripes \nand swirls are actually cold, windy clouds \nof ammonia and water, floating in an atmosphere of \nhydrogen and helium. Jupiter’s iconic Great Red Spot \nis a giant storm bigger than Earth that has \nraged for hundreds of years.'
JUPITER_FACT = 'One spacecraft — NASA\'s Juno orbiter — is currently exploring this giant world.'

FULL_NEPTUNE_DESC = 'Dark, cold and whipped by supersonic winds, \nice giant Neptune is the eighth and most distant \nplanet in our solar system.\n\n\nMore than 30 times as far from the Sun as Earth, Neptune \nis the only planet in our solar system not visible to the \nnaked eye and the first predicted by \nmathematics before its discovery. In 2011\nNeptune completed its first 165-year \norbit since its discovery in 1846.\n\n\n NASA\'s Voyager 2 is the only spacecraft \nto have visited Neptune up close. It flew past in \n1989 on its way out of the solar system.'
NEPTUNE_FACT = 'Neptune has 14 moons! \nThe most interesting moon is Triton, a frozen world that is spewing nitrogen ice and dust particles out from below its surface.\nIt was likely captured by the gravitationalnpull of Neptune. It is probably the coldest world in the solar system.'

FULL_MARS_DESC = 'The fourth planet from the Sun, \nMars is a dusty, cold, \ndesert world with a very thin atmosphere.\n\n\nThis dynamic planet has seasons, \npolar ice caps and weather and canyons and \nextinct volcanoes, evidence it was once \nan even more active past\n\n\n Mars is one of the most explored bodies \nin our solar system, and it\'s the only planet \nwhere we\'ve sent rovers to roam the\nalien landscape. NASA currently has three spacecraft \nin orbit, one rover and one lander on the surface.\nIndia and ESA also have spacecraft in orbit above Mars.\nThese robotic explorers have found lots of \nevidence that Mars was much wetter and warmer, \nwith a thicker atmosphere, \nbillions of years ago. NASA launched the next-generation \nPerseverance rover to Mars on July 30,2020.'
MARS_FACT = 'NASA\'s latest robotic mission to the Red Planet, Mars 2020, aims to help future astronauts \nbrave that inhospitable landscape.'

FULL_SATURN_DESC = 'Saturn is the sixth planet from the Sun \nand the second largest planet in our solar system.\n\n\nAdorned with thousands of beautiful ringlets,\n Saturn is unique among the planets. It is\nnot the only planet to have rings—made \nof chunks of ice and rock—but none \nare as spectacular or as complicated as Saturn\'s.\n\n\n Like fellow gas giant Jupiter, Saturn is a massive \nball made mostly of hydrogen and helium.'
SATURN_FACT = 'Nine Earths side by side would almost span Saturn’s diameter. That doesn’t include Saturn’s rings.'

FULL_VENUS_DESC = 'Venus is the second planet from the Sun and our \nclosest planetary neighbor. Similar in structure and size to \nEarth, Venus spins slowly in the opposite direction from \nmost planets.Its thick atmosphere traps heat in a runaway \ngreenhouse effect, making it the hottest planet \nin our solar system with surface temperatures hot enough \nto melt lead. Glimpses below the clouds \nreveal volcanoes and deformed mountains.\n\n\n Venus is named for the ancient Roman goddess of love \nand beauty, who was known as Aphrodite \nto the Ancient Greeks.'
VENUS_FACT = 'With a radius of 3,760 miles, Venus is roughly the same size as Earth — just slightly smaller'

FULL_URANUS_DESC = 'The first planet found with the aid of a telescope\nUranus was discovered in 1781 by astronomer William Herschel\n although he originally thought it was either a comet or a star.\n\n\nIt was two years later that the object was \nuniversally accepted as a new planet, \nin part because of observations by astronomer Johann Elert Bode.\nHerschel tried unsuccessfully to name his discovery \nGeorgium Sidus after King George III. Instead the \nscientific community accepted Bode\'s suggestion to name \nit Uranus, the Greek god of the sky, \nas suggested by Bode.'
URANUS_FACT = 'Uranus is known as the “sideways planet” because it rotates on its side.'

FULL_MERCURY_DESC = 'The smallest planet in our solar system and \nnearest to the Sun, Mercury is only \nslightly larger than Earth\'s Moon.\n\n\n From the surface of Mercury, the Sun would \nappear more than three times as large as it \ndoes when viewed from Earth,\nand the sunlight would be as \nmuch as seven times brighter. Despite its \nproximity to the Sun, Mercury is not the hottest \nplanet in our solar system \nthat title belongs to nearby Venus, \nthanks to its dense atmosphere.'
MERCURY_FACT = 'It is the closest planet to the Sun at a distance of about 36 million miles (58 million kilometers)'

FULL_PLUTO_DESC = 'Pluto—which is smaller than Earth’s Moon\nhas a heart-shaped glacier that’s the size of Texas\nThis fascinating world has blue skies, \nspinning moons, mountains as high as the Rockies\nand it snows—but the snow is red.\n\n\n Pluto’s atmosphere is thin and composed \nmostly of nitrogen, methane and carbon monoxide.\n\n\nPluto got its name from 11-year-old \nVenetia Burney of Oxford, England'
PLUTO_FACT = 'Pluto (minor planet designation: 134340 Pluto) is an icy dwarf planet in the Kuiper belt, a ring of bodies beyond the orbit of Neptune'

HEIGHT = 700
WIDTH = 900

root = tk.Tk()
root.title('Welcome to Terra Planets')

def planet(event):
    planet_type = clicked.get()

    if planet_type == option[0]:                                            # EARTH
        image = Image.open("earth.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()


        earth_label = tk.Label(desc_frame, text=FULL_EARTH_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=EARTH_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[1]:                                            # Jupiter
        image = Image.open("jupiter.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        planet_label = tk.Label(desc_frame, text=FULL_JUPITER_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        planet_label.pack()

        planet_fact = tk.Label(fact_frame, text=JUPITER_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        planet_fact.pack(side='left')

        item4.pack()

    if planet_type == option[2]:                                            # Neptune
        image = Image.open("neptune.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        planet_label = tk.Label(desc_frame, text=FULL_NEPTUNE_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        planet_label.pack()

        planet_fact = tk.Label(fact_frame, text=NEPTUNE_FACT,font=('Monotype Corsiva', 13), bg='#121212', fg='white')
        planet_fact.pack(side='left')

        item4.pack()

    if planet_type == option[3]:                                            # Mars
        image = Image.open("mars.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        planet_label = tk.Label(desc_frame, text=FULL_MARS_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        planet_label.pack()

        planet_fact = tk.Label(fact_frame, text=MARS_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        planet_fact.pack(side='left')

        item4.pack()

    if planet_type == option[4]:                                            # Saturn
        image = Image.open("saturn.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        earth_label = tk.Label(desc_frame, text=FULL_SATURN_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=SATURN_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[5]:                                            # Venus
        image = Image.open("venus.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        earth_label = tk.Label(desc_frame, text=FULL_VENUS_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=VENUS_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[6]:                                            # Uranus
        image = Image.open("uranus.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        earth_label = tk.Label(desc_frame, text=FULL_VENUS_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=URANUS_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[7]:                                            # Mercury
        image = Image.open("mercury.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()

        earth_label = tk.Label(desc_frame, text=FULL_MERCURY_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=MERCURY_FACT,font=('Monotype Corsiva', 16), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

    if planet_type == option[8]:                                            # Pluto
        image = Image.open("pluto.png")
        basewidth = 400

        canvas2 = tk.Canvas(root, height=400, width=400, bg='#171717',bd=0, highlightthickness=0, relief='ridge')
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        item4 = canvas2.create_image(225, 210, image=photo)

        canvas2.place(relx=0.05, rely=0.1, relheight=0.6, relwidth=0.5)

        for widget in desc_frame.winfo_children():
            widget.destroy()

        for widget in fact_frame.winfo_children():
            widget.destroy()


        earth_label = tk.Label(desc_frame, text=FULL_PLUTO_DESC, font=('Gadugi', 9), bg='#121212', fg='white')
        earth_label.pack()

        earth_fact = tk.Label(fact_frame, text=PLUTO_FACT,font=('Monotype Corsiva', 12), bg='#121212', fg='white')
        earth_fact.pack(side='left')

        item4.pack()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#171717')
canvas.pack()

desc_frame = tk.Frame(root, bg='#121212')              # This should have sliding bar for information
desc_frame.place(relx=0.6, rely=0.1, relheight=0.6, relwidth=0.35)

fact_frame = tk.Frame(root, bg='#121212')
fact_frame.place(relx=0.05, rely=0.72, relheight=0.2, relwidth=0.9)

option = ['Earth','Jupiter','Neptune','Mars','Saturn','Venus','Uranus','Mercury', 'Pluto'] # dropdown menu options
clicked = StringVar()
clicked.set(option[0])
drop = OptionMenu(root, clicked, *option)
drop.place(relx=0.3, rely=0.01, relheight=0.05, relwidth=0.1)

button = tk.Button(canvas, text='Get Info')
button.bind('<Button-1>', planet)
button.place(relx=0.4, rely=0.01, relheight=0.05, relwidth=0.1)

text = 'Welcome to the Planet App!\n \n \n Choose a planet to get started...\n\n\n Project by Anthony Terrano'
text2 = 'Fun Facts will show up in this box here!'

initial_label2 = tk.Label(fact_frame, text=text2, font=('Monotype Corsiva', 18), bg='#121212', fg='white')
initial_label2.pack(side='left')

initial_label = tk.Label(desc_frame, text=text, font=('Gadugi', 12), bg='#121212', fg='white')
initial_label.pack()

root.mainloop()
