from turtle import *

words = [
    ("저(나)", "I (honorific"),
    (("중국 "), ("China")),
    (("~씨 "), ("Mr. / Mrs./Miss")),
    (("한국 "), ("Korea")),
    (("사람 "), ("Person")),
    (("학생 "), ("student")),
    (("캐나다 "), ("Canada ")),
    (("이란 "), ("Iran")),
    (("필리핀 "), ("Philippines ")),
    (("호주 "), ("Australia")),
    (("이름이 뭐예요? "), ("What is your name? ")),
    (("홍콩 "), ("Hong Kong")),
    (("반갑다 "), ("To be glad (to meet) / Mostly used 반갑습니다")),
    (("대학생 "), ("College student ")),
    (("독일 "), ("Germany")),
    (("미국 "), ("U.S.A. ")),
    (("프랑스 "), ("France")),
    (("일본"), ("Japan")),
    (("베트남"), ("Vietnam")),
    (("러시아"), ("Russia")),
    (("태국"), ("Thailand")),
    (("고등학생"), ("High school student ")),
    (("영국"), ("U.K.")),
    (('인도'), ('India')),
    (("만나서 반 갑습니다"), ("Nice to meet you")),
    (('의사'), ('doctor')),
    (('학년'), ('School year')),
    (("중학생 "), ("Middle school student")),
    (("일본어 "), ("Japanese language")),
    (("일"), ("1")),
    (("이 "), ("2")),
    (("여자 "), ("woman")),
    (("삼 "), ("3")),
    (("사 "), ("4")),
    (("한국어 "), ("Korean language ")),
    (("선생님 "), ("teacher")),
    (("우리 "), ("Uli")),
    (("회사 원"), ("Company employee")),
    (("채소 "), ("Vegetable ")),
    (("오렌지 "), ("orange")),
    (("사과 "), ("apple")),
    (("오이"), ("cucumber")),
    (("토마토 "), ("tomato")),
    (("누나"), ("older sister (of male)")),
    (("동생 "), ("younger subling")),
    (("아버지 "), ("father")),
    (("말레이시아 "), ("Malaysia")),
    (("어머니 "), ("mother")),
]
"""
- create dictionary with words
- create cards object
    - include audios to cards
    -include the uncover button that changes the color of the result from bg to black or red
"""
from random import randint
from tkinter import *

turt = Turtle()
screen = Screen()
screen.setup(width=600, height=400)
penup()
hideturtle()
turt.hideturtle()
turt.penup()
turt.right(90)
turt.forward(50)


def answer():
    turt.write(words[random_index][1], False, 'left',('arial', 18, 'normal'))

def word():
    clear()
    turt.clear()
    global random_index
    random_index = randint(0, len(words) - 1)
    write(words[random_index][0], False, 'center', ('arial', 20, 'normal'))



canvas = screen.getcanvas()
new_word = Button(canvas.master, text="new_word", command=word)
show_answer = Button(canvas.master, text="Show_answer", command=answer)

new_word.pack()
new_word.place(x=300, y=50)
show_answer.pack()
show_answer.place(x=300, y=100)  # place the button anywhere on the screen
screen.exitonclick()


