// src/pages/Login.jsx
import React from 'react';
import "../styles/Login.css";

function Login() {
  return (
    <div className="login-page">
      <div className="login-card">
        <h1 className="login-title">Iniciar Sesión</h1>

        <form className="login-form" noValidate>
          <div className="field">
            <label htmlFor="email">Email</label>
            <input
              id="email"
              type="email"
              name="email"
              placeholder="usuario@ejemplo.com"
              required
            />
          </div>

          <div className="field">
            <label htmlFor="password">Contraseña</label>
            <input
              id="password"
              type="password"
              name="password"
              placeholder="••••••••"
              required
            />
          </div>

          <button type="submit" className="btn-primary">
            Entrar
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;


