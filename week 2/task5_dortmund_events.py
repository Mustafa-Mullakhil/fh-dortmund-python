events = {
    "Museum Folkwang": "2026-09-19",
    "Deutsches Fußballmuseum": "2026-09-19",
    "Kunstmuseum Dortmund": "2026-09-19",
    "Naturmuseum Dortmund": "2026-09-19",
    "Brauerei Museum": "2026-09-19",
    "U-Bahn Museum": "2026-09-19",
}

night_of_museums_date = "2026-09-19"

print(f"=== Events during Night of Museums ({night_of_museums_date}) ===")
print()

for event, date in events.items():
    if date == night_of_museums_date:
        print(f"✓ {event} ({date})")
