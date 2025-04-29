from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

generation_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate funny twitter posts about RCB."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Reflect on the following: {messages}"),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm