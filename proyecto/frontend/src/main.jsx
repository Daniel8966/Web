
import './index.css'
import App from './App.jsx'
import React from "react";
import ReactDOM from "react-dom/client";
import Login from "./Login";  
import { BrowserRouter, Routes, Route } from "react-router-dom";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/login" element={<Login />} /> 
    </Routes>
  </BrowserRouter>
);