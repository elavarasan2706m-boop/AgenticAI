from dotenv import load_dotenv

load_dotenv()


from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware


from schemas import (
    AnalyzeRequest,
    AnalyzeResponse
)


from graph import graph



app = FastAPI(

    title="PriceGuard AI",

    version="3.0"

)



app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)



@app.get("/")
def home():

    return {

        "status": "online",

        "service": "PriceGuard AI"

    }





@app.post(
    "/analyze",
    response_model=AnalyzeResponse
)
def analyze(

    request: AnalyzeRequest

):

    try:

        result = graph.invoke(

            {

                "product":
                    request.product,

                "user_price":
                    request.price

            }

        )


        price = result.get(
            "price_analysis",
            {}
        )


        sentiment = result.get(
            "sentiment",
            {}
        )


        explanation = result.get(
            "explanation",
            {}
        )



        market = price.get(
            "market",
            {}
        )



        return {


            "product":
                request.product,


            "user_price":
                request.price,


            "market":

                market,


            "deal_rating":

                price.get(
                    "deal_rating",
                    "Unknown"
                ),


            "risk_level":

                price.get(
                    "risk_level",
                    "Unknown"
                ),


            "decision":

                price.get(
                    "decision",
                    "WAIT"
                ),


            "discount":

                price.get(
                    "discount"
                ),



            "sentiment":

                sentiment.get(
                    "sentiment",
                    "Unknown"
                ),



            "confidence": int(
                float(
                    explanation.get(
                        "confidence",
                        70
                    )
                ) * (
                    100
                    if float(
                        explanation.get(
                            "confidence",
                            70
                        )
                    ) <= 1
                    else 1
                )
            ),



            "explanation":

                explanation.get(
                    "explanation",
                    ""
                ),



            "sources":

                result.get(
                    "sources",
                    []
                )

        }


    except Exception as e:

        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
