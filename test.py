from menakabot import MenakaBot

gameState = {
    "rounds": [
        {"p1": "R", "p2": "D"},
        {"p1": "W", "p2": "S"},
    ]
}

bot = MenakaBot()
print(bot.make_move(gameState))