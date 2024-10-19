from flask import Flask
from inventory import inventory_blueprint
from sales import sales_blueprint
from demand_forecasting import forecast_blueprint

app = Flask(__name__)

app.register_blueprint(inventory_blueprint, url_prefix='/inventory')
app.register_blueprint(sales_blueprint, url_prefix='/sales')
app.register_blueprint(forecast_blueprint, url_prefix='/forecast')

if __name__ == "__main__":
    app.run(debug=True)
