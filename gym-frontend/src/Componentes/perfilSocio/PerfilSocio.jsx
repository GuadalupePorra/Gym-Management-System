import { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "axios";

const PerfilSocio = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { perfil } = location.state || {};
  const [mensaje, setMensaje] = useState("");
  const [perfilData, setPerfil] = useState(perfil || {});
  const [horarioSeleccionado, setHorarioSeleccionado] = useState({});
  const API = process.env.REACT_APP_API_URL;

  // --- Actualiza el perfil desde backend ---
  const actualizarPerfil = async () => {
    try {
      const res = await axios.post(`${API}/socios/perfil/`, {
        dni: perfilData.dni,
        
      });
      console.log("PerfilData:", perfilData);
      if (res.status === 200) {
        setPerfil(res.data);
      }
    } catch (error) {
      console.error("Error al actualizar perfil:", error);
    }
  };

  // --- Cargar perfil al montar ---
  useEffect(() => {
    if (perfilData.dni) {
      actualizarPerfil();
    } else {
      setMensaje("No se encontró el perfil del socio.");
    }
  }, [perfilData.dni]);

  // --- Inscribirse a clase ---
  const inscribirseClase = async (claseId, horarioId) => {
    try {
      const response = await axios.post(`${API}/clases/inscribirse/`, {
        dni: perfilData.dni,
        clase_id: claseId,
        horario_clase_id: horarioId,
      });

      if (response.status === 201) {
        alert("Inscripción exitosa");
        actualizarPerfil();
      }
    } catch (error) {
      alert(
        "No se pudo inscribir: " +
          (error.response?.data?.error || "Error desconocido")
      );
    }
  };

  // --- Darse de baja de clase ---
  const darseBajaClase = async (claseId, horarioId) => {
    try {
      const response = await axios.post(`${API}/clases/darse_baja/`, {
        dni: perfilData.dni,
        horario_clase_id: horarioId,
        // clase_id: claseId, // opcional si backend lo requiere
      });

      if (response.status === 200) {
        alert(response.data.mensaje || "Baja exitosa");
        actualizarPerfil();
      } else {
        alert(response.data.error || "Error al darse de baja");
      }
    } catch (error) {
      console.error("Error al darse de baja:", error.response?.data || error.message);
      alert(
        "Error al darse de baja: " +
          (error.response?.data?.error || error.message)
      );
    }
  };

  // --- Cerrar perfil (volver al inicio visualmente) ---
  const cerrarPerfil = () => {
    const seccionInicio = navigate("/");
    if (seccionInicio) {
      seccionInicio.scrollIntoView({ behavior: "smooth" });
    } else {
      navigate("/"); // fallback por si no existe el div
    }
  };

  // --- Clases disponibles filtradas ---
  const clasesDisponiblesFiltradas = (() => {
    if (!perfilData.horarios_disponibles) return [];

    const horariosTomados = new Set(
      (perfilData.horarios_inscritos || []).map((h) => h.horario_id)
    );

    const clasesMap = {};

    perfilData.horarios_disponibles.forEach((horario) => {
      if (horariosTomados.has(horario.horario_id)) return;

      const claseId = horario.clase_id;

      if (!clasesMap[claseId]) {
        clasesMap[claseId] = {
          id: claseId,
          nombre_clase: horario.nombre_clase,
          instructor: horario.instructor,
          horarios: [],
        };
      }

      clasesMap[claseId].horarios.push(horario);
    });

    return Object.values(clasesMap).filter((clase) => clase.horarios.length > 0);
  })();


  return (
    <div className="container my-4">
      <div className="text-end mb-3">
        <button className="btn btn-secondary" onClick={cerrarPerfil}>
          Cerrar perfil
        </button>
      </div>

      <h2 className="text-center mb-4">Perfil del Socio</h2>
      {mensaje && <p className="text-danger text-center">{mensaje}</p>}

      {perfilData && perfilData.dni ? (
        <>
          {/* Datos del socio */}
          <div className="card shadow mb-3">
            <div className="card-header bg-dark text-white">Datos del Socio</div>
            <div className="card-body">
              <p><strong>Socio:</strong> {perfilData.socio}</p>
              <p><strong>DNI:</strong> {perfilData.dni}</p>
              <p><strong>Clases restantes:</strong> {perfilData.dias_restantes}</p>
              <p><strong>Próxima fecha de pago:</strong> {perfilData.proxima_fecha_pago}</p>
            </div>
          </div>

          {/* Clases inscritas */}
          <div className="card shadow mb-3">
            <div className="card-header bg-dark text-white">Clases Inscritas</div>
            <div className="card-body">
              {perfilData.horarios_inscritos && perfilData.horarios_inscritos.length > 0 ? (
                perfilData.horarios_inscritos.map((clase) => (
                    <div key={`${clase.clase_id}-${clase.horario_id}`} className="mb-3 border-bottom pb-2">
                    <p><strong>{clase.nombre_clase}</strong> - Instructor: {clase.instructor}</p>
                    <p>Día: {clase.dia} - Hora: {clase.hora}</p>
                    <button
                        className="btn btn-danger btn-sm"
                        onClick={() => darseBajaClase(clase.clase_id, clase.horario_id)}
                    >
                        Darse de baja
                    </button>
                    </div>
                ))
              ) : (
                <p className="text-muted">No tienes clases inscritas actualmente.</p>
              )}
            </div>
          </div>

          {/* Clases disponibles */}
          <div className="card shadow mb-3">
            <div className="card-header bg-dark text-white">Clases Disponibles</div>
            <div className="card-body">
              {clasesDisponiblesFiltradas.length > 0 ? (
                clasesDisponiblesFiltradas.map((clase) => {
                  const horarioActivo =
                    clase.horarios.find(
                      (h) => h.horario_id === horarioSeleccionado[clase.id]
                    ) || clase.horarios[0];

                  return (
                    <div key={clase.id} className="mb-3 border-bottom pb-2">
                      <p><strong>{clase.nombre_clase}</strong> - Instructor: {clase.instructor}</p>
                      <p>Capacidad: {horarioActivo.capacidad_maxima}</p>
                      <p>
                        Lugares disponibles:{" "}
                        {horarioActivo.capacidad_maxima - horarioActivo.cantidad_inscriptos}
                      </p>
                      <div className="mb-2">
                        <label className="form-label">Seleccione un horario:</label>
                        <select
                          className="form-select"
                          onChange={(e) =>
                            setHorarioSeleccionado({
                              ...horarioSeleccionado,
                              [clase.id]: parseInt(e.target.value),
                            })
                          }
                        >
                          {clase.horarios.map((horario) => (
                            <option key={horario.horario_id} value={horario.horario_id}>
                              {horario.dia} - {horario.hora}
                            </option>
                          ))}
                        </select>
                      </div>
                      <button
                        className="btn btn-success btn-sm"
                        onClick={() =>
                          inscribirseClase(
                            clase.id,
                            horarioSeleccionado[clase.id] || clase.horarios[0].horario_id
                          )
                        }
                      >
                        Inscribirse
                      </button>
                    </div>
                  );
                })
              ) : (
                <p className="text-muted">No hay clases disponibles para inscribirse.</p>
              )}
            </div>
          </div>
        </>
      ) : null}
    </div>
  );
};

export default PerfilSocio;