import React, { useEffect, useState } from "react";
import axios from "axios";
import TrafficChart from "./TrafficChart";

function App() {
  const [traffic, setTraffic] = useState(null);
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetchTraffic();

    const interval = setInterval(() => {
      fetchTraffic();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const fetchTraffic = async () => {
    try {
      const response = await axios.get(
        "http://127.0.0.1:8000/latest-traffic"
      );

      setTraffic(response.data);

      const historyResponse = await axios.get(
        "http://127.0.0.1:8000/traffic-history"
      );

      setHistory(historyResponse.data);
    } catch (error) {
      console.error(error);
    }
  };

  const cardStyle = {
    background: "white",
    padding: "25px",
    borderRadius: "15px",
    width: "220px",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  };

  const valueStyle = {
    fontSize: "42px",
    fontWeight: "bold",
    marginTop: "10px"
  };

  return (
    <div
      style={{
        padding: "40px",
        fontFamily: "Arial",
        backgroundColor: "#f4f4f4",
        minHeight: "100vh"
      }}
    >
      <h1
        style={{
          marginBottom: "30px"
        }}
      >
        🚦 Smart Traffic Dashboard
      </h1>

      {traffic && (
        <>
          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              gap: "20px"
            }}
          >
            <div style={cardStyle}>
              <h2>Vehicles</h2>
              <h1 style={valueStyle}>
                {traffic.vehicle_count}
              </h1>
            </div>

            <div style={cardStyle}>
              <h2>Cars</h2>
              <h1 style={valueStyle}>
                {traffic.cars}
              </h1>
            </div>

            <div style={cardStyle}>
              <h2>Bikes</h2>
              <h1 style={valueStyle}>
                {traffic.bikes}
              </h1>
            </div>

            <div style={cardStyle}>
              <h2>Buses</h2>
              <h1 style={valueStyle}>
                {traffic.buses}
              </h1>
            </div>

            <div style={cardStyle}>
              <h2>Trucks</h2>
              <h1 style={valueStyle}>
                {traffic.trucks}
              </h1>
            </div>

            <div style={cardStyle}>
              <h2>Congestion</h2>

              <h1
                style={{
                  ...valueStyle,
                  color:
                    traffic.congestion === "LOW"
                      ? "green"
                      : traffic.congestion === "MEDIUM"
                      ? "orange"
                      : "red"
                }}
              >
                {traffic.congestion}
              </h1>
            </div>

            <div style={cardStyle}>
              <h2>Signal Time</h2>
              <h1 style={valueStyle}>
                {traffic.signal_time}s
              </h1>
            </div>
          </div>

          <div
            style={{
              marginTop: "30px",
              background: "white",
              padding: "25px",
              borderRadius: "15px",
              boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
            }}
          >
            <TrafficChart history={history} />
          </div>
        </>
      )}
    </div>
  );
}

export default App;