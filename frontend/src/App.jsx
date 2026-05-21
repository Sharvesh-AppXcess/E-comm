import {
  BrowserRouter, Routes, Route
} from "react-router-dom";

import Products from "./pages/Products";
import Orders from "./pages/Order";
import Cart from "./pages/Cart";
import Login from "./pages/Login";

export default function App() {

    return (
      
        <BrowserRouter>
            <Routes>
              <Route path="/" element={<Login />}/>
              <Route path="/Products" element={<Products />}/>
              <Route path="/Cart" element={<Cart />}/>
              <Route path="/Orders" element={<Orders />}/>
            </Routes>
        </BrowserRouter>
    );
}