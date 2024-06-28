from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv
import argparse

load_dotenv()


parser = argparse.ArgumentParser()
parser.add_argument("--task", default="sum two numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()


# No need to fetch this becasue the OPENAI_API_KEY is known by OpenAI
# api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(
    # openai_api_key=api_key
)

code_prompt = PromptTemplate(
    template="Write a short {language} code that will {task}",
    input_variables=["language", "task"]
)

error_checking_prompt = PromptTemplate(
    template="Write a unit test for this code in {language}:\n{code}",
    input_variables=["code", "language"]
)

code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key="code"
)

error_checking_chain = LLMChain(
    llm=llm,
    prompt=error_checking_prompt,
    output_key="unittest"
)

chain = SequentialChain(
    chains=[code_chain, error_checking_chain],
    input_variables=["task", "language"],
    output_variables=["unittest", "code"]
)

result = chain({
    "language": args.language,
    "task": args.task
})

print("--------- code ---------")
print(result["code"])
print("--------- unittest ---------")
print(result["unittest"])
