import os, sys, re, json

BASE_DIR = "/Users/green/Downloads/Takealot Refrigerator"

HERO_CDN = "https://files.catbox.moe/fvy3gd.jpg"
OPEN_CDN = "https://files.catbox.moe/3zcemq.jpg"
DISPENSER_CDN = "https://files.catbox.moe/yzkw8u.jpg"
INTERIOR_CDN = "https://files.catbox.moe/4rig0s.jpg"

HERO_TITLE = "Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox"
HERO_MODEL = "RB30J3611S9/FA"
HERO_PRICE = 2199
HERO_WAS_PRICE = 9999
HERO_DISCOUNT = 78
HERO_SAVINGS = 7800
STEP3_PRICE = 297

# 1. Update package.json
pkg_path = os.path.join(BASE_DIR, "package.json")
if os.path.exists(pkg_path):
    with open(pkg_path, "r") as f:
        pkg = json.load(f)
    pkg["name"] = "takealot-refrigerator"
    pkg["description"] = "Takealot South Africa Refrigerator Storefront & Automated Order Engine"
    with open(pkg_path, "w") as f:
        json.dump(pkg, f, indent=2)
    print("Updated package.json")

# 2. Update .env and .env.example
for env_name in [".env", ".env.example"]:
    epath = os.path.join(BASE_DIR, env_name)
    content = f"""PORT=3020
NODE_ENV=production
STORE_NAME=Takealot Refrigerator
GREENSEND_API_KEY=greensend_live_9b4a1f68e2
GREENSEND_SENDER_EMAIL=orders@takealot.co.za
DEFAULT_PRODUCT_TITLE=Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox
DEFAULT_PRODUCT_PRICE=2199
DEFAULT_PRODUCT_IMAGE={HERO_CDN}
"""
    with open(epath, "w") as f:
        f.write(content)
    print(f"Updated {env_name}")

# 3. Update server.js
server_path = os.path.join(BASE_DIR, "server.js")
with open(server_path, "r", encoding="utf-8") as f:
    s = f.read()

# Replace port
s = re.sub(r'const PORT = process\.env\.PORT \|\| \d+;', 'const PORT = process.env.PORT || 3020;', s)
s = re.sub(r'http://localhost:\d+', 'http://localhost:3020', s)

# Replace washing machine titles and image URLs
s = s.replace("Samsung 8kg Bottom Freezer Washing Machine with All-Around Cooling & Total No Frost", HERO_TITLE)
s = s.replace("Samsung 8kg Bottom Freezer Washing Machine", HERO_TITLE)
s = s.replace("Samsung 10kg AI Bottom Freezer with AddWash", "Samsung 432L Side-by-Side Inox Refrigerator")
s = s.replace("Samsung 8kg Bottom Freezer", HERO_TITLE)
s = s.replace("Washing Machine", "Refrigerator")
s = s.replace("washing machine", "refrigerator")
s = s.replace("washing-machine", "refrigerator")
s = s.replace("Washing Machines", "Refrigerators")
s = s.replace("washing machines", "refrigerators")

# Replace default amounts: 1899 or 2499 -> 2199
s = s.replace("1899", "2199")
s = s.replace("2499", "2199")
s = s.replace("6499", "9999")
s = s.replace("4600", "7800")
s = s.replace("4,600", "7,800")
s = s.replace("71%", "78%")

# Replace image URLs
s = re.sub(r'https://files\.catbox\.moe/[a-z0-9]+\.(?:jpg|png)', HERO_CDN, s)
s = s.replace("imagens/samsung_ww80_1_hero.jpg", "imagens/samsung_fridge_1_hero.jpg")
s = s.replace("imagens/samsung_ww80_2_door_open.jpg", "imagens/samsung_fridge_2_open.jpg")
s = s.replace("imagens/samsung_ww80_3_steam_drum.jpg", "imagens/samsung_fridge_3_dispenser.jpg")
s = s.replace("imagens/samsung_ww80_4_control_panel.jpg", "imagens/samsung_fridge_4_interior.jpg")

# Refrigerator specific email descriptions
s = s.replace("All-Around Cooling technology and Total No Frost cycle", "All-Around Cooling technology and Non-Plumbed Water Dispenser")
s = s.replace("All-Around Cooling", "All-Around Cooling")
s = s.replace("Total No Frost", "Multi Flow Frost Free")
s = s.replace("8kg Capacity", "300L Capacity")
s = s.replace("10kg AI AddWash", "432L Side-by-Side Inox")

with open(server_path, "w", encoding="utf-8") as f:
    f.write(s)
print("Updated server.js")

# 4. Clean data/orders.json and data/abandoned_checkouts.json
data_dir = os.path.join(BASE_DIR, "data")
os.makedirs(data_dir, exist_ok=True)
with open(os.path.join(data_dir, "orders.json"), "w") as f:
    json.dump([], f)
with open(os.path.join(data_dir, "abandoned_checkouts.json"), "w") as f:
    json.dump([], f)
print("Reset data/ storage files")

