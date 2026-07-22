function StatCard({

    icon,
    title,
    value,
    color = "text-cyan-400"

}) {

    return (

        <div
            className="
                bg-slate-900
                border
                border-slate-800
                rounded-3xl
                p-6
                hover:-translate-y-2
                duration-300
            "
        >

            <div className={`${color} mb-4`}>

                {icon}

            </div>

            <p className="text-gray-400">

                {title}

            </p>

            <h2 className="text-4xl font-bold mt-2">

                {value}

            </h2>

        </div>

    );

}

export default StatCard;