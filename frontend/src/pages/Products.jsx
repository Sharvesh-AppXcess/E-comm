import { useEffect, useState } from "react";

import API from "../services/api";

import { useNavigate } from "react-router-dom";


export default function Products() {

    // Router navigation
    const navigate = useNavigate();


    // Stores products
    const [products, setProducts] = useState([]);


    // Runs when page loads
    useEffect(() => {

        const fetchProducts = async () => {

            try {

                // Fetch products from backend
                const response = await API.get("/products");

                // Save products
                setProducts(response.data);

            } catch (error) {

                console.log(error);

                alert("Failed to fetch products");
            }
        };

        fetchProducts();

    }, []);


    // Add product into cart
    const addToCart = async (productId) => {

        try {

            // JWT token
            const token = localStorage.getItem("token");


            // POST request
            await API.post(

                `/cart/${productId}`,

                {
                    quantity: 1
                },

                {
                    headers: {

                        Authorization: `Bearer ${token}`
                    }
                }
            );

            alert("Added To Cart");

        } catch (error) {

            console.log(error);

            alert("Failed To Add Cart");
        }
    };


    return (

        <div className="min-h-screen bg-gray-100 p-8">

            {/* Heading */}
            <h1 className="text-4xl font-bold text-center mb-10">

                Products

            </h1>


            {/* Go To Cart Button */}
            <div className="flex justify-end mb-6">

                <button

                    onClick={() => navigate("/cart")}

                    className="bg-green-600 text-white px-4 py-2 rounded"
                >

                    Go To Cart

                </button>

            </div>


            {/* Product Grid */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

                {products.map((product) => (

                    <div
                        key={product.id}
                        className="bg-white p-6 rounded-xl shadow-lg"
                    >

                        {/* Product Name */}
                        <h2 className="text-2xl font-bold mb-2">

                            {product.name}

                        </h2>

                        {/* Description */}
                        <p className="text-gray-600 mb-2">

                            {product.description}

                        </p>

                        {/* Price */}
                        <p className="text-lg font-semibold mb-2">

                            ₹ {product.price}

                        </p>

                        {/* Stock */}
                        <p className="mb-4">

                            Stock: {product.stock}

                        </p>


                        {/* Add To Cart Button */}
                        <button

                            onClick={() => addToCart(product.id)}

                            className="w-full bg-blue-600 text-white p-3 rounded hover:bg-blue-700"
                        >

                            Add To Cart

                        </button>

                    </div>
                ))}

            </div>

        </div>
    );
}