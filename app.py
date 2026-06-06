from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import streamlit as st
import os

st.set_page_config(page_title="🤖 Multi-Agent Assistant", layout="wide")
st.title("🤖 Multi-Agent AI Assistant")
st.markdown("Powered by CrewAI — multiple specialized agents working together")

openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
task_input = st.text_area("What do you want the agents to work on?", height=100)

if st.button("🚀 Run Agents") and openai_key and task_input:
    os.environ["OPENAI_API_KEY"] = openai_key
    llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    researcher = Agent(
        role="Senior Research Analyst",
        goal="Find accurate, comprehensive information on the given topic",
        backstory="Expert researcher with 10 years of experience in data gathering and analysis",
        llm=llm, verbose=True
    )
    writer = Agent(
        role="Content Writer",
        goal="Transform research into clear, structured, engaging content",
        backstory="Professional writer specializing in technical and business content",
        llm=llm, verbose=True
    )

    research_task = Task(
        description=f"Research the following topic thoroughly: {task_input}",
        agent=researcher,
        expected_output="A comprehensive research report with key findings, data, and insights"
    )
    writing_task = Task(
        description="Transform the research into a well-structured, readable document",
        agent=writer,
        expected_output="A polished, professional document ready for presentation"
    )

    crew = Crew(agents=[researcher, writer], tasks=[research_task, writing_task], process=Process.sequential)

    with st.spinner("Agents working... this may take a minute..."):
        result = crew.kickoff()

    st.markdown("### 📋 Result")
    st.write(result)
