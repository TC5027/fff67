# fff67

J'ai mis en place une génération de code asm avec les paramètres **nombre de blocs** et **taille d'un bloc** en entrée
J'ai vu qu'il était possible de récupérer des performances counter directement avec rust (linux compatible seulement) et c'est ce que j'utilise pour générer mes données.
Je fais donc varier la taille de 8 à 16 32 et 64 et le nombre 512,1024 etc. et j'obtiens en lançant le script .sh un résultat comme le svg du répo par exemple.

Les résultats que j'ai c'est pour 1 run directement après la compilation de mon programme rust et donc avec des caches que je suppose non préparés pour mon programme (comme si cold cache du coup ?)
Les résultats que j'avais en lançant plusieurs fois l'éxécutable était le 1er run avait des valeurs plutot hautes et ceux d'après plutot équivalentes ensuite (plus basses) ce que je suppose du au cache effect ?

Pour l'instant j'ai testé sur 2 machines linux avec processeur intel et les résultats sont similaires malgré une grosse différence au niveau du hardware, icache et nombre de coeurs rien à voir tout ça

commande **lscpu**

La suite c'est faire ça pour des apple M1 mais du coup mon code pour les performances counter n'est pas réutilisable
https://github.com/siedentop/macos-perf pourrait m'aider

https://blog.cloudflare.com/branch-predictor/

https://gist.github.com/ibireme/173517c208c7dc333ba962c1f0d67d12 et asm dans du c du coup
