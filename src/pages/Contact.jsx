// src/pages/Contact.jsx
import React from 'react';
import "../styles/Contact.css";

function Contact() {
  return (
    <div className="contact-page">
      <div className="contact-card">
        <h1 className="contact-title">Contáctanos</h1>
        <form className="contact-form" noValidate>
          <div className="field">
            <label htmlFor="name">Nombre</label>
            <input id="name" type="text" name="name" placeholder="Tu nombre" />
          </div>

          <div className="field">
            <label htmlFor="email">Email</label>
            <input id="email" type="email" name="email" placeholder="tu@ejemplo.com" />
          </div>

          <div className="field">
            <label htmlFor="message">Mensaje</label>
            <textarea id="message" name="message" placeholder="Escribe tu mensaje" rows="4" />
          </div>

          <button type="submit" className="btn-primary">
            Enviar
          </button>
        </form>
      </div>
    </div>
  );
}

export default Contact;

