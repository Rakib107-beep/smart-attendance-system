
function Greeting() {

    const hour = new Date().getHours();

    let text = "Good Evening";

    if (hour < 12) {
        text = "Good Morning";
    } else if (hour < 17) {
        text = "Good Afternoon";
    }

    return (
        <div>
            <h1 className="text-4xl font-bold">
                {text} 👋
            </h1>

            <p className="text-gray-400 mt-2">
                Welcome back, Rakib
            </p>
        </div>
    );

}

export default Greeting;