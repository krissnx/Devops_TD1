from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, \
    QSizePolicy, QComboBox
import unittest


def create_GUI(width, height):
    app = QApplication()

    window = QWidget()
    window.setWindowTitle("Augmentation d'image")

    window.setFixedWidth(width)
    window.setFixedHeight(height)

    image_label = QLabel("Image path: ")
    text = QLineEdit()
    text.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    select_button = QPushButton("Select")
    select_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    transformation_label = QLabel("select a transformation ")
    transformation_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    combo = QComboBox()
    combo.addItems(["blur", "resize", "rotate", "grey", "slide", "greyerosion", "greyopening", "filt"])
    submit_button = QPushButton("Apply")
    submit_button \
        .setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    h_layout = QHBoxLayout()
    h_layout.addWidget(image_label, 1)
    h_layout.addWidget(text, 2)
    h_layout.addWidget(select_button, 1)

    v_layout = QVBoxLayout()
    v_layout.addLayout(h_layout)
    v_layout.addWidget(transformation_label)
    v_layout.addWidget(combo)
    v_layout.addWidget(submit_button)

    window.setLayout(v_layout)
    window.show()
    app.exec()


def calculate(a, b, op):
    # renforcement de code
    res = 0
    if op not in "/*+-%**":
        print("opération non valide")
    else:
        if op == "+":
            res = a+b
            print(f" {a} {op} {b} = {res}")
        elif op == "-":
            res = a-b
            print(f" {a} {op} {b} = {res}")
        elif op == "*":
            res = a*b
            print(f" {a} {op} {b} = {res}")
        elif op == "/":
            # renforcement de code
            if b == 0:
                print("Division par zéro")
            else:
                res = a/b
                print(f" {a} {op} {b} = {res}")
        elif op == "%":
            res = a%b
            print(f" {a} {op} {b} = {res}")
        elif op == "**":
            res = a ** b
            print(f" {a} {op} {b} = {res}")
    return res


# Les tests unitaires
def test_fct1(width, height):
    assert(type(width) == int)
    assert(type(width) != 0)
    assert(type(height) == int)
    assert(type(height) != 0)


test_fct1(0,0)
test_fct1("400", "300")
test_fct1("400", 0)
test_fct1(500,500)


def test_fct2(a, b, op):
    if op == "/":
        assert(b != 0)
    assert(op in "+*/-%**")


test_fct2(5,0, "/")
test_fct2(5,5, "p")
test_fct2(0, 0, "+")



