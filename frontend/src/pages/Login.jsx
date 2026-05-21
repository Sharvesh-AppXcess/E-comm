import { useState } from "react";
import API from "../services/api";
import { useNavigate } from "react-router-dom";


export default function Login() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();
    
    const handleLogin = async () => {

        try {

            const response = await API.post(
                "/auth/login",
                {
                    email,
                    password
                }
            );

            // Save JWT token
            localStorage.setItem(
                "token",
                response.data.access_token
            );

            navigate("/products");

        } catch (error) {

            alert("Login Failed");
        }
    };

    return (

        <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600">

            <div className="bg-white p-8 rounded-xl shadow-xl w-96">

                <h1 className="text-3xl font-bold text-center mb-6">
                    Login
                </h1>

                <input
                    type="email"
                    placeholder="Email"
                    className="w-full border p-3 rounded mb-4"
                    onChange={(e) => setEmail(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Password"
                    className="w-full border p-3 rounded mb-4"
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button
                    onClick={handleLogin}
                    className="w-full bg-blue-600 text-white p-3 rounded hover:bg-blue-700"
                >
                    Login
                </button>

            </div>

        </div>
    );
}