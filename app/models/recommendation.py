
import pandas as pd

# Function to recommend offers based on user behavior
def recommend_offers(user_id: int):
    # Load the cleaned orders data
    orders = pd.read_csv('data/cleaned_orders.csv')
    products = pd.read_csv('data/products.csv')

    # Filter orders for the given user
    user_orders = orders[orders['user_id'] == user_id]

    if user_orders.empty:
        # If the user has no orders, return a default recommendation
        return [101, 202, 303]  # Default offer IDs as placeholders

    # Get product IDs that the user has ordered
    user_product_ids = user_orders['product_id'].unique()

    # Find products from the same category or related categories
    user_products = products[products['product_id'].isin(user_product_ids)]
    user_product_category = user_products['aisle_id'].mode()[0]

    # Recommend new offers in the same or similar category
    recommendations = products[products['aisle_id'] == user_product_category]['product_id'].sample(5).tolist()

    return recommendations

# Function to visualize user purchases
def visualize_user_purchases(user_id: int):
    # Load the data
    orders = pd.read_csv('data/cleaned_orders.csv')
    products = pd.read_csv('data/products.csv')

    # Filter orders for the given user
    user_orders = orders[orders['user_id'] == user_id]

    if user_orders.empty:
        return None  # No visualization if there are no purchases

    # Merge with product data to get product names
    user_orders = user_orders.merge(products, on='product_id', how='left')

    # Count how many times each product is purchased
    product_counts = user_orders['product_name'].value_counts()

    # Generate a bar chart using Plotly
    import plotly.graph_objs as go

    fig = go.Figure([go.Bar(x=product_counts.index, y=product_counts.values)])
    fig.update_layout(
        title='User Purchase History',
        xaxis_title='Product Name',
        yaxis_title='Number of Purchases',
        xaxis_tickangle=-45
    )

    # Save the plot as an HTML file and return the file path
    plot_path = f'templates/plots/user_{user_id}_purchase_history.html'
    fig.write_html(plot_path)
    return plot_path
