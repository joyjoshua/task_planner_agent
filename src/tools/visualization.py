import matplotlib.pyplot as plt

def plot_expenses(destinations: list[str], costs: list[int]) -> str:
    """
    Generates and displays a bar chart comparing travel expenses.
    
    Args:
        destinations: List of destination names.
        costs: List of total costs corresponding to the destinations.
        
    Returns:
        str: A message indicating the chart has been displayed.
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(destinations, costs, color='skyblue')
        plt.xlabel('Destinations')
        plt.ylabel('Total Cost')
        plt.title('Travel Destination Cost Comparison')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return "Bar chart displayed successfully."
    except Exception as e:
        return f"Error displaying chart: {e}"
