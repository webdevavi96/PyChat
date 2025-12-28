import { createBrowserRouter } from "react-router-dom";
import Layout from "../../Components/Layouts/Layout";
import { Loader } from "../../Components/Ui/export.js";
import { Home, Chat, Profile, Landing, Settings, Register, Login, Friends } from "../../Pages/pagesExport.js";
import { Suspense } from "react";





const router = createBrowserRouter([
    {
        path: "/",
        element: <Suspense fallback={Loader}>
            <Layout />
        </Suspense>,
        children: [
            { index: true, element: <Landing /> },
            { path: "/login", element: < Login /> },
            { path: "/register", element: < Register /> },
            { path: "/home", element: < Home /> },
            { path: "/chat", element: < Chat /> },
            { path: "/friends", element: < Friends /> },
            { path: "/profile", element: < Profile /> },
            { path: "/settings", element: < Settings /> },

        ]

    }
]);


export default router;