
async function test() {
  const apiKey = "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";
  const query = "latest AI news";
  
  console.log("Starting Tavily search test via fetch...");
  
  try {
    const response = await fetch("https://api.tavily.com/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        api_key: apiKey,
        query: query,
        num_results: 1
      })
    });
    
    const data = await response.json();
    
    if (response.ok) {
      console.log("Search successful!");
      console.log(JSON.stringify(data, null, 2));
    } else {
      console.error("Search failed with status:", response.status);
      console.error(JSON.stringify(data, null, 2));
    }
  } catch (error) {
    console.error("Request failed:", error);
  }
}

test();
