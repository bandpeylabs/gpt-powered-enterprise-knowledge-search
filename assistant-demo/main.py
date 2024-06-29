import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI


token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")

client = AzureOpenAI(
    azure_ad_token_provider=token_provider,
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_version="2024-05-01-preview",
)

# Create an assistant
assistant = client.beta.assistants.create(
    name="sarcastic-chat",
    instructions="You are a useless AI assistant. No matter what was the question, answer sarcastically and make fun of user!",
    # tools=[{"type": "code_interpreter"}],
    # You must replace this value with the deployment name for your model.
    model="depl-assistant-dev"
)

# Create a thread
thread = client.beta.threads.create()

# Add a user question to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)


# Run the thread and poll for the result
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    # Way to overwrite system instructions
    # instructions="Please address the user as Roozbeh Bandpey. The user has a premium account.",
)

print("Run completed with status: " + run.status)

if run.status == "completed":
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    print(messages.to_json(indent=2))
