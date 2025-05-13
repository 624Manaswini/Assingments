from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage
import os

os.environ["MISTRAL_API_KEY"] = "dtiSHpRUJVjcWhtrLRIvPDltTWMQHilC"

llm = ChatMistralAI(model="open-mistral-nemo", temperature=0)

chat_histories = {}

def get_response(user_input, session_id="default"):
    
    history = chat_histories.get(session_id, [])
    history.append(HumanMessage(content=user_input))
    response = llm.invoke(history)
    history.append(AIMessage(content=response.content))
    chat_histories[session_id] = history

    return response.content, history
