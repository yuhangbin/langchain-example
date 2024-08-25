# langchain-example

## key component:
- Model (GPT,Claude,Gemini and so on)
- prompt (natural language programming)
- parser (reformat the output result for better read which for next llm input or human)
- Memory (instruction context for llm better answer)
- Chain (support n input and n output, setup data pipeline to handle complex tasks)
- Q&A (get answer from user input documents, it will use embedding let llm can read data)
- Evaluation (evaluate it's good or not for your use cases, help you to improve your langchain app)
- Agents

## Agents
### IELTS Agent
- for writing skill
  - making bot familiar with all history essays
  - Q&A question for learner and correct the grammatical mistake in learner's answer. And give a recommend answer.
- for speaking skill
  - making bot familiar with all history
  - talking with learner 

## RAG (retrieval-augmented generation)
- document loading
- document split
- document embedding and store in vector database
- retrieval from vector database
- answer generation 