import { useState } from "react";

function App() {
  const [data, setData] = useState({
    product: "",
    price: "",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    if (!data.product.trim() || !data.price) {
      setError("Please enter product name and price.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setResult(null);

      const response = await fetch(
        "http://localhost:8000/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            product: data.product,
            price: Number(data.price),
          }),
        }
      );

      if (!response.ok) {
        throw new Error("Backend error");
      }

      const json = await response.json();

      setResult(json);

    } catch (err) {
      console.error(err);
      setError(
        "Cannot connect to PriceGuard AI backend."
      );
    } finally {
      setLoading(false);
    }
  };


  const getDecisionColor = (decision) => {
    if (!decision) return "#333";

    if (
      decision.includes("BUY")
    ) {
      return "#16a34a";
    }

    if (
      decision.includes("WAIT")
    ) {
      return "#ca8a04";
    }

    return "#dc2626";
  };


  return (
    <div style={styles.page}>

      <div style={styles.container}>

        <h1 style={styles.title}>
          🛡️ PriceGuard AI
        </h1>

        <p style={styles.subtitle}>
          AI-powered product price analysis
        </p>


        <input
          style={styles.input}
          type="text"
          placeholder="Enter product name"
          value={data.product}
          onChange={(e) =>
            setData({
              ...data,
              product: e.target.value,
            })
          }
        />


        <input
          style={styles.input}
          type="number"
          placeholder="Enter your price"
          value={data.price}
          onChange={(e) =>
            setData({
              ...data,
              price: e.target.value,
            })
          }
        />


        <button
          style={styles.button}
          onClick={handleAnalyze}
          disabled={loading}
        >
          {loading
            ? "Analyzing..."
            : "Analyze Price"}
        </button>



        {error && (
          <div style={styles.error}>
            {error}
          </div>
        )}



        {result && (

          <div style={styles.result}>


            <h2>
              Decision:
              {" "}
              <span
                style={{
                  color:
                    getDecisionColor(
                      result.decision
                    ),
                }}
              >
                {result.decision}
              </span>
            </h2>



            <div style={styles.card}>

              <h3>
                📊 Price Analysis
              </h3>


              <p>
                Your Price:
                {" "}
                ₹{result.user_price}
              </p>


              <p>
                Minimum Market Price:
                {" "}
                ₹
                {
                  result.market
                    ?.min_price ?? "N/A"
                }
              </p>


              <p>
                Average Market Price:
                {" "}
                ₹
                {
                  result.market
                    ?.average_price ?? "N/A"
                }
              </p>


              <p>
                Maximum Market Price:
                {" "}
                ₹
                {
                  result.market
                    ?.max_price ?? "N/A"
                }
              </p>

            </div>



            <div style={styles.card}>

              <h3>
                🏷️ Deal Information
              </h3>


              <p>
                Deal Rating:
                {" "}
                <b>
                  {result.deal_rating}
                </b>
              </p>


              <p>
                Risk Level:
                {" "}
                <b>
                  {result.risk_level}
                </b>
              </p>


              <p>
                Discount:
                {" "}
                {result.discount ?? 0}%
              </p>

            </div>



            <div style={styles.card}>

              <h3>
                🤖 AI Analysis
              </h3>


              <p>
                Sentiment:
                {" "}
                {result.sentiment}
              </p>


              <p>
                Confidence:
                {" "}
                {result.confidence}%
              </p>


              <p>
                {result.explanation}
              </p>

            </div>



            {
              result.sources &&
              result.sources.length > 0 &&

              <div style={styles.card}>

                <h3>
                  🔗 Sources
                </h3>


                {
                  result.sources.map(
                    (source, index) => (

                      <p key={index}>

                        <a
                          href={source}
                          target="_blank"
                          rel="noreferrer"
                        >
                          {source}
                        </a>

                      </p>

                    )
                  )
                }

              </div>
            }


          </div>

        )}

      </div>

    </div>
  );
}



const styles = {

  page: {
    minHeight: "100vh",
    background:
      "linear-gradient(135deg,#eef2ff,#f8fafc)",
    padding: "40px",
    fontFamily:
      "Arial, sans-serif",
  },


  container: {

    maxWidth: "750px",

    margin: "auto",

    background: "white",

    padding: "35px",

    borderRadius: "18px",

    boxShadow:
      "0 10px 30px rgba(0,0,0,0.12)",

  },


  title: {

    textAlign: "center",

    color:"#111827",

  },


  subtitle: {

    textAlign:"center",

    color:"#6b7280",

    marginBottom:"30px"

  },


  input: {

    width:"100%",

    padding:"14px",

    marginBottom:"15px",

    borderRadius:"10px",

    border:
      "1px solid #d1d5db",

    fontSize:"16px",

    boxSizing:"border-box"

  },


  button: {

    width:"100%",

    padding:"15px",

    borderRadius:"10px",

    border:"none",

    background:"#2563eb",

    color:"white",

    fontSize:"17px",

    cursor:"pointer"

  },


  result: {

    marginTop:"30px"

  },


  card: {

    background:"#f9fafb",

    padding:"20px",

    borderRadius:"12px",

    marginTop:"15px",

    border:
      "1px solid #e5e7eb"

  },


  error: {

    marginTop:"20px",

    padding:"15px",

    background:"#fee2e2",

    color:"#991b1b",

    borderRadius:"10px"

  }

};


export default App;