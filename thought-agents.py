from langgraph.graph import MessagesState
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, RemoveMessage
from typing import List, Annotated
import operator
import setup_env
from setup_prompts import load_prompts


# the idea is to try and make the agent as human as humanly possible XDDDD
# https://open.spotify.com/track/2GaqdTO88MeyaQ90jMGRYl?si=aefcce12f7d64fa3
# https://open.spotify.com/track/4Q4CuXrwdd3pwwK346cfwY?si=7aae287ac78f41aa


llm = ChatOpenAI(model="o3-mini")
prompts = load_prompts()


class DialogueState(MessagesState):
    current_session_topics: Annotated[List[str], operator.add]
    summary: str
    emotion_candidates: List[str]
    user_name: str


def summarize_context(state: DialogueState, n_sum=-5):
    """
    state["messages"] summarizer node to not go broke on tokens
    :param state: state
    :param n_sum: how many messages we want to summarize
    :return: {"messages": [msg]}
    """
    summary = state.get('summary')
    messages = state.get('messages')
    if summary:
        prompt = prompts["summary"].format(messages=messages)
        new_summary = llm.invoke(prompt)
        delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:n_sum]]
        return {"summary": new_summary, "messages": delete_messages}
    else:
        prompt = prompts["not_summary"].format(messages=messages)
        new_summary = llm.invoke(prompt)
        delete_messages = [RemoveMessage(id=m.id) for m in state["messages"][:n_sum]]
        return {"summary": new_summary, "messages": delete_messages}




