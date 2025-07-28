# Petites commandes utiles pour traduire les fichiers de configuration de DCC Foundry VTT

Les commandes suivantes sont utiles pour trier, fusionner et compter les clés dans les fichiers JSON utilisés pour la traduction de DCC Foundry VTT.
Elles nécessitent Python et `jq` pour fonctionner correctement.
Elles sont conçues pour être exécutées àa la racine du projet.

## Pour trier les fichiers JSON par ordre alphabétique des clés

```bash
python3 tools/json_sort.py
```
Ce script produit une version triée du fichier `en.json` nommée `en_sorted.json`.

## Pour fusionner les fichiers JSON en un seul fichier

```bash
python3 tools/json_merge.py
```
Ce script fusionne les fichiers `en_sorted.json` et `fr.json` en un seul fichier nommé `fr-complet.json`. 
Il est utile pour combiner les traductions en français avec la version anglaise triée.

## Pour compter le nombre de clés dans un fichier JSON

```bash
jq 'paths | length' en.json | wc -l
jq 'paths | length' en_sorted.json | wc -l
jq 'paths | length' fr-complet.json | wc -l
```

Les commandes ci-dessus utilisent `jq` pour compter le nombre de chemins dans les fichiers JSON.
Après le lancement des scripts, ce nombre est affiché dans la console, doit être identique pour les trois fichiers.
