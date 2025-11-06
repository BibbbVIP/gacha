import random

# Character lists
five_star = ["Acheron", "Kafka", "Blade", "Seele", "Jingliu", "Fu Xuan"]
four_star = ["March 7th", "Dan Heng", "Asta", "Herta", "Pela", "Tingyun"]
three_star = ["Arlan", "Natasha", "Sampo", "Hook", "Sushang"]

def gacha_pull():
    """Pull one character"""
    chance = random.randint(1, 100)
    
    if chance <= 1:  # 1% chance for 5-star
        character = random.choice(five_star)
        return f"⭐⭐⭐⭐⭐ {character} (5-STAR!)"
    
    elif chance <= 11:  # 10% chance for 4-star
        character = random.choice(four_star)
        return f"⭐⭐⭐⭐ {character} (4-STAR)"
    
    else:  # 89% chance for 3-star
        character = random.choice(three_star)
        return f"⭐⭐⭐ {character} (3-STAR)"

def ten_pull():
    """Pull 10 characters at once"""
    print("\n🎲 PERFORMING 10-PULL...\n")
    results = []
    
    for i in range(10):
        result = gacha_pull()
        results.append(result)
        print(f"{i+1}. {result}")
    
    return results

# Main menu
print("=== HONKAI STAR RAIL GACHA ===\n")

while True:
    print("\nWhat do you want to do?")
    print("1. Single Pull")
    print("2. Ten Pull")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == "1":
        print("\n" + gacha_pull())
    
    elif choice == "2":
        ten_pull()
    
    elif choice == "3":
        print("\nThanks for playing!")
        break
    
    else:
        print("\nInvalid choice! Please enter 1, 2, or 3.")