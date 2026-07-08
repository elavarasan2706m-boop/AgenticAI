from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):

    product: str = Field(
        ...,
        min_length=2,
        description="Product name"
    )

    price: float = Field(
        ...,
        gt=0,
        description="User offered price"
    )



class MarketData(BaseModel):

    min_price: int | None = None

    max_price: int | None = None

    average_price: int | None = None



class AnalyzeResponse(BaseModel):

    product: str


    user_price: float


    market: MarketData | None = None


    deal_rating: str


    risk_level: str


    decision: str


    discount: float | None = None


    sentiment: str


    confidence: float


    explanation: str


    sources: list[str]