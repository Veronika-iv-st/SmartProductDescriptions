from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from config import OPENAI_API_KEY

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=OPENAI_API_KEY)

description = input("Write the current product description: ")

prompt = PromptTemplate(
    input_variables=["description"],
    template="""
You are an e-commerce professional. With the product description you receive, I want you to improve it at a professional level so that the product description catches the buyers' attention and stays true to the product.
Use clear language and focus on highlighting the product’s benefits.
Original description: {description}
Return only the new product description without explanations.
"""
)

chain = LLMChain(llm=llm, prompt=prompt)

respuesta = chain.run(description)

print(respuesta)