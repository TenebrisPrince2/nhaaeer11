from flask import Flask, render_template, abort

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# Страница дебетовых карт
@app.route('/debit-cards')
def debit_cards():
    cards = [
        {
            'id': 1,
            'title': 'Дебетовая Кэшбэк',
            'bankName': 'Альфа-Банк',
            'imageUrl': '/static/images/cards/debit-card-1.png',
            'features': [
                'До 5% кэшбэка на покупки',
                'Бесплатное обслуживание',
                'Снятие наличных без комиссии'
            ],
            'buttonText': 'Оформить карту'
        },
        # ... другие карточки
    ]
    return render_template('debit_cards.html', cards=cards)

# Страница кредитных карт
@app.route('/credit-cards')
def credit_cards():
    cards = [
        {
            'id': 1,
            'title': 'Кэшбэк Премиум',
            'bankName': 'Альфа-Банк',
            'imageUrl': '/static/images/cards/credit-card-1.png',
            'features': [
                'До 10% кэшбэка в избранных категориях',
                'Льготный период до 100 дней',
                'Доступ в бизнес-залы аэропортов'
            ],
            'buttonText': 'Оформить карту'
        },
        # ... другие карточки
    ]
    return render_template('credit_cards.html', cards=cards)

# Страница займов
@app.route('/loans')
def loans():
    loans = [
        {
            'id': 1,
            'title': 'Потребительский кредит',
            'bankName': 'Альфа-Банк',
            'imageUrl': '/static/images/cards/loan-1.png',
            'features': [
                'Ставка от 6,5% годовых',
                'Сумма до 5 000 000 ₽',
                'Срок до 7 лет'
            ],
            'buttonText': 'Получить кредит'
        },
        # ... другие займы
    ]
    return render_template('loans.html', loans=loans)

# Страница РКО
@app.route('/rko')
def rko():
    rko_options = [
        {
            'id': 1,
            'title': 'Базовый РКО',
            'bankName': 'Альфа-Банк',
            'imageUrl': '/static/images/cards/rko-1.png',
            'features': [
                'Открытие счета бесплатно',
                '30 операций в месяц включено',
                'Интернет-банк и мобильное приложение'
            ],
            'buttonText': 'Открыть счет'
        },
        # ... другие РКО
    ]
    return render_template('rko.html', rko_options=rko_options)

# Обработка 404 ошибки
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)