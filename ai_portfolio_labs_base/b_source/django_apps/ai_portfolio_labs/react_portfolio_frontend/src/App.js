import React, { useEffect, useState } from "react";


function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/portfolio/")
      .then((response) => response.json())
      .then((data) => setData(data.message));
  }, []);

  return (
    <div>
      <h1>React + Django App</h1>
      <h2>{data ? data : "Loading..."}</h2>
    </div>
  );
}

export default App;
