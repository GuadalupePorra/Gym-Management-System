import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "./buscarSocio.css";

const BuscarSocio = () => {
  const [dni, setDni] = useState("");
  const [mensaje, setMensaje] = useState("");
  const navigate = useNavigate();

  const handleDniChange = (event) => {
    const value = event.target.value;
    if (/^\d{0,8}$/.test(value)) {
      setDni(value);
    }
  };

  const buscarSocio = async () => {
    try {
      const response = await axios.post("http://localhost:8000/socios/perfil/", { dni });
      if (response.status === 200) {
        navigate("/perfil", { state: { perfil: response.data } });
      } else {
        setMensaje("Socio no encontrado");
      }
    } catch (error) {
      console.error("Socio no encontrado", error);
      setMensaje("Hubo un error al buscar el socio.");
    }
  };

  return (
    <div className="container-fluid bg-lime min-vh-100 d-flex justify-content-center align-items-center">
      <div className="card text-center p-4 login-card">
        <h2 className="text-white mb-3">Ingreso socios</h2>
        <p className="text-white">Ingresa a tu perfil para gestionar tu reserva de clases</p>

        {/* Campo DNI */}
        <input
          type="text"
          className="form-control mb-3 text-center"
          placeholder="Ingrese su DNI"
          value={dni}
          onChange={handleDniChange}
          maxLength={8}
        />

        {/* Botón */}
        <button className="btn btn-lime fw-bold mb-3" onClick={buscarSocio}>
          Ingresar
        </button>

        {/* Mensaje */}
        {mensaje && <p className="text-danger">{mensaje}</p>}

        <p className="text-white fw-bold">Ingreso solo para socios del gimnasio</p>
      </div>
    </div>
  );
};

export default BuscarSocio;
