import { useState } from 'react'
import './App.css';
import router from './Services/routes/routes';
import { RouterProvider } from 'react-router-dom';

function App() {

  return (
    <>
      <RouterProvider router={router} />
    </>
  )
}

export default App
