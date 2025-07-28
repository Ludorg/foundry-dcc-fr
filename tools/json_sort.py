import json
from collections import OrderedDict

# Load the JSON file
with open("en.json", "r") as file:
    data = json.load(file)

# Sort the JSON by keys
sorted_data = OrderedDict(sorted(data.items()))

# Save the sorted JSON back to the file
with open("en_sorted.json", "w") as file:
    json.dump(sorted_data, file, indent=4)
