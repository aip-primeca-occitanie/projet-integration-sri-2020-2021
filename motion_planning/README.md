# Planification de mouvement du bras manipulateur de Tiago

## Installation

Pour être assuré d'avoir toutes les dépendances nécessaires liées à la partie de planification de mouvement du bras, le plus simple est de partir du projet de démo Tiago et de cloner ce repository dans `~/tiago_public_ws/src/`. Assurez vous de suivre toutes les étapes de la partie _1. Source-based installation_ du tutoriel [Installing TIAGo Simulation](http://wiki.ros.org/Robots/TIAGo/Tutorials/Installation/TiagoSimulation).

## Lancement

`cd ~/tiago_public_ws`

Dans un premier terminal, lancer Gazebo pour la simulation de Tiago :

```
source ./devel/setup.bash
roslaunch tiago_pick_demo pick_simulation.launch
```

Dans un deuxième, lancer les nodes de motion planning.

```
source ./devel/setup.bash
roslaunch motion_planning pick_sri.launch
```

## Détails techniques

Les [Actions Servers et Clients ROS](http://wiki.ros.org/actionlib) sont des serveurs, écris ici en Python, qui se lancent sur un node et qui permettent de traiter des services sans être bloquants. Les traitements de services se font à travers une requête d'un _ActionGoal_ d'un client dont la structure du message est définie dans `action/MyAction.action`. Le serveur pourra retourner _ActionResult_ pour permettre au client d'avoir un feedback sur sa requête.

## Fonctionnement

_Le développement n'a pas pu être complêtement terminé et est sujet à divers bugs et disfonctionnements. Voici cependant le fonctionnement et l'architecture que l'équipe de motion planning avait en tête pour cette partie._

Le fichier `pick_sri.launch` va lancer les nodes suivants :

- `motion_planning_server` : action serveur et point d'entrée pour le lancement des tâches pick and place.
- `pick_and_place_server` : action serveur qui traite toutes les demandes liés à la planification de mouvement du bras. Il communique avec `motion_planning_server`.
- `node_prise` : action serveur qui lit les efforts de la pince pour en déduire si un objet à bien été attrapé. 
- `test_client` (pour débugger) : action client pour tester le bon fonctionnement. Il envoie un goal défini en dur à `motion_planning_server` pour simuler l'envoie d'une position de l'objet par l'équipe de perception.

Note : 

`pick_client.py` définie des mouvements de pick and place que `motion_planning_serveur` va exécuter.
