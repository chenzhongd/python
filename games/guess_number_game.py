import random

def guess_number_game():
    print("欢迎来到猜数字游戏！")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("请输入你猜的数字（1到100之间）："))
            attempts += 1

            if guess < 1 or guess > 100:
                print("请确保你的数字在1到100之间。")
            elif guess < number_to_guess:
                print("太小了！再试一次。")
            elif guess > number_to_guess:
                print("太大了！再试一次。")
            else:
                print(f"恭喜你，猜对了！你一共猜了{attempts}次。")
                break
        except ValueError:
            print("请输入一个有效的数字。")

if __name__ == "__main__":
    guess_number_game()