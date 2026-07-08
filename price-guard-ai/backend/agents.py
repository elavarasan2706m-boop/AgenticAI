import json

from pydantic import BaseModel, Field

from langchain_google_genai import ChatGoogleGenerativeAI



llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)



class SentimentResult(BaseModel):

    sentiment: str = Field(
        description="Positive, Negative, or Mixed"
    )

    summary: str



class ExplanationResult(BaseModel):

    confidence: int = Field(
        description="Confidence score from 0 to 100"
    )

    explanation: str





sentiment_llm = llm.with_structured_output(
    SentimentResult
)



explanation_llm = llm.with_structured_output(
    ExplanationResult
)





def analyze_sentiment(
    product: str,
    web_content: str
):


    prompt = f"""

Analyze customer sentiment.

Product:

{product}


Use this information:

{web_content[:3000]}


Return:

- overall sentiment
- short summary


Do not discuss prices.

"""


    try:

        result = sentiment_llm.invoke(
            prompt
        )


        return {

            "sentiment":
                result.sentiment,

            "summary":
                result.summary

        }


    except Exception as e:


        return {

            "sentiment":
                "Unknown",

            "summary":
                "Sentiment unavailable"

        }







def generate_final_explanation(
    product: str,
    price_analysis: dict,
    sentiment: dict
):


    prompt = f"""

You are PriceGuard AI.


Product:

{product}



Price analysis:

{json.dumps(
    price_analysis,
    indent=2
)}



Customer sentiment:

{json.dumps(
    sentiment,
    indent=2
)}



Rules:

1. Do not change the decision.
2. Trust the price calculation.
3. Explain risks clearly.
4. If price is extremely low, mention possible fraud/counterfeit.
5. Confidence must be 0-100 integer.



Return only:

confidence

and

explanation

"""


    try:


        result = explanation_llm.invoke(
            prompt
        )


        return {

            "confidence":
                result.confidence,

            "explanation":
                result.explanation

        }



    except Exception:


        return {

            "confidence":
                50,

            "explanation":
                "Unable to generate explanation."

        }