import { useEffect, useState } from "react";

import API from "../services/api";

import { useNavigate } from "react-router-dom";


export default function Cart() {

    // Used for page navigation
    const navigate = useNavigate();


    // Stores cart items
    const [cartItems, setCartItems] = useState([]);


    // Stores total quantity
    const [total, setTotal] = useState(0);


    // Runs automatically when page loads
    useEffect(() => {

        fetchCart();

    }, []);


    // Function to fetch cart items
    const fetchCart = async () => {

        try {

            // JWT token from localStorage
            const token = localStorage.getItem("token");


            // GET request to backend
            const response = await API.get(

                "/cart",

                {
                    headers: {

                        Authorization: `Bearer ${token}`
                    }
                }
            );


            // Save cart items into state
            setCartItems(response.data);


            // Variable to calculate total quantity
            let cartTotal = 0;


            // Loop through all cart items
            response.data.forEach((item) => {

                // Add quantity
                cartTotal += item.quantity;
            });


            // Save total quantity
            setTotal(cartTotal);

        } catch (error) {

            console.log(error);

            alert("Failed to fetch cart");
        }
    };


    // Function to remove item from cart
    const removeFromCart = async (cartId) => {

        try {

            // JWT token
            const token = localStorage.getItem("token");


            // DELETE request
            await API.delete(

                `/cart/${cartId}`,

                {
                    headers: {

                        Authorization: `Bearer ${token}`
                    }
                }
            );


            alert("Item Removed");


            // Refresh cart items
            fetchCart();

        } catch (error) {

            console.log(error);

            alert("Failed to remove item");
        }
    };


    return (

        <div className="min-h-screen bg-gray-100 p-8">

            {/* Page Heading */}
            <h1 className="text-4xl font-bold text-center mb-10">

                My Cart

            </h1>


            {/* If cart is empty */}
            {cartItems.length === 0 ? (

                <p className="text-center text-xl">

                    Cart is Empty

                </p>

            ) : (

                <div className="space-y-6">

                    {/* Loop through cart items */}
                    {cartItems.map((item) => (

                        <div
                            key={item.id}
                            className="bg-white p-6 rounded-xl shadow-lg flex justify-between items-center"
                        >

                            <div>

                                {/* Product ID */}
                                <h2 className="text-2xl font-bold">

                                    Product ID: {item.product_id}

                                </h2>


                                {/* Quantity */}
                                <p>

                                    Quantity: {item.quantity}

                                </p>

                            </div>


                            {/* Remove Button */}
                            <button

                                onClick={() => removeFromCart(item.id)}

                                className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
                            >

                                Remove

                            </button>

                        </div>
                    ))}


                    {/* Total Section */}
                    <div className="bg-white p-6 rounded-xl shadow-lg text-right">

                        <h2 className="text-3xl font-bold">

                            Total Quantity: {total}

                        </h2>

                    </div>


                    {/* Place Order Button */}
                    <button

                        onClick={() => navigate("/orders")}

                        className="w-full bg-blue-600 text-white p-3 rounded mt-6 hover:bg-blue-700"
                    >

                        Place Order

                    </button>

                </div>
            )}

        </div>
    );
}