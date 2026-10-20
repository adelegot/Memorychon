# 🥒 Memorychons

**Memorychons** est un jeu de paires (Memory) original et coloré développé en Python avec la bibliothèque graphique **PyQt5**. Plongez dans l'univers des cornichons à travers différents niveaux de difficulté ou affrontez un ami en duel !

## ✨ Fonctionnalités

* **Mode Solo évolutif (8 Niveaux) :** Progressez du Niveau 1 (2 paires, 2 vies) jusqu'au Niveau 8 (9 paires, 9 vies) avec une grille qui s'agrandit à chaque étape.
* **Mode 1VS1 Classique :** Affrontez un deuxième joueur sur le même écran (saisie des pseudos, gestion du tour par tour et calcul automatique du gagnant ou de l'égalité).
* **Interface adaptative :** Les éléments graphiques et les textes s'ajustent automatiquement à la résolution de votre écran.
* **Ambiance sonore et visuelle :** Effets sonores lors des victoires et défaites, polices d'écriture personnalisées et illustrations uniques sur le thème des cornichons.

## 📁 Structure du projet

Assurez-vous que votre dépôt respecte l'arborescence suivante pour que le jeu charge correctement les ressources :

```text
Memorychons/
├── memorychon.py       # Script principal du jeu
├── image/              # Cartes cornichons, fonds (fod.png, fod1.png) et icônes (heart.png, home.png, etc.)
├── son/                # Effets sonores (gagner.wav, perdu.wav)
└── fonts/              # Polices personnalisées (Copeland.otf, Quitle.otf)
