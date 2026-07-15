import os, dotenv
import asyncio
dotenv.load_dotenv('.env')

from app.graph.workflow import graph

async def main():
    print("Starting graph...")
    async for event in graph.astream_events({'question': 'hello', 'retries': 0}, config={'configurable': {'thread_id': '123'}}, version='v2'):
        print(f"EVENT: {event['event']} NODE: {event.get('metadata', {}).get('langgraph_node')}")
        
    print("Done")

if __name__ == "__main__":
    asyncio.run(main())
