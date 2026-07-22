import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../../services/authService";

import { Eye, EyeOff, ShieldCheck } from "lucide-react";
import { motion } from "framer-motion";

function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [showPassword, setShowPassword] = useState(false);

    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await login(username, password);

            localStorage.setItem(
                "token",
                response.access_token
            );

            navigate("/dashboard");

        } catch (error) {

            alert(
                error.response?.data?.detail ||
                "Login Failed"
            );

        }

    };

    return (

        <div className="relative min-h-screen overflow-hidden bg-[#050816]">

            <div className="absolute w-72 h-72 bg-cyan-500/30 rounded-full blur-3xl top-0 -left-20 animate-pulse"></div>

            <div className="absolute w-96 h-96 bg-indigo-600/30 rounded-full blur-3xl bottom-0 right-0 animate-pulse"></div>

            <div className="flex justify-center items-center min-h-screen">

                <motion.div

                    initial={{ opacity: 0, scale: .8 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: .5 }}

                    className="w-[420px]
                               rounded-3xl
                               border border-white/20
                               bg-white/10
                               backdrop-blur-xl
                               p-10
                               shadow-2xl"

                >

                    <div className="flex justify-center">

                        <div className="bg-cyan-500 p-4 rounded-full">

                            <ShieldCheck
                                size={40}
                                className="text-white"
                            />

                        </div>

                    </div>

                    <h1 className="text-center text-white text-3xl font-bold mt-6">

                        Smart Attendance

                    </h1>

                    <p className="text-center text-slate-300 mt-2">

                        Welcome Back

                    </p>

                    <form
                        onSubmit={handleLogin}
                        className="mt-8 space-y-5"
                    >

                        <input

                            type="text"

                            placeholder="Username"

                            value={username}

                            onChange={(e) =>
                                setUsername(e.target.value)
                            }

                            className="w-full
                                       rounded-xl
                                       bg-white/10
                                       border
                                       border-white/20
                                       px-4
                                       py-3
                                       text-white
                                       placeholder:text-slate-300
                                       outline-none
                                       focus:border-cyan-400"

                        />

                        <div className="relative">

                            <input

                                type={
                                    showPassword
                                        ? "text"
                                        : "password"
                                }

                                placeholder="Password"

                                value={password}

                                onChange={(e) =>
                                    setPassword(e.target.value)
                                }

                                className="w-full
                                           rounded-xl
                                           bg-white/10
                                           border
                                           border-white/20
                                           px-4
                                           py-3
                                           pr-12
                                           text-white
                                           placeholder:text-slate-300
                                           outline-none
                                           focus:border-cyan-400"

                            />

                            <button

                                type="button"

                                onClick={() =>
                                    setShowPassword(
                                        !showPassword
                                    )
                                }

                                className="absolute
                                           right-4
                                           top-1/2
                                           -translate-y-1/2
                                           text-slate-300"

                            >

                                {
                                    showPassword
                                        ? <EyeOff size={20}/>
                                        : <Eye size={20}/>
                                }

                            </button>

                        </div>

                        <motion.button

                            whileHover={{
                                scale: 1.03
                            }}

                            whileTap={{
                                scale: .97
                            }}

                            className="w-full
                                       rounded-xl
                                       bg-cyan-500
                                       py-3
                                       font-bold
                                       text-white
                                       hover:bg-cyan-400"

                        >

                            LOGIN

                        </motion.button>

                    </form>

                </motion.div>

            </div>

        </div>

    );

}

export default Login;