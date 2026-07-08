def calculate_market_stats(prices: list[int]):

    if not prices:
        return {
            "min_price": None,
            "max_price": None,
            "average_price": None
        }


    return {
        "min_price": min(prices),
        "max_price": max(prices),
        "average_price": round(
            sum(prices) / len(prices)
        )
    }



def calculate_discount(
    market_price: float,
    user_price: float
):

    if market_price <= 0:
        return 0


    discount = (
        (market_price - user_price)
        /
        market_price
    ) * 100


    return round(
        discount,
        2
    )



def evaluate_price(
    market_price: float,
    user_price: float
):

    ratio = user_price / market_price


    discount = calculate_discount(
        market_price,
        user_price
    )


    #
    # Extremely cheap
    #
    if ratio < 0.25:

        return {

            "deal_rating":
                "Exceptional Deal",

            "risk_level":
                "Very High",

            "decision":
                "BUY WITH CAUTION",

            "discount":
                discount,

            "reason":
                "Price is extremely below market value. Verify authenticity, warranty, condition, and seller credibility."

        }



    #
    # Great discount
    #
    elif ratio < 0.60:

        return {

            "deal_rating":
                "Excellent Deal",

            "risk_level":
                "Medium",

            "decision":
                "BUY",

            "discount":
                discount,

            "reason":
                "Product is significantly cheaper than current market price."

        }



    #
    # Good discount
    #
    elif ratio < 0.90:

        return {

            "deal_rating":
                "Good Deal",

            "risk_level":
                "Low",

            "decision":
                "BUY",

            "discount":
                discount,

            "reason":
                "Price is below the estimated market average."

        }



    #
    # Normal price
    #
    elif ratio <= 1.10:

        return {

            "deal_rating":
                "Fair Price",

            "risk_level":
                "Low",

            "decision":
                "WAIT",

            "discount":
                discount,

            "reason":
                "Price is close to market average. Compare offers before buying."

        }



    #
    # Expensive
    #
    else:

        return {

            "deal_rating":
                "Overpriced",

            "risk_level":
                "Low",

            "decision":
                "DON'T BUY",

            "discount":
                discount,

            "reason":
                "Price is higher than current market value."

        }



def build_price_analysis(
    prices: list[int],
    user_price: float
):

    stats = calculate_market_stats(
        prices
    )


    if not stats["average_price"]:

        return {

            "market_found": False,

            "decision":
                "WAIT",

            "reason":
                "Unable to find reliable market prices."

        }



    evaluation = evaluate_price(

        stats["average_price"],

        user_price

    )


    return {

        "market_found": True,

        "market": stats,

        "user_price": user_price,

        **evaluation

    }