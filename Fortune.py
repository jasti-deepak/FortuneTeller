# fortune.py - Version 1.0

print("🔮 Welcome to Jasti Deepak Chowdary's Fortune Teller (22JE0429) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Jasti! Keep smiling. ✨")
elif mood == "sad":
    print("🌧️ Your fortune: Tough times don't last. Keep your head up! 🌈")
elif mood == "neutral":
    print("🌓 Your fortune: Today is what you make of it. Choose wisely. 🌟")
else:
    print("🤔 Sorry, I don't understand that mood.")
