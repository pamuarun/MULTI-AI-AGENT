from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):

    llm = ChatGroq(model=llm_id)

    tools = [TavilySearch(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # 🔥 FIX: explicit system + human message
    state = {
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ]
    }

    response = agent.invoke(state)

    messages = response.get("messages", [])

    ai_messages = [
        m.content for m in messages if isinstance(m, AIMessage)
    ]

    return ai_messages[-1] if ai_messages else "No response generated"