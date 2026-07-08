import httpx

from bs4 import BeautifulSoup

from ddgs import DDGS



USER_AGENT = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "Chrome/120 Safari/537.36"
)



def build_queries(product):

    return [

        f"{product} official price India",

        f"{product} buy price India",

        f"{product} Amazon India price",

        f"{product} Flipkart price",

        f"{product} review"

    ]





def duckduckgo_search(product):

    results = []


    queries = build_queries(product)


    with DDGS() as ddgs:


        for query in queries:


            try:

                items = ddgs.text(
                    query,
                    max_results=5
                )


                for item in items:


                    results.append(

                        {

                            "title":
                                item.get(
                                    "title",
                                    ""
                                ),

                            "url":
                                item.get(
                                    "href",
                                    ""
                                ),

                            "snippet":
                                item.get(
                                    "body",
                                    ""
                                )

                        }

                    )


            except Exception as e:

                print(
                    "Search error:",
                    e
                )



    return results






def fetch_page_text(url):

    try:

        response = httpx.get(

            url,

            headers={
                "User-Agent":
                    USER_AGENT
            },

            timeout=10,

            follow_redirects=True

        )


        if response.status_code != 200:

            return ""



        soup = BeautifulSoup(

            response.text,

            "html.parser"

        )


        for tag in soup(

            [
                "script",
                "style",
                "nav",
                "footer",
                "header"
            ]

        ):

            tag.decompose()



        text = soup.get_text(

            separator=" ",

            strip=True

        )


        return text[:5000]



    except Exception:


        return ""







def collect_product_information(product):


    results = duckduckgo_search(
        product
    )


    combined = ""

    sources = []



    for result in results[:10]:


        url = result["url"]


        if not url:

            continue



        page_text = fetch_page_text(
            url
        )



        combined += f"""

TITLE:
{result['title']}

URL:
{url}

SNIPPET:
{result['snippet']}

PAGE:
{page_text}

----------------------

"""



        sources.append(
            url
        )



    return {

        "content":
            combined,

        "sources":
            sources

    }