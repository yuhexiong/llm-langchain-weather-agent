from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType
import os
from langchain_ollama import ChatOllama

from dotenv import load_dotenv

from util import get_weather



# 讀取 .env 變數
load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

if not OLLAMA_URL:
    raise Exception("未在 .env 檔案中找到 OLLAMA_URL")
if not OLLAMA_MODEL:
    raise Exception("未在 .env 檔案中找到 OLLAMA_MODEL")

# 初始化 LLM
llm = ChatOllama(model=OLLAMA_MODEL, base_url=OLLAMA_URL)

# 定義工具
@tool
def fetch_weather(city: str) -> str:
    """
    獲取指定城市的天氣狀況
    """

    return get_weather(city)


# 設定 Agent
agent = initialize_agent(
    tools=[fetch_weather],  # 註冊天氣查詢工具
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # 讓 LLM 自動決定是否呼叫函式
    verbose=True
)

# 測試輸入
response = agent.invoke("台北今天的天氣如何？")
print(response['output'])
