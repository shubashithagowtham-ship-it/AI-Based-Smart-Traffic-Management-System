import React from "react";

function TrafficChart({ history }) {
  const maxValue = Math.max(...history, 1);

  return (
    <div
      style={{
        marginTop: "30px",
        background: "white",
        padding: "20px",
        borderRadius: "10px"
      }}
    >
      <h2>Traffic Analytics</h2>

      <div
        style={{
          display: "flex",
          alignItems: "flex-end",
          gap: "10px",
          height: "250px",
          marginTop: "20px"
        }}
      >
        {history.map((value, index) => (
          <div
            key={index}
            style={{
              width: "40px",
              height: `${(value / maxValue) * 200}px`,
              backgroundColor: "steelblue",
              textAlign: "center",
              color: "white"
            }}
          >
            {value}
          </div>
        ))}
      </div>
    </div>
  );
}

export default TrafficChart;