
# 🧬 Jeu de la Vie – Simulation en Tkinter

Ce projet est une implémentation graphique du célèbre **Jeu de la Vie** de Conway en Python, utilisant la bibliothèque **Tkinter** pour l'interface graphique.

## 🖥️ Fonctionnalités

- Grille dynamique de cellules vivantes et mortes
- Simulation du Jeu de la Vie avec les règles classiques
- Interface responsive adaptée à la taille de l'écran
- Contrôles intuitifs :
  - 🎬 **Démarrer** la simulation
  - ⏸️ **Mettre en pause**
  - 🛑 **Quitter l'application**
  - 📈 **Régler la vitesse** de génération
  - 🔢 **Affichage du numéro de génération**

## 📸 Aperçu

Chaque cellule peut être activée ou désactivée manuellement. À chaque génération, les cellules évoluent selon leurs voisines.

## 🚀 Installation

1. Clone le dépôt :

```bash
git clone https://github.com/ton-utilisateur/nom-du-repo.git
cd nom-du-repo
```

2. Installe les dépendances :

```bash
pip install screeninfo
```

3. Lance l'application :

```bash
python mini_projet2_final_Mathias.py
```

## 📚 Règles du Jeu de la Vie

- Une cellule vivante avec 2 ou 3 voisines reste vivante
- Une cellule morte avec exactement 3 voisines devient vivante
- Dans tous les autres cas, la cellule meurt ou reste morte

## 🛠️ Fait avec

- Python 🐍
- Tkinter 🎨
- Screeninfo 🖥️

## 📄 Licence

Ce projet est libre d'utilisation à des fins éducatives ou personnelles.
