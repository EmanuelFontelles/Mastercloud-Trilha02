from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/car_list')
def car_list():
    cars = [
        {'name': 'Carro A', 'price': 20000},
        {'name': 'Carro B', 'price': 30000},
    ]
    return render_template('car_list.html', cars=cars)

@app.route('/car_details/<string:car_name>')
def car_details(car_name):
    car = {'name': car_name, 'price': 20000, 'features': ['Ar-condicionado', 'Direção hidráulica']}
    return render_template('car_details.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)
