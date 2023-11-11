from flask import Flask
import random
from random import choice

app = Flask(__name__)

@app.route("/")
def index():
    ssilka = "<a href='/randomFact'>Посмотреть случайный факт!</a>"
    return "<h1>Hello world</h1>" + ssilka

@app.route("/randomFact")
def randomFact():
    facts = ["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
             "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов."]
    fact = random.choice(facts)
    return f"<h1>{fact}</h1>"

@app.route("/money")
def money():
    mon = {1: "Орёл", 2: "Решка"}
    num = random.randint(1,2)
    cash = mon[num]
    return f"<h1>{cash}</h1>"

app.run(debug=True)

