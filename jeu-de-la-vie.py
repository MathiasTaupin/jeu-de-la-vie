from tkinter import Tk, Button, Scale, HORIZONTAL, Frame, Label, messagebox
import random
from screeninfo import get_monitors

# Obtenir les dimensions de l'écran principal
screen = get_monitors()[0]
screen_width = screen.width
screen_height = screen.height

# Créer la fenêtre Tkinter et les boutons
root = Tk()
root.geometry(f"{screen_width}x{screen_height}")

# Constantes
TAILLE_GRILLE = 30  # Taille de la grille
VITESSE_INITIALE = 1000  # Vitesse initiale de la simulation en millisecondes
simulation_en_cours = False  # Variable pour suivre l'état de la simulation (démarrée ou non)
generation = 0  # Variable pour suivre le numéro de génération

# Initialiser la grille avec des états de cellules aléatoires
grille = [[random.choice([0, 0]) for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]

# Créer une liste pour les boutons représentant les cellules
boutons = []
for i in range(TAILLE_GRILLE):
    ligne = []
    for j in range(TAILLE_GRILLE):
        bouton = Button(root, width=2, height=1, borderwidth=1, relief="solid", command=lambda i=i, j=j: toggle_cell(i, j))
        bouton.grid(row=i, column=j)
        ligne.append(bouton)
    boutons.append(ligne)

# Initialiser les boutons avec les états de la grille
for i in range(TAILLE_GRILLE):
    for j in range(TAILLE_GRILLE):
        if grille[i][j] == 1:
            boutons[i][j]["bg"] = "black"  # Cellule vivante
        else:
            boutons[i][j]["bg"] = "white"  # Cellule morte

def toggle_cell(i, j):
    # Inverser l'état de la cellule
    grille[i][j] = 1 - grille[i][j]
    if grille[i][j] == 1:
        boutons[i][j]["bg"] = "black"
    else:
        boutons[i][j]["bg"] = "white"

def count_neighbors(i, j):
    # Compter le nombre de cellules voisines vivantes
    compteur = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            compteur += grille[(i + x) % TAILLE_GRILLE][(j + y) % TAILLE_GRILLE]
    return compteur

def update():
    global simulation_en_cours, generation
    if simulation_en_cours:
        # Mettre à jour la grille selon les règles du Jeu de la Vie
        nouvelle_grille = [[0 for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
        for i in range(TAILLE_GRILLE):
            for j in range(TAILLE_GRILLE):
                voisins = count_neighbors(i, j)
                if grille[i][j] == 1:
                    if voisins < 2 or voisins > 3:
                        nouvelle_grille[i][j] = 0
                    else:
                        nouvelle_grille[i][j] = 1
                else:
                    if voisins == 3:
                        nouvelle_grille[i][j] = 1
        for i in range(TAILLE_GRILLE):
            for j in range(TAILLE_GRILLE):
                grille[i][j] = nouvelle_grille[i][j]
                if grille[i][j] == 1:
                    boutons[i][j]["bg"] = "black"
                else:
                    boutons[i][j]["bg"] = "white"
        generation += 1  # Incrémenter le numéro de génération
        label_generation.config(text=f"Génération: {generation}")  # Mettre à jour le label
        root.after(vitesse.get(), update)

# Créer un bouton "Démarrer" pour démarrer la simulation
def start_simulation():
    global simulation_en_cours
    if not simulation_en_cours:
        simulation_en_cours = True
        update()  # Commencer la simulation

# Créer un bouton "Pause" pour mettre en pause la simulation
def pause_simulation():
    global simulation_en_cours
    simulation_en_cours = False

# Fonction pour fermer la fenêtre avec confirmation
def close_application():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter l'application?"):
        root.destroy()

# Bouton pour démarrer la simulation
btn_start = Button(root, text="Démarrer", command=start_simulation)
btn_start.place(x=screen_width - 150, y=110)
btn_start["bg"]="green"
btn_start["fg"]="white"


# Bouton pour mettre en pause la simulation
btn_pause = Button(root, text="Pause", command=pause_simulation)
btn_pause.place(x=screen_width - 150, y=170)
btn_pause["bg"]="yellow"
btn_pause["fg"]="black"

# Bouton pour fermer l'application
btn_quit = Button(root, text="Quitter", command=close_application)
btn_quit.place(x=screen_width - 250, y=110)
btn_quit["bg"]="red"
btn_quit["fg"]="white"

# Ajouter une échelle pour régler la vitesse
vitesse = Scale(root, from_=90, to=2000, orient=HORIZONTAL, label="Vitesse(ms/g)", troughcolor="blue", length="76" )
vitesse.set(VITESSE_INITIALE)  # Valeur initiale
vitesse.place(x=screen_width - 255, y=135)


# Ajouter un cadre pour le compteur de générations
frame_generation = Frame(root)
frame_generation.place(x=screen_width - 200, y=200)

# Ajouter un label pour afficher le numéro de génération
label_generation = Label(frame_generation, text=f"Génération: {generation}")
label_generation.pack()

root.mainloop()

#ici la commande pour instaler un module ==>==> pip install screeninfo
