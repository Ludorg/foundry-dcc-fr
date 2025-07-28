import json

with open("en_sorted.json", "r", encoding="utf-8") as f:
    en_sorted = json.load(f)

with open("fr.json", "r", encoding="utf-8") as f:
    fr = json.load(f)

merged = {}
todo = {}
tocheck = {}

for key in en_sorted:
    if key not in fr:
        print(f"Warning: Key '{key}' not found in French JSON, using English value.")
        todo[key] = en_sorted[key]

    merged[key] = fr.get(key, en_sorted[key])

for key in fr:
    if key not in en_sorted:
        print(
            f"Warning: Key '{key}' found in French JSON but not in English JSON, using French value. CHECK IF THIS IS INTENTIONAL."
        )
        tocheck[key] = fr[key]


with open("fr-complet.json", "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)
print("Fusion terminée : fr-complet.json généré.")

with open("todo.json", "w", encoding="utf-8") as f:
    json.dump(todo, f, ensure_ascii=False, indent=2)
print("Liste des clés manquantes enregistrée dans todo.json.")

with open("tocheck.json", "w", encoding="utf-8") as f:
    json.dump(tocheck, f, ensure_ascii=False, indent=2)
print("Liste des clés à vérifier tocheck.json.")
