from langchain_ollama import ChatOllama
llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0)
llm_json_mode = ChatOllama(model="deepseek-r1:1.5b", temperature=0, format="json")

# msg = llm.invoke("What is the capital of France?")
# msg.content
# print(msg.content)

import json
p = """Your goal is to generated targeted web search query.

The query will gather information related to a specific topic.

Topic: Cats

Return your query as a JSON object:

{{
    "query": "string",
    "aspect": "string",
    "rationale": "string"
}}
"""
msg = llm_json_mode.invoke(p)
query = json.loads(msg.content)
print(query)