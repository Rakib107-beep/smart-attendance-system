import {
    LayoutDashboard,
    Users,
    Clock3,
    CalendarDays,
    BarChart3,
    Settings
} from "lucide-react";

import { useNavigate } from "react-router-dom";

function Sidebar() {

    const navigate = useNavigate();
    const menus = [

        {
            icon: <LayoutDashboard size={20} />,
            title: "Dashboard"
        },

        {
            title: "Employees",
            icon: <Users size={20} />,
            path: "/employees"
        },

        {
            icon: <Clock3 size={20} />,
            title: "Attendance"
        },

        {
            icon: <CalendarDays size={20} />,
            title: "Leave"
        },

        {
            icon: <BarChart3 size={20} />,
            title: "Reports"
        },

        {
            icon: <Settings size={20} />,
            title: "Settings"
        }

    ];

    return (

        <aside className="w-72 bg-white/5 backdrop-blur-xl border-r border-white/10">

            <div className="text-center py-8">

                <h1 className="text-cyan-400 text-3xl font-bold">

                    Smart Attendance

                </h1>

            </div>

            <div className="space-y-2 px-4">

                {

                    menus.map((item, index) => (

                            <button

                                key={index}

                                onClick={() => {

                                    if(item.path){

                                        navigate(item.path);

                                    }

                                }}

                                className="flex items-center gap-4 w-full px-5 py-4 rounded-xl text-gray-300 hover:bg-cyan-500 hover:text-white transition-all duration-300"

                            >

                            {item.icon}

                            {item.title}

                        </button>

                    ))

                }

            </div>

        </aside>

    );

}

export default Sidebar;