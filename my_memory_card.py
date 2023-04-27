from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

app = QApplication([])


class Question():
    def __init__(
    self, question, right_answer, wrong1, wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


window = QWidget()
window.setWindowTitle('мемари кард')
window.resize(400, 200)


RadioGroupBox = QGroupBox('Варианты ответов:')

b1=QRadioButton('Энцы')
b2=QRadioButton('Смурфы')
b3=QRadioButton('Чулымцы')
b4=QRadioButton('Алеуты')


title=QLabel('Какой национальности не существует?')
button=QPushButton('Ответить')

l_ans_1=QHBoxLayout()
l_ans_2=QVBoxLayout()
l_ans_3=QVBoxLayout()

ans=QGroupBox('Результаты теста')
ans_l = QVBoxLayout()
Lb_Result=QLabel('Правильно/Неправильно')
ans_text1=QLabel('Правильный ответ')
ans_l.addWidget(Lb_Result)
ans_l.addWidget(ans_text1)
ans.setLayout(ans_l)



l_ans_1.addLayout(l_ans_2)
l_ans_1.addLayout(l_ans_3)
l_ans_2.addWidget(b1)
l_ans_2.addWidget(b2)
l_ans_3.addWidget(b3)
l_ans_3.addWidget(b4)
l_ans_1.addLayout(l_ans_2)
l_ans_1.addLayout(l_ans_3)

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    title.setText(q.question)
 
RadioGroupBox.setLayout(l_ans_1)

def show_res():
    RadioGroupBox.hide()
    ans.show()
    button.setText('Следующий вопрос')
    

def show_q():
    RadioGroupBox.show()
    ans.hide()
    title.setText('Самый сложный вопрос в мире')
    button.setText('Ответить')
    RadioGroup.setExclusive(False)    
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [b1,b2,b3,b4]



q1 = Question('как тебя зовут','крутой парен','никита','кирилл','майонезii')
q2 = Question('сколько тебе лет', 'столько', '12','13','14')
q3 = Question('где ты живешь','дома', 'на улице мира', 'в школе', 'где мой майонез')
q5 = Question('сколько будет корень из 4х?','2','1','0','-1')


que_list = [q1,q2,q3,q5]

ask(q1)

def show_correct(res):
    ans_text1.setText(res)
    show_res()

def test():
    if button.text() == "Ответить":
        show_res()
    else:
        show_q() 
 
"""click_OK"""

def check_answer():
    if answers[0].isChecked():
        show_correct('верно')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('неверно')

button.clicked.connect(click_OK)

RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

main_lay = QVBoxLayout()
main_lay.addWidget(title)
main_lay.addWidget(RadioGroupBox)

main_lay.addWidget(ans)
main_lay.addWidget(button)

ans.hide()



window.setLayout(main_lay)
window.show()
app.exec()