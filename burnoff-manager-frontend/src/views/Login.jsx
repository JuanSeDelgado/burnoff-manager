import { useForm } from "react-hook-form";
import api from "../api/axios";
import { useState } from "react";
import { useAuth } from "../hooks/useAuth";
import { useNavigate } from "react-router";

export default function Login() {
    const { register, handleSubmit, formState: { errors } } = useForm();
    const [loginError, setLoginError] = useState(null);
    const { login } = useAuth();
    const navigate = useNavigate();

    const onSubmit = async (data) => {
        setLoginError(null);
        try {
            const res = await api.post('/login', {
                email: data.email,
                password: data.password
            });
            
            const user = res.data.admin;
            const token = res.data.token;
            login(user, token);
            navigate("/");
        } catch (error) {
            setLoginError(`Credenciales incorrectas o error de servidor. ${error}`);
        }
    };

    return (
        <div className="bg-gray-800 min-h-screen flex flex-col justify-center items-center p-4">
            <div className="bg-slate-800 rounded-lg px-6 py-8 ring shadow-xl ring-gray-900/5 w-full max-w-sm">
                <h2 className="text-2xl font-bold text-center text-white">Iniciar sesión</h2>
                <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
                    {/* Email */}
                    <div className="mb-4">
                        <label htmlFor="email" className="block text-sm font-medium text-gray-200 mb-1">Email</label>
                        <input
                            id="email"
                            type="email"
                            {...register("email", {
                                required: "El email es obligatorio"
                            })}
                            className={`w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-900 text-white placeholder-gray-400 transition-colors ${errors.email ? "border-red-500" : "border-gray-600"}`}
                            placeholder="ejemplo@correo.com"
                            autoComplete="email"
                        />
                        {errors.email && (
                            <p className="text-red-400 text-xs mt-1">{errors.email.message}</p>
                        )}
                    </div>
                    {/* Password */}
                    <div className="mb-4">
                        <label htmlFor="password" className="block text-sm font-medium text-gray-200 mb-1">Contraseña</label>
                        <input
                            id="contraseña"
                            type="password"
                            {...register("password", {
                                required: "La contraseña es obligatoria"
                            })}
                            className={`w-full px-4 py-2 rounded-lg border focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-900 text-white transition-colors ${errors.password ? "border-red-500" : "border-gray-600"}`}
                            autoComplete="password"
                        />
                        {errors.password && (
                            <p className="text-red-400 text-xs mt-1">{errors.password.message}</p>
                        )}
                    </div>
                    {loginError && (
                        <p className="text-red-400 text-xs text-center">{loginError}</p>
                    )}
                    <button className="w-full min-h-4 rounded-lg text-sm font-medium text-gray-200 py-3 bg-blue-600 hover:bg-blue-700 transition-colors">
                        Ingresar
                    </button>
                </form>
            </div>
        </div>
    );
}