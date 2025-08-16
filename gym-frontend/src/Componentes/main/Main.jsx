import { useEffect } from 'react';
import React from "react";
import './main.css' ;
import { useNavigate } from 'react-router-dom';

const Main = () => {
    const navigate = useNavigate();

    const handleButtonClick = () => {
        navigate('/buscar-socio'); // Navega a la página de BuscarSocio
    };

    useEffect(() => { 
        const cards = document.querySelectorAll('.membresia-card'); 
        const observer = new IntersectionObserver((entries) => { 
            entries.forEach(entry => { 
                if (entry.isIntersecting) { 
                    entry.target.classList.add('show'); 
                } 
            }); 
        }, { 
            threshold: 0.2 
            }); 
            cards.forEach(card => observer.observe(card)); return () => observer.disconnect(); }, [])

  return ( 
    <div className="main"> 
            <div className="insc_clases"> 
                <div className="text-center my-3" > 
                    <button type="button" className="btn btn-dark btn-lg px-2" onClick={handleButtonClick} id="inscrpcion" > Ingreso socios 
                    </button> 
                </div>
            </div> 
        <div className="clases" id="clases"> 
            <h2>NUESTRAS CLASES</h2> 
            <div className="slider-container"> 
                <div className="slider-track"> {/* Tarjetas duplicadas para efecto infinito */} {[...Array(2)].map((_, i) => ( <React.Fragment key={i}> 
                    <div className="card-custom"> <img src="./imagenes/funcional.jpg" alt="Funcional" /> 
                    <h5>Funcional</h5> 
                    <p>
                        Ejercicios variados que simulan movimientos cotidianos, mejoran la fuerza, estabilidad y coordinación general del cuerpo. 
                    </p> 
                    <a href="#" className="btn">
                        Conocer más
                    </a> 
                </div> 
                <div className="card-custom"> 
                    <img src="./imagenes/kick.jpg" alt="Kick Boxing" /> 
                    <h5>Kick Boxing</h5> 
                    <p>
                        Disciplina que combina golpes de puño y patadas. Mejora la resistencia, la fuerza, lacoordinación y libera el estrés. 
                    </p> 
                    <a href="#" className="btn">Conocer más</a> 
                </div> 
                <div className="card-custom"> 
                    <img src="./imagenes/spinning.jpg" alt="Spinning" /> 
                    <h5>Spinning</h5> 
                    <p>
                        Entrenamiento cardiovascular intenso en bicicleta fija, ideal para quemar calorias, mejorar la resistencia y tonificar piernas. 
                    </p> 
                    <a href="#" className="btn">Conocer más</a> 
                </div> 
                <div className="card-custom"> 
                    <img src="./imagenes/zumba.jpg" alt="Zumba" /> 
                    <h5>Zumba</h5> 
                    <p>
                        Clase de baile aeróbico con ritmos latinos. Divertida, dinamica y perfecta para quemar calorias sin dejar de moverte al ritmo de la música. 
                    </p> 
                    <a href="#" className="btn">Conocer más</a> 
                </div> 
                </React.Fragment> ))} 
                </div> 
                </div> 
                </div> 
                <div className="membresias-container" id="membresias"> 
                    <div className="membresias-info"> 
                        <h2>NUESTRAS MEMBRESIAS</h2> 
                        <p>Elegí la que mejor se adapte a vos!</p> 
                    </div> 
                    <div className="membresias-list"> 
                        <div className="membresia-card hidden"> 
                            <div className="card-inner"> 
                                <div className="card-front"> 
                                    <h5>MENSUAL</h5> 
                                </div> 
                            <div className="card-back"> 
                                <h6>Mensual</h6> 
                                <h4>$35.000</h4> 
                                <p>Acceso total al gimnasio durante 1 mes. Incluye clases y asesoría.</p> 
                            </div> 
                        </div>
                    </div> 
                    <div className="membresia-card hidden"> 
                        <div className="card-inner"> 
                            <div className="card-front"> 
                                <h5>TRIMESTRAL</h5> 
                            </div> 
                            <div className="card-back"> 
                                <h6>Trimestral</h6> 
                                <h4>$94.500</h4> 
                                <p>Acceso total al gimnasio durante 3 meses. Incluye clases y asesoría.</p> 
                            </div> 
                        </div> 
                    </div> 
                    <div className="membresia-card hidden"> 
                        <div className="card-inner"> 
                            <div className="card-front"> 
                                <h5>ANUAL</h5> 
                            </div> 
                            <div className="card-back"> 
                                <h6>Anual</h6> 
                                <h4>$357.000</h4> 
                                <p>Acceso total al gimnasio durante 1 año. Incluye clases y asesoría.</p> 
                            </div> 
                        </div> 
                    </div> 
                    <div className="membresia-card hidden"> 
                        <div className="card-inner"> 
                            <div className="card-front"> 
                                <h5>QUINCENAL</h5> 
                            </div> 
                            <div className="card-back"> 
                                <h6>Quincenal</h6> 
                                <h4>$18.000</h4> 
                                <p>Acceso total al gimnasio durante 15 dias. Incluye clases.</p> 
                            </div> 
                        </div> 
                    </div> 
                    <div className="membresia-card hidden"> 
                        <div className="card-inner"> 
                            <div className="card-front"> 
                                <h5>DIARIA</h5> 
                            </div>
                            <div className="card-back"> 
                                <h6>Pase diario</h6> 
                                <h4>$6.000</h4> 
                                <p>Acceso de un dia al gimnasio.</p> 
                            </div> 
                        </div> 
                    </div> 
                    </div> 
                    </div> 
                    </div> 
); }; export default Main;


