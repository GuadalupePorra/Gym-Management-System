import React, {useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Agregar Router y Routes
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import Header from './Componentes/header/Header.jsx';
import Main from './Componentes/main/Main.jsx';
import Footer from './Componentes/footer/Footer.jsx';
import BuscarSocio from './Componentes/buscarSocio/buscarSocio.jsx';
import PerfilSocio from './Componentes/perfilSocio/PerfilSocio.jsx';




function App() {
  const [data, setData] = useState(null);
  return (
    <Router> 
      <div className="App">
        {/* Header y Footer */}
        <Header />
        
        <Routes>
          {/* Ruta principal con Main */}
          <Route path="/" element={<Main />} />

          {/* Ruta para BuscarSocio */}
          <Route path="/buscar-socio" element={<BuscarSocio />} />
          <Route path="/perfil" element={<PerfilSocio />} />
        </Routes>
        
        <Footer />
      </div>
  </Router>
  );
}

export default App;
