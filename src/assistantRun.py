from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?",
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id="asst_i6rVjdFVrgE1niza5sjwu5Sd",
    instructions="Please address the user as Jane Doe. The user has a premium account.",
)

print(run.status)
