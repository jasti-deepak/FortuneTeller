# fortune.py - Version 1.1
import random

print("🔮 Welcome to Jasti Deepak Chowdary's Fortune Teller (22JE0429) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

fortunes = {
    "happy": [
        "✨ Your fortune: Great things await you, Jasti! Keep smiling. ✨",
        "🎉 You're on the right path, keep going strong!"
    ],
    "sad": [
        "💖 Don't worry, Jasti, brighter days are just ahead!",
        "🌈 Storms don't last forever. You got this!"
    ],
    "neutral": [
        "🌟 It's the perfect day to take a new step.",
        "🌓 Life is a blank canvas today—paint something beautiful."
    ],
    "stressed": [
        "🧘 Take a deep breath. Peace begins with you.",
        "💪 You're stronger than you think, Jasti!"
    ]
}

if mood in fortunes:
    print(random.choice(fortunes[mood]))
else:
    print("🤔 Sorry, I don't understand that mood.")
