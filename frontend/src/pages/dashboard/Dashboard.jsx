import { useEffect, useState } from "react";
import {
    Users,
    CalendarCheck,
    AlarmClock,
    UserX,
    LogIn,
    LogOut
} from "lucide-react";

import Greeting from "../../components/common/Greeting";
import LiveClock from "../../components/common/LiveClock";
import StatCard from "../../components/ui/StatCard";

import { getDashboard } from "../../services/dashboardService";

function Dashboard() {

    const [dashboard, setDashboard] = useState(null);

    useEffect(() => {

        loadDashboard();

    }, []);

    async function loadDashboard() {

        try {

            const data = await getDashboard();

            setDashboard(data);

        } catch (e) {

            console.error(e);

        }

    }

    return (

        <div className="space-y-10">

            {/* Header */}

            <div className="flex justify-between items-center">

                <Greeting />

                <LiveClock />

            </div>

            {/* Statistics */}

            <div className="grid lg:grid-cols-4 md:grid-cols-2 gap-6">

                <StatCard
                    icon={<Users size={30} />}
                    title="Employees"
                    value={dashboard?.employee_count ?? 0}
                    color="text-cyan-400"
                />

                <StatCard
                    icon={<CalendarCheck size={30} />}
                    title="Present"
                    value={dashboard?.present ?? 0}
                    color="text-green-400"
                />

                <StatCard
                    icon={<AlarmClock size={30} />}
                    title="Late"
                    value={dashboard?.late ?? 0}
                    color="text-yellow-400"
                />

                <StatCard
                    icon={<UserX size={30} />}
                    title="Absent"
                    value={dashboard?.absent ?? 0}
                    color="text-red-400"
                />

            </div>

            {/* Today's Attendance */}

            <div className="grid lg:grid-cols-2 gap-8">

                <div
                    className="
                        rounded-3xl
                        bg-white/5
                        backdrop-blur-xl
                        border border-white/10
                        p-8
                    "
                >

                    <h2 className="text-2xl font-bold mb-6">

                        Today's Attendance

                    </h2>

                    <div className="space-y-5">

                        <div className="flex justify-between">

                            <span className="flex items-center gap-2">

                                <LogIn className="text-green-400" />

                                Check In

                            </span>

                            <span>

                                {dashboard?.today?.check_in ?? "--"}

                            </span>

                        </div>

                        <div className="flex justify-between">

                            <span className="flex items-center gap-2">

                                <LogOut className="text-red-400" />

                                Check Out

                            </span>

                            <span>

                                {dashboard?.today?.check_out ?? "--"}

                            </span>

                        </div>

                        <div className="flex justify-between">

                            <span>Status</span>

                            <span className="text-cyan-400 font-bold">

                                {dashboard?.today?.status ?? "--"}

                            </span>

                        </div>

                        <div className="flex justify-between">

                            <span>Working Hours</span>

                            <span>

                                {dashboard?.today?.working_hours ?? "--"}

                            </span>

                        </div>

                    </div>

                </div>

                {/* Chart Placeholder */}

                <div
                    className="
                        rounded-3xl
                        bg-gradient-to-br
                        from-cyan-500/20
                        to-purple-500/20
                        border border-cyan-500/20
                        backdrop-blur-xl
                        flex
                        items-center
                        justify-center
                        p-8
                    "
                >

                    <div className="text-center">

                        <h2 className="text-3xl font-bold">

                            Weekly Attendance

                        </h2>

                        <p className="text-slate-400 mt-3">

                            Chart will be added in the next phase

                        </p>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default Dashboard;