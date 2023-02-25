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

[asm in c](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(filename:'1',fontScale:14,fontUsePx:'0',j:1,lang:___c,selection:(endColumn:16,endLineNumber:5,positionColumn:16,positionLineNumber:5,selectionStartColumn:16,selectionStartLineNumber:5,startColumn:16,startLineNumber:5),source:'%0Avoid+getCountry()+%7B%0A%09asm(%22jmp+label2%5Cn%5Ct%22%0A++++++++%22nop%5Cn%5Ct%22%0A++++++++%22label2:%5Cn%5Ct%22)%3B%0A%0A++++++++//+asm!!(%22jmp+2f%22,+%22nop%22,+%22nop%22,+%22nop%22,+%22nop%22,+%222:%22)%0A%7D%0A'),l:'5',n:'0',o:'C+source+%231',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:cg102,deviceViewOpen:'1',filters:(b:'0',binary:'1',binaryObject:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'1',intel:'0',libraryCode:'0',trim:'1'),flagsViewOpen:'1',fontScale:14,fontUsePx:'0',j:1,lang:___c,libs:!(),options:'-O3',selection:(endColumn:1,endLineNumber:1,positionColumn:1,positionLineNumber:1,selectionStartColumn:1,selectionStartLineNumber:1,startColumn:1,startLineNumber:1),source:1),l:'5',n:'0',o:'+x86-64+gcc+10.2+(Editor+%231)',t:'0')),k:50,l:'4',n:'0',o:'',s:0,t:'0')),l:'2',n:'0',o:'',t:'0')),version:4)
