import os
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel, DuckDuckGoSearchTool

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")

model = OpenAIServerModel(
    model_id="gpt-4o-mini",
    api_base="https://api.openai.com/v1",
    api_key=api_key,
)

search_tool = DuckDuckGoSearchTool()

agent = CodeAgent(
    tools=[search_tool],
    model=model,
    max_steps=5,
)

question = input("Ask your AI agent: ")
answer = agent.run(question)

print("\nAgent Answer:")
print(answer)
