import json

with open("en_sorted.json", "r", encoding="utf-8") as f:
    en_sorted = json.load(f)

with open("fr.json", "r", encoding="utf-8") as f:
    fr = json.load(f)

merged = {}
for key in en_sorted:
    merged[key] = fr.get(key, en_sorted[key])

with open("fr-complet.json", "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print("Fusion terminée : fr-complet.json généré.")
