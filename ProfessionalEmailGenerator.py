from langchain.prompts import PromptTemplate
#from langchain.llms import OpenAI
from langchain_openai import OpenAI

# Initialize the OpenAI language model with an API key and set the temperature parameter
# Temperature 0.0 means the model's outputs will be more deterministic
llm = OpenAI(openai_api_key='todo add your own key', temperature=0.0)

prompt = PromptTemplate(
    # Define the variables that will be replaced in the template
    input_variables=['content', 'clientName', 'senderName'], 
    # Provide the prompt, including placeholders for variables.
    template="""
    You are an AI assistant that is optimized for writing concise, friendly, and professional emails. 
    
    Write an email to a client with the name {client_name} that contains the following, optimized content: {content}
    
    The email signature should contain the name of the sender: {sender_name}
    """
)

# Prompt the user to input the email content, customer's name, and sender's name
content = input('Email content: ')
clientName = input('Client Name: ')
senderName = input('Sender Name: ')

# Format the prompt with the user's inputs and generate the response using the language model
response = llm(prompt.format(content=content, client_name=clientName, sender_name=senderName))

# Print the generated email response
print(response)