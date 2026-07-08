import re



# Only accept prices that look like real product prices

PRICE_PATTERNS = [

    # ₹99,999
    r"(?:₹|Rs\.?|INR)\s?\d{1,3}(?:,\d{3})+",

    # ₹99999
    r"(?:₹|Rs\.?|INR)\s?\d{4,6}",

    # $999
    r"\$\s?\d{3,6}"

]



# Words that indicate the number is actually a price

PRICE_CONTEXT = [

    "price",
    "cost",
    "mrp",
    "buy",
    "sale",
    "offer",
    "starts at",
    "starting",
    "retail",
    "available"

]



def normalize_price(value):

    value = (
        value
        .replace(",", "")
        .replace("₹", "")
        .replace("$", "")
        .replace("Rs", "")
        .replace("INR", "")
        .strip()
    )


    try:

        return int(value)

    except:

        return None





def extract_price_candidates(text):

    candidates=[]


    lines = text.split("\n")


    for line in lines:


        lower=line.lower()


        has_context = any(
            word in lower
            for word in PRICE_CONTEXT
        )


        if not has_context:
            continue



        for pattern in PRICE_PATTERNS:


            matches = re.findall(
                pattern,
                line,
                flags=re.I
            )


            for match in matches:


                price = normalize_price(
                    match
                )


                if price:

                    candidates.append(
                        price
                    )


    return candidates





def validate_price(price):


    # Ignore tiny numbers
    # (battery, ratings, years)

    if price < 10000:

        return False



    # Ignore impossible phone prices

    if price > 500000:

        return False



    return True






def remove_outliers(prices):


    if len(prices) < 3:

        return prices



    prices.sort()


    low = prices[0]

    high = prices[-1]


    filtered=[]


    for p in prices:


        # remove extreme values

        if (
            p > low * 0.35
            and
            p < high * 3
        ):

            filtered.append(p)



    return filtered






def extract_market_prices(content):


    prices = extract_price_candidates(
        content
    )


    prices = [

        p for p in prices

        if validate_price(p)

    ]



    prices=list(set(prices))


    prices=remove_outliers(
        prices
    )


    prices.sort()


    return prices