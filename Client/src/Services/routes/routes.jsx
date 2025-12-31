import { createBrowserRouter } from 'react-router-dom';
import Layout from '../../Components/Layouts/Layout';
import { Loader, Chat, ChatList, ChatPage } from '../../Components/Ui/export.js';
import {
  Home,
  Profile,
  Landing,
  Settings,
  Register,
  Login,
  Friends,
  PrivacyPolicy,
  TermsOfService,
  CookiePolicy,
  Security,
} from '../../Pages/pagesExport.js';
import { Suspense } from 'react';
import ProtectedRoutes from './ProtectedRoutes.jsx';

const router = createBrowserRouter([
  {
    path: '/',
    element: (
      <Suspense fallback={<Loader />}>
        <Layout />
      </Suspense>
    ),
    children: [
      { index: true, element: <Landing /> },
      { path: 'login', element: <Login /> },
      { path: 'register', element: <Register /> },
      { path: 'home', element: <Home /> },
      {
        element: <ProtectedRoutes />,
        children: [
          {
            path: 'chat',
            element: <Chat />,
            children: [{ path: ':id', element: <ChatPage /> }],
          },
          { path: 'friends', element: <Friends /> },
          { path: 'profile', element: <Profile /> },
          { path: 'settings', element: <Settings /> },
        ],
      },
      { path: 'privacy', element: <PrivacyPolicy /> },
      { path: 'terms', element: <TermsOfService /> },
      { path: 'policy', element: <CookiePolicy /> },
      { path: 'security', element: <Security /> },
    ],
  },
]);

export default router;
