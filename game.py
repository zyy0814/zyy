<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)  # 生成一个1到100之间的随机数
    attempts = 0

    print("猜数字游戏开始！我已经想好了一个1到100之间的数字。")

    while True:
        attempts += 1
        user_input = input("请输入你猜的数字：")
        
        try:
            user_guess = int(user_input)
        except ValueError:
            print("请输入一个有效的整数。")
            continue

        if user_guess < number_to_guess:
            print("太小了，再试试看。")
        elif user_guess > number_to_guess:
            print("太大了，再试试看。")
        else:
            print(f"恭喜你！你猜对了数字，它就是 {number_to_guess}。")
            print(f"你总共猜了 {attempts} 次。")
            break

if __name__ == "__main__":
    guess_number_game()
</body>
</html>