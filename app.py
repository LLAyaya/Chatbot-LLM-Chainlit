import chainlit as cl
from src.llm import ask_order, messages

@cl.on_chat_start
async def main():
    await cl.Message(content="Hello, Welcome to our online store.").send()        
    
@cl.on_message
async def handle_message(message: cl.Message):

    messages.append({"role": "user", "content": message.content})

    if message.content.strip().lower() in ['bye', 'goodbye', 'exit']:
        res = await cl.AskActionMessage(
            content="Are you satisfied with our Bot help?",
            actions=[
                cl.Action(name="YES", value="YES", label="YES"),
                cl.Action(name="NO", value="NO", label="NO")  
            ]
        )
        if res:
            await cl.Message(content=f"Thank you for your feedback: {res['value']}").send()
        return 

    response = generate_response(messages)

    messages.append({"role": "assistant", "content": response})

    await send_response(response)


def generate_response(messages):
    return ask_order(messages)


async def send_response(response):
    await cl.Message(content=response).send()

async def update_sidebar():
    """
    Update the sidebar to display all previous conversation history.
    """
    sidebar_content = ""
    for message in messages:
        role = "User" if message["role"] == "user" else "Assistant"
        sidebar_content += f"**{role}:** {message['content']}\n\n"

    # Render conversation history in the sidebar
    await cl.Sidebar(content=sidebar_content).send()