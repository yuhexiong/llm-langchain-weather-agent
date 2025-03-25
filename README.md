# LLM LangChain Weather Agent

Using LangChain to integrate the Ollama model (I am using Gemma3) to implement an AI Agent's function calling, allowing the model to decide whether to call an external API to fetch weather data for its response.  

## Overview

- Language: Python v3.12
- Module: langchain v0.3.20, langchain-core v0.3.41, langchain-ollama v0.2.3


## Env

```
OLLAMA_URL='localhost:11434'
OLLAMA_MODEL='gemma3:27b'
```

## Run

### Install Module

```bash
pip install langchain==0.3.20 langchain-core==0.3.41 langchain-ollama==0.2.3 python-dotenv==1.0.1
```

### Run
```bash
python agent.py
```


## Demo
![Demo](demo.png)