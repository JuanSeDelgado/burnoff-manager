import { Routes, Route } from "react-router";
import MainLayout from "../layouts/MainLayout";
import Home from "../views/Home";
import Login from "../views/Login";
import NotFound from "../views/NotFound";

export default function AppRouter(){
    return(
        <Routes>

            {/* Ruta a home */}
            <Route
            path = "/"
            element={
                <MainLayout>
                    <Home/>
                </MainLayout>
            }
            />

            <Route
            path = "/login"
            element={
                <MainLayout>
                    <Login/>
                </MainLayout>
            }
            />

             <Route
            path = "*"
            element={
                <MainLayout>
                    <NotFound/>
                </MainLayout>
            }
            />
        </Routes>
    )
}