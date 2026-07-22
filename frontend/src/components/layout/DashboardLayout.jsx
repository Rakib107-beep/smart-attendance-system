import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

function DashboardLayout({ children }) {
    return (
        <div className="flex h-screen bg-[#070b1a] text-white">

            <Sidebar />

            <div className="flex-1 flex flex-col">

                <Navbar />

                <main className="flex-1 overflow-y-auto p-8">

                    <h1 className="text-red-500 text-5xl">
                        Layout Working
                    </h1>

                    {children}

                </main>

            </div>

        </div>
    );
}

export default DashboardLayout;