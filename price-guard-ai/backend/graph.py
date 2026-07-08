from typing import TypedDict, Any


from langgraph.graph import (
    StateGraph,
    END
)



from resolver import resolve_product


from search import (
    collect_product_information
)



from extractor import (
    extract_market_prices
)



from price_engine import (
    build_price_analysis
)



from agents import (
    analyze_sentiment,
    generate_final_explanation
)





class AgentState(TypedDict):

    product:str

    normalized_product:str

    user_price:float


    web_content:str

    sources:list[str]


    extracted_prices:list[int]


    price_analysis:dict[str,Any]


    sentiment:dict[str,Any]


    explanation:dict[str,Any]






def resolver_node(state):

    result = resolve_product(
        state["product"]
    )


    return {

        "normalized_product":
            result[
                "normalized_name"
            ]

    }







def search_node(state):


    result = collect_product_information(

        state["normalized_product"]

    )


    return {

        "web_content":
            result["content"],


        "sources":
            result["sources"]

    }






def extract_node(state):


    prices = extract_market_prices(

        state["web_content"]

    )


    return {

        "extracted_prices":
            prices

    }






def price_node(state):


    analysis = build_price_analysis(

        state["extracted_prices"],

        state["user_price"]

    )


    return {

        "price_analysis":
            analysis

    }







def sentiment_node(state):


    result = analyze_sentiment(

        state["normalized_product"],

        state["web_content"]

    )


    return {

        "sentiment":
            result

    }







def explanation_node(state):


    result = generate_final_explanation(

        state["normalized_product"],

        state["price_analysis"],

        state["sentiment"]

    )


    return {

        "explanation":
            result

    }








workflow = StateGraph(
    AgentState
)



workflow.add_node(
    "resolver",
    resolver_node
)


workflow.add_node(
    "search",
    search_node
)


workflow.add_node(
    "extract",
    extract_node
)


workflow.add_node(
    "price",
    price_node
)


workflow.add_node(
    "sentiment",
    sentiment_node
)


workflow.add_node(
    "explain",
    explanation_node
)





workflow.set_entry_point(
    "resolver"
)



workflow.add_edge(
    "resolver",
    "search"
)


workflow.add_edge(
    "search",
    "extract"
)


workflow.add_edge(
    "extract",
    "price"
)


workflow.add_edge(
    "price",
    "sentiment"
)


workflow.add_edge(
    "sentiment",
    "explain"
)


workflow.add_edge(
    "explain",
    END
)




graph = workflow.compile()