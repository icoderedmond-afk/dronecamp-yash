
import random
import time

symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "💎", "7"]

coins = 100

print("🎰 PYTHON SLOT MACHINE 🎰")
print("========================")

for spin_number in range(10):

    if coins <= 0:
        break

    coins -= 1

    print(f"\n💰 Coins: {coins}")
    print(f"🎰 Spin #{spin_number + 1}")

    # Spin animation
    for i in range(5):
        reels = [
            random.choice(symbols),
            random.choice(symbols),
            random.choice(symbols)
        ]

        print(f"\r[{reels[0]}] [{reels[1]}] [{reels[2]}]", end="")
        time.sleep(0.2)

    # Final result
    reels = [
        random.choice(symbols),
        random.choice(symbols),
        random.choice(symbols)
    ]

    print(f"\r[{reels[0]}] [{reels[1]}] [{reels[2]}]")

    # Rewards
    if reels[0] == reels[1] == reels[2] == "7":
        print("💥 JACKPOT!!! +100 coins!")
        coins += 100

    elif reels[0] == reels[1] == reels[2]:
        print("🎉 THREE OF A KIND! +25 coins!")
        coins += 25

    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        print("✨ TWO MATCH! +5 coins!")
        coins += 5

    else:
        print("❌ No match!")

print("\n========================")
print("🎰 GAME OVER 🎰")
print(f"💰 Final coins: {coins}")
print("========================")

