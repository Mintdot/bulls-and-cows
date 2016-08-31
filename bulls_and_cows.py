import random
from tkinter import *
4
def bulls_and_cows(event):

    global count
    strike=0
    ball=0

    player = input.get()
    input.delete(0, END)

    if len(player) > 3 or 0 < len(player) < 3:
        listbox.insert(END, "숫자를 총 3개 입력해주세요.")
        return

    if player[0] == player[1] or player[0] == player[2] or player[1] == player[2]:
        listbox.insert(END, "중복되지 않은 숫자를 입력해주세요.")
        return

    count += 1

    for i in range(0, 3):
        if int(player[i]) == computer[i]:
            strike+=1
        elif int(player[i]) != computer[i] and int(player[i]) in computer:
            ball+=1

    gameMsg = "%d회차) 컴퓨터[%d%d%d] 플레이어[%s] Strike[%d] Ball[%d]" % (count, computer[0], computer[1], computer[2], player, strike, ball)
    listbox.insert(END, gameMsg)

    if strike == 3:
        listbox.insert(END, "%d번 만에 우승하셨습니다!" % count)
        input.config(state=DISABLED)
        count=0
        return

    if count == 9:
        listbox.insert(END, "패배하셨습니다..")
        input.config(state=DISABLED)
        count=0
        return

def rnd():
    computer = []
    while len(computer) != 3:
        rnd = random.randint(0, 9)
        if rnd not in computer:
            computer.append(rnd)

    return computer

def restart():
    global computer, count
    input.config(state=NORMAL)
    listbox.delete(0, END)
    listbox.insert(END, "0~9사이의 서로 다른 숫자 3개를 입력해주세요.")
    computer = rnd()

game = Tk()
game.title("숫자 야구 게임")
#game.geometry("450x200+450+100")

play = Frame(game)
explanation = Label(play, text="숫자 야구 게임")
input = Entry(play, width=3)
restart = Button(play, text="재시작", command=restart)
scroll = Scrollbar(game, orient=VERTICAL)
listbox = Listbox(game, width=40, height=20, bg="white", yscrollcommand=scroll.set)

play.pack()
explanation.pack(side=LEFT)
input.pack(side=LEFT)
restart.pack(padx=5)
scroll.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH)
scroll.config(command=listbox.yview)

count=0
computer = rnd()

listbox.insert(END, "0~9사이의 서로 다른 숫자 3개를 입력해주세요.")
listbox.insert(END, "주어진 게임 기회는 9번입니다.")

input.bind('<Key-Return>', bulls_and_cows)

game.mainloop()

# c_sum = [0, 0, 0]
# p_sum = [0, 0, 0]
# count = 0
#
# print("숫자 야구 게임에 오신 것을 환영합니다.")
# print("도전 기회는 총 9번 입니다.")
#
# c_sum[0] = random.randint(0, 9)
# c_sum[1] = random.randint(0, 9)
# c_sum[2] = random.randint(0, 9)
#
# while not (c_sum[0] != c_sum[1] and c_sum[0] != c_sum[2] and c_sum[1] != c_sum[2]) :
#     if c_sum[0] == c_sum[1] :
#         c_sum[1] = random.randint(0, 9)
#     if c_sum[0] == c_sum[2] or c_sum[1] == c_sum[2] :
#         c_sum[2] = random.randint(0, 9)
#
# # print(c_sum[0], c_sum[1], c_sum[2])
#
# while count < 9 :
#     print("0~9 사이의 서로 다른 숫자를 세 번 입력해주세요.")
#
#     p_sum[0] = int(input())
#     p_sum[1] = int(input())
#     p_sum[2] = int(input())
#
#     while True :
#
#         if p_sum[0] < 0 or p_sum[0] > 9 :
#             print("첫번 째 수를 0~9 사이의 다른 수로 수정해주세요,")
#             p_sum[0] = int(input())
#         elif p_sum[0] == p_sum[1] or p_sum[1] < 0 or p_sum[1] > 9 :
#             print("두 번째 수를", p_sum[0], "(을)를 제외한 0~9 사이의 다른 수로 수정해주세요.")
#             p_sum[1] = int(input())
#         elif p_sum[0] == p_sum[2] or p_sum[1] == p_sum[2] or p_sum[2] < 0 or p_sum[2] > 9 :
#             print("세 번째 수를", p_sum[0], "와", p_sum[1], "(을)를 제외한 0~9 사이의 다른 수로 수정해주세요.")
#             p_sum[2] = int(input())
#         else :
#             break
#
#     print(p_sum[0], p_sum[1], p_sum[2])
#
#     i = 0
#     j = 0
#     strike = 0
#     ball = 0
#     out = 0
#
#     while i < 3 :
#         while j < 3 :
#             if c_sum[i] == p_sum[j] and i == j :
#                 strike += 1
#                 break
#             elif c_sum[i] == p_sum[j] and i != j :
#                 ball += 1
#             j += 1
#         i += 1
#         j = 0
#
#     out = 3 - (strike + ball)
#
#     print(strike, "스트라이크", ball, "볼", out, "아웃")
#     count += 1
#     if strike == 3 :
#         print("게임에서 승리하셨습니다!")
#         break
#     elif count==9 :
#         print("게임에서 패배하셨습니다..")
#         break
#     print("남은 기회는", (9 - count), "번 입니다")