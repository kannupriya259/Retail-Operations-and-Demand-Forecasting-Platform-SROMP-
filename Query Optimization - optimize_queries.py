def optimize_inventory_query():
    query = """
    CREATE INDEX IF NOT EXISTS idx_inventory_product_name ON inventory (product_name);
    """
    execute_query(query)
    print("Inventory query optimized with indexing.")

def optimize_sales_query():
    query = """
    CREATE INDEX IF NOT EXISTS idx_sales_product_id ON sales (product_id);
    """
    execute_query(query)
    print("Sales query optimized with indexing.")

if __name__ == "__main__":
    optimize_inventory_query()
    optimize_sales_query()
