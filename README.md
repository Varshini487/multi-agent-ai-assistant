# 🤖 Multi-Agent AI Assistant

A **Multi-Agent AI system** where specialized agents collaborate to solve complex tasks.

## 🧩 Architecture
The system uses an **Orchestrator Pattern** — one central agent delegates tasks to specialized sub-agents.

## 🤖 Agents
| Agent | Role |
|-------|------|
| 🎯 Orchestrator | Breaks tasks, delegates to agents |
| 🔍 Research Agent | Web search and information gathering |
| 💻 Code Agent | Writes and executes Python code |
| 📊 Data Agent | Analyzes data, generates charts |
| ✍️ Writer Agent | Drafts documents, emails, summaries |

## 🛠️ Tech Stack
- **CrewAI / LangChain Agents** – agent orchestration
- **OpenAI GPT-4** – language model
- **Tavily** – web search tool
- **Python + FastAPI** – backend
- **Streamlit** – user interface

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/multi-agent-ai-assistant
cd multi-agent-ai-assistant
pip install -r requirements.txt
python app.py
```

## 📁 Project Structure
```
multi-agent-ai-assistant/
├── agents/
│   ├── orchestrator.py
│   ├── research_agent.py
│   ├── code_agent.py
│   ├── writer_agent.py
│   └── data_agent.py
├── tools/
│   ├── web_search.py
│   └── code_executor.py
├── app.py
├── requirements.txt
└── README.md
```

## 💡 Use Cases
- Complex multi-step research
- Automated report generation
- Data analysis pipelines
- Content creation workflows
