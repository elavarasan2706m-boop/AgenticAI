from pydantic import BaseModel, Field

from langchain_google_genai import ChatGoogleGenerativeAI



llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)



class ProductResolution(BaseModel):

    normalized_name: str = Field(
        description="Exact product name"
    )

    brand: str = Field(
        description="Product brand"
    )

    category: str = Field(
        description="Product category"
    )

    clarification_needed: bool = Field(
        description="Whether user input is too generic"
    )





resolver_llm = llm.with_structured_output(
    ProductResolution
)





def resolve_product(product: str):


    prompt = f"""

You are a product identification agent.

User entered:

{product}


Identify the most likely exact product.

Rules:

- Do not use prices.
- Do not guess random products.
- If product name is incomplete, choose the most common current product.
- Set clarification_needed=true if multiple products are possible.


Return:

normalized_name
brand
category
clarification_needed

"""


    try:

        result = resolver_llm.invoke(
            prompt
        )


        return {

            "normalized_name":
                result.normalized_name,

            "brand":
                result.brand,

            "category":
                result.category,

            "clarification_needed":
                result.clarification_needed

        }



    except Exception as e:


        print(
            "Resolver error:",
            e
        )


        return {

            "normalized_name":
                product,

            "brand":
                "",

            "category":
                "",

            "clarification_needed":
                True

        }