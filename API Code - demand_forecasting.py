from flask import Blueprint, jsonify
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from utils import execute_query

forecast_blueprint = Blueprint('forecast', __name__)

@forecast_blueprint.route("/", methods=["GET"])
def forecast_demand():
    sales_query = "SELECT sale_date, quantity_sold FROM sales"
    sales_data = execute_query(sales_query)
    
    df = pd.DataFrame(sales_data)
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df.set_index('sale_date', inplace=True)

    # Holt-Winters model for demand forecasting
    model = ExponentialSmoothing(df['quantity_sold'], seasonal='add', seasonal_periods=12).fit()
    forecast = model.forecast(12)
    
    return jsonify(forecast.tolist())
