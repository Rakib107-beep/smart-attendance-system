import { Bell, LogOut } from "lucide-react";

function Navbar() {

    return (

        <header className="h-20 border-b border-white/10 bg-white/5 backdrop-blur-xl flex items-center justify-between px-8">

            <div>

                <h2 className="text-white text-2xl font-bold">

                    Dashboard

                </h2>

            </div>

            <div className="flex items-center gap-6">

                <Bell
                    className="text-white cursor-pointer"
                    size={22}
                />

                <div className="text-white">

                    Rakib

                </div>

                <LogOut
                    className="text-red-400 cursor-pointer"
                    size={22}
                />

            </div>

        </header>

    );

}

export default Navbar;