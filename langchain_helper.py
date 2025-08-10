from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

llm = OllamaLLM(model='mistral')

def generate_restaurant_name_and_item(cuisine):
    prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = " i want to open a restaurant for {cuisine} food . Suggest a single fancy name for this , remember to only give the restaurant name as the output and dont give additional information about the restaurant name ."
    )
    name_chain = LLMChain(llm = llm , prompt=prompt_template_name,output_key = "restaurant_name")
    prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = 'suggest some food items for the {restaurant_name} and only stick to the dish names . No need for additional descriptions related to the restaurant name or the dish name.'
    )
    
    food_item_chain = LLMChain(llm=llm,prompt=prompt_template_items,output_key='menu_items')
    
    chain = SequentialChain(
    chains = [name_chain,food_item_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name','menu_items']
    )
    
    response = chain({'cuisine' : cuisine})
    
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_item("Italian"))



