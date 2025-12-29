import React, { useContext } from "react";
import { Navigate, Outlet, useLocation } from "react-router-dom";
import { Loader } from "../../Components/Ui/export.js";
import { AuthContext } from "../../Contexts/authContext.jsx";

export default function ProtectedRoutes() {
    const { isAuthenticated, loading } = useContext(AuthContext);
    const location = useLocation();

    if (loading) {
        return <Loader />;
    }

    if (!isAuthenticated) {
        return (
            <Navigate
                to="/"
                replace
                state={{ from: location.pathname }}
            />
        );
    }

    return <Outlet />;
}
