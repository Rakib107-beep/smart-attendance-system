import { useEffect, useState } from "react";

function LiveClock() {

    const [time, setTime] = useState(new Date());

    useEffect(() => {

        const timer = setInterval(() => {
            setTime(new Date());
        }, 1000);

        return () => clearInterval(timer);

    }, []);

    return (

        <div className="text-right">

            <h2 className="text-xl font-semibold text-cyan-400">
                {
                    time.toLocaleDateString("en-US", {
                        weekday: "long"
                    })
                }
            </h2>

            <p className="text-gray-400">
                {
                    time.toLocaleDateString()
                }
            </p>

            <h3 className="mt-2 text-3xl font-bold">
                {
                    time.toLocaleTimeString()
                }
            </h3>

        </div>

    );

}

export default LiveClock;