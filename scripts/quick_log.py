from datetime import date

today = date.today().isoformat()

lines = [
    "Base Airdrop Lab - Quick Log",
    f"Date: {today}",
    "",
    "Done:",
    "- Small repo update",
    "- Progress logged in notes/",
]

print("\n".join(lines))
