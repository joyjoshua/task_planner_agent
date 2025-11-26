from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search
from src.tools.visualization import plot_expenses
def create_task_planner_agent():
    """
    Creates and configures the Task Planner agent hierarchy.
    
    Returns:
        Agent: The root agent (SequentialAgent) ready to be run.
    """
    # 1. Destination Scout Agent
    destination_agent = Agent(
        name="DestinationScoutAgent",
        model="gemini-2.5-flash-lite",
        instruction="""You are an expert Travel Scout. Your goal is to find the best travel destinations that fit the user's specific budget and duration constraints.
        
        Step 1: Analyze the user's request to understand their budget, number of days, and any specific preferences (e.g., beach, mountains, city).
        Step 2: Use the `google_search` tool to find current travel deals and estimated costs for various destinations that fit the criteria.
        Step 3: Select the top 3-5 destinations.
        
        Output Format:
        Provide a list of destinations with a brief description and a rough total cost estimate.
        
        Example Output:
        [
            {"name": "Bali, Indonesia", "description": "Tropical beaches and temples", "estimated_total_cost": 1200},
            {"name": "Tokyo, Japan", "description": "Modern city meets tradition", "estimated_total_cost": 1500}
        ]
        """,
        tools=[google_search],
        output_key="destinations"     
    )

    # 2. Expense Tracker Agent
    expense_agent = Agent(
        name="ExpenseTrackerAgent",
        model="gemini-2.5-flash-lite",
        instruction="""You are a meticulous Travel Expense Planner. Your input will be a list of potential destinations provided by the DestinationScoutAgent.
        
        Your Goal: Create a detailed expense breakdown for EACH destination provided.
        
        For each destination, estimate costs for:
        1. Round-trip Flights/Transportation (from a major hub if not specified)
        2. Accommodation (Hotel/Airbnb for the duration)
        3. Food & Dining (Daily allowance)
        4. Activities & Sightseeing
        5. Miscellaneous (Visa, Local transport, etc.)
        
        Output Format:
        Return a structured JSON-like list containing the breakdown.
        
        Example Output:
        [
            {
                "location": "Bali, Indonesia",
                "breakdown": {
                    "flights": 500,
                    "accommodation": 400,
                    "food": 200,
                    "activities": 100
                },
                "total_price": 1200
            },
            ...
        ]
        """,
        output_key="expense_breakdown",
    )   

    # 3. Visualization Agent
    visualization_agent = Agent(
        name="VisualizationAgent",
        model="gemini-2.5-flash-lite",
        instruction="""You are a Data Visualization Expert and Summarizer. 
        Input: Detailed expense breakdowns from the ExpenseTrackerAgent.
        
        Your Tasks:
        1. Summarize: Provide a brief text summary comparing the options, highlighting the best value or most luxurious option.
        2. Visualize: Use the `plot_expenses` tool to generate a bar chart comparing the TOTAL costs of the destinations.
        
        Extract the destination names and their corresponding total prices from the input and pass them to the tool.
        """,
        tools=[plot_expenses],
        output_key="final_output",
    )

    # 4. Root Agent (Sequential)
    root_agent = SequentialAgent(
        name="RootAgent",
        description="A travel planning coordinator that finds destinations, calculates expenses, and visualizes the data.",
        sub_agents=[destination_agent, expense_agent, visualization_agent],
    )
    
    return root_agent
