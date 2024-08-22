from langchain_community.llms import Ollama

# Initialize the Ollama model
llm = Ollama(model="llama3")  # You can change this to any model you have in Ollama
print(llm.invoke("Tell me a joke"))
