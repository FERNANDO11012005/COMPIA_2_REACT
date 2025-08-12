import React from 'react';
import { Routes, Route, useNavigate } from 'react-router-dom';

import Navbar from './components/Navbar';
import Home from './pages/Home';
import Contact from './pages/Contact';
import Login from './pages/Login';
import AdminLayout from './layouts/AdminLayout';

function App() {
  const navigate = useNavigate();

  const handleLogin = (isAuthenticated) => {
    if (isAuthenticated) {
      console.log("Usuario autenticado");
      navigate('/admin');
    }
  };

  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contacto" element={<Contact />} />
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
        <Route path="/admin" element={<AdminLayout />} />
      </Routes>
    </>
  );
}

export default App;

