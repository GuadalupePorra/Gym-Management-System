// src/Componentes/Footer/Footer.jsx
import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import { FaFacebook, FaInstagram } from "react-icons/fa";
import "./footer.css"; // para estilos adicionales

const Footer = () => {
  return (
    <footer>
      {/* Franja blanca superior */}
      <div className="footer-white"></div>

      {/* Bloque oscuro */}
      <div className="footer-dark text-center text-light py-4">
        <h5 className="mb-3">Zeus Gym</h5>

        {/* Íconos redes */}
        <div className="mb-3">
          <a href="https://facebook.com" className="text-light mx-2" target="_blank" rel="noreferrer">
            <FaFacebook size={24} />
          </a>
          <a href="https://instagram.com" className="text-light mx-2" target="_blank" rel="noreferrer">
            <FaInstagram size={24} />
          </a>
        </div>

        {/* Copyright */}
        <p className="mb-0">© Guadalupe Porra. 2025</p>
      </div>
    </footer>
  );
};

export default Footer;
