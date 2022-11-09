def python_snakes(level: int):
    print("🐍")
    for n in range(0, level-1):
        a = "🐍 "
        for m in range(0, n):
            a += "🐍🐍 "
        a += "🐍"
        print(a)


python_snakes(7)
