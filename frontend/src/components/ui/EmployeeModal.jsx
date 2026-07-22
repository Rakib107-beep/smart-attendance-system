function EmployeeModal({

    open,
    title,
    children,
    onClose

}) {

    if (!open) {

        return null;

    }

    return (

        <div
            className="
                fixed
                inset-0
                bg-black/70
                backdrop-blur-sm
                flex
                items-center
                justify-center
                z-50
            "
        >

            <div
                className="
                    bg-[#111827]
                    rounded-3xl
                    w-full
                    max-w-2xl
                    border
                    border-slate-700
                    shadow-2xl
                "
            >

                <div
                    className="
                        flex
                        justify-between
                        items-center
                        p-6
                        border-b
                        border-slate-700
                    "
                >

                    <h2
                        className="
                            text-2xl
                            font-bold
                        "
                    >

                        {title}

                    </h2>

                    <button
                        onClick={onClose}
                        className="
                            text-2xl
                            hover:text-red-400
                        "
                    >

                        ✕

                    </button>

                </div>

                <div className="p-6">

                    {children}

                </div>

            </div>

        </div>

    );

}

export default EmployeeModal;