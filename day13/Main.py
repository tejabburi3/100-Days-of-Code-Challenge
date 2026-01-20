import data_higher_lower as data
import random

print("🎮 Hi! Welcome to Higher or Lower Game\n")

datasets = [
    data.google_search_data,
    data.social_followers,
    data.youtube_channels,
    data.movies
]

score = 0

def random_option():
    category = random.choice(datasets)
    cat = datasets.index(category)

    if cat == 0:
        print("🔍 Choose which has HIGHER Google search volume\n")
    elif cat == 1:
        print("👥 Choose who has MORE social media followers\n")
    elif cat == 2:
        print("▶️ Choose which YouTube channel has MORE subscribers\n")
    elif cat == 3:
        print("🎬 Choose which movie has HIGHER IMDb rating\n")

    item1 = random.choice(category)
    item2 = random.choice(category)

    while item1 == item2:
        item2 = random.choice(category)

    return item1, item2

while True:
    item1, item2 = random_option()

    print(f"Option 1: {item1['name']}")
    print(f"Option 2: {item2['name']}")

    user_choice = int(input("Which one you choose? 1 or 2: "))

    if user_choice == 1:
        chosen = item1
        other = item2
    else:
        chosen = item2
        other = item1

    if chosen["value"] >= other["value"]:
        print("✅ Correct Answer!\n")
        score += 1
    else:
        print("❌ Wrong Answer!")
        print(f"🏆 Final Score: {score}")
        print("🎮 Play Again ☺️")
        break
