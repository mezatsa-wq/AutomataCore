AutomataCore

Application de construction, de visualisation et de simulation d’automates finis à partir d’expressions régulières.

1. Présentation du projet

AutomataCore est un projet informatique universitaire visant à développer une application capable de traiter des expressions régulières et de construire les automates finis correspondants.

L’application permettra à l’utilisateur de saisir un alphabet et une expression régulière, de vérifier sa validité, de générer les automates associés et de visualiser graphiquement leur structure.

Elle permettra également de tester différents mots afin de déterminer s’ils sont acceptés ou rejetés par l’automate généré.

2. Objectifs du projet

Les principaux objectifs sont :

* Comprendre et manipuler les expressions régulières.
* Vérifier la validité syntaxique des expressions régulières.
* Construire des automates finis à partir d’expressions régulières.
* Représenter graphiquement les automates générés.
* Simuler le fonctionnement des automates.
* Déterminer si un mot appartient ou non au langage reconnu par un automate.

3. Fonctionnalités prévues

L’application prévoit les fonctionnalités suivantes :

1. Gestion de l’alphabet : saisie et validation des symboles.
2. Analyse lexicale : reconnaissance des éléments constituant une expression régulière.
3. Analyse syntaxique : vérification de la structure et de la validité de l’expression.
4. Construction des automates : génération des automates à partir des expressions régulières.
5. Déterminisation : conversion d’un automate non déterministe en automate déterministe.
6. Visualisation graphique : représentation des états et des transitions avec Graphviz.
7. Simulation : test de mots pour vérifier leur acceptation ou leur rejet.
8. Explication des résultats : affichage du parcours effectué dans l’automate.

4. Technologies utilisées

Technologie	Utilisation
Python	Langage de programmation principal
Graphviz	Génération graphique des automates
PySide6	Création de l’interface graphique
Git	Gestion des versions
GitHub	Collaboration et hébergement du code

5. Organisation du projet

Le projet est organisé en plusieurs modules indépendants afin de faciliter le développement collaboratif.

* core/ : traitement des alphabets, expressions régulières et automates.
* visualization/ : génération et affichage graphique des automates.
* interface/ : interface utilisateur.
* tests/ : tests des différents modules.
* docs/ : documentation technique du projet.

6. Installation et configuration

Prérequis

* Python 3 installé.
* Git installé.
* Graphviz installé sur le système.
* Visual Studio Code (recommandé).

Cloner le projet

git clone https://github.com/mezatsa-wq/AutomataCore.git
cd AutomataCore

Créer un environnement virtuel

python -m venv .venv

Activer l’environnement virtuel

Sous Windows PowerShell :

.\.venv\Scripts\Activate.ps1

Installer les dépendances

python -m pip install -r requirements.txt

7. Collaboration et contribution

Ce projet est développé en équipe de cinq membres.

Chaque membre travaille sur une branche spécifique afin de faciliter la collaboration et d’éviter les conflits de modifications.

Règles de collaboration

* Ne pas modifier directement la branche main.
* Créer une branche pour chaque fonctionnalité.
* Utiliser des messages de commit explicites.
* Tester les modifications avant de les envoyer.
* Utiliser les Pull Requests pour intégrer le travail dans main.

Exemple de création d’une branche

git switch -c feature/nom-de-la-fonctionnalite

Envoyer ses modifications

git add .
git commit -m "Description des modifications"
git push -u origin feature/nom-de-la-fonctionnalite

8. Équipe du projet

Projet réalisé par une équipe de cinq étudiants.

* Membre 1 : mezatsa-wq (Mezatsa Roland Berthier)
* Membre 2 : Angelinakay (Awouna Assonga Ange)
* Membre 3 : À compléter
* Membre 4 : À compléter
* Membre 5 : À compléter

9. État d’avancement

Statut : En cours de développement.

Les fonctionnalités et la documentation seront progressivement enrichies au fur et à mesure de l’avancement du projet.

10. Licence

Projet universitaire. Les conditions de distribution et de réutilisation seront précisées ultérieurement.
