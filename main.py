import os
from dotenv import load_dotenv 
from google.adk.runners import InMemoryRunner
from src.agents import create_task_planner_agent


import asyncio

async def main():
    print("Initializing Travel Planner Agent...")
    try:
        # Load environment variables
        load_dotenv()
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        if not GOOGLE_API_KEY:
             raise ValueError("GOOGLE_API_KEY not found in environment variables.")
             
        os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
        print("[Success] Gemini API key setup complete.")

        # Initialize the agent hierarchy
        root_agent, session_service = create_task_planner_agent()
        runner = InMemoryRunner(agent=root_agent)

        while True:
            userinput = input("\nEnter your travel goal (or type 'quit' to exit): ")
            if userinput.lower() in ['quit', 'exit', 'q']:
                print("Exiting Travel Planner Agent. Goodbye!")
                break

            print("\n--- Starting Task ---")
            response = await runner.run_debug(userinput, session_id='session_service')
            print("\n--- Task Completed ---")
            print(response)
            
            # Explicitly ask if they want to continue (though the loop does this implicitly, 
            # the prompt asked for a specific interaction after the graph/task is done)
            cont = input("\nDo you want to plan another trip? (y/n): ")
            if cont.lower() not in ['y', 'yes']:
                print("Exiting Travel Planner Agent. Goodbye!")
                break

        
    except Exception as e:

        print(f"[Auth Error]: Please make sure you have added 'GOOGLE_API_KEY' to your Kaggle secrets. Details: {e}")

if __name__ == "__main__":
    asyncio.run(main())
