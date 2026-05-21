export default function Order() {

    return (

        <div className="min-h-screen flex items-center justify-center bg-gray-100">

            <div className="bg-white p-10 rounded-xl shadow-lg text-center">

                {/* Success Message */}
                <h1 className="text-4xl font-bold text-green-600 mb-4">

                    Order Placed Successfully 🎉

                </h1>


                {/* Small description */}
                <p className="text-xl text-gray-600">

                    Your order has been placed.

                </p>

            </div>

        </div>
    );
}