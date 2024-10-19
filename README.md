# SROMP: Retail Operations and Demand Forecasting Platform

**SROMP** is a full-stack platform designed to manage retail operations, including **inventory management**, **sales transactions**, and **demand forecasting** using **Holt-Winters seasonal models**. It integrates a PostgreSQL database and provides a REST API for interaction with inventory and sales data.

## Features
- **Inventory Management:** Track product stock levels, update quantities, and monitor inventory health.
- **Sales Transactions:** Record and retrieve sales transactions.
- **Demand Forecasting:** Predict future stock requirements using historical sales data and Holt-Winters seasonal models.
- **Performance Optimization:** Optimized query performance using indexing and query caching, achieving a 20% reduction in response times.
- **REST API:** Provides an API for performing CRUD operations on inventory, sales, and demand forecasting.

## Tech Stack
- **Backend:** Python, Flask (for REST API)
- **Database:** PostgreSQL
- **Forecasting:** Holt-Winters Seasonal Model (statsmodels)
- **Optimization:** Query indexing and caching

## Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/SROMP.git
   cd SROMP
Tech Stack:
Backend: Python, Flask (REST API)
Database: PostgreSQL
Forecasting Model: Holt-Winters Seasonal Model (statsmodels library)
Optimization Techniques: Indexing, Query Caching
API Testing: Postman, PyTest
