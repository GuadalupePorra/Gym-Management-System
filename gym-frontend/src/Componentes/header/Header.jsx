import React from "react";
import { Link } from "react-router-dom";
import './header.css' 
import p1Img from '../../assets/portada1.png';
import p2Img from '../../assets/portada2.png';
import p3Img from '../../assets/portada3.png';
const API = process.env.REACT_APP_ADMIN_URL;

const Header = () => {
    return ( <> {/* Navbar */} 
    <nav className="navbar navbar-expand-lg border-bottom border-body" data-bs-theme="dark"> 
        <div className="container-fluid"> 
            <Link className="nv_zeus" to="/">Zeus Gym</Link> {/* link al sitio principal*/} 
            <button className="navbar-toggler d-lg-none" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation"> 
                <span className="navbar-toggler-icon"></span> 
            </button> 
            <div className="collapse navbar-collapse" id="navbarScroll"> 
                <ul className="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style={{ "--bs-scroll-height": "100px" }}> 
                    <li className="nav-item"> 
                        <Link
                            to="/"
                            onClick={() => {
                                setTimeout(() => {
                                const el = document.getElementById("inicio");
                                if (el) el.scrollIntoView({ behavior: "smooth" });
                                }, 100);
                            }}
                            className="nav-link"
                            >
                            Inicio
                        </Link>
                    </li> 
                    <li className="nav-item"> 
                        <Link
                            to="/"
                            onClick={() => {
                                setTimeout(() => {
                                const el = document.getElementById("clases");
                                if (el) el.scrollIntoView({ behavior: "smooth" });
                                }, 100);
                            }}
                            className="nav-link"
                            >
                            Clases
                        </Link>
                    </li> 
                    <li className="nav-item"> 
                        <Link
                            to="/"
                            onClick={() => {
                                setTimeout(() => {
                                const el = document.getElementById("membresias");
                                if (el) el.scrollIntoView({ behavior: "smooth" });
                                }, 100);
                            }}
                            className="nav-link"
                            >
                            Membresias
                        </Link> 
                    </li> 
                    <li className="nav-item"> 
                        <Link
                            to="/"
                            onClick={() => {
                                setTimeout(() => {
                                const el = document.getElementById("inscrpcion");
                                if (el) el.scrollIntoView({ behavior: "smooth" });
                                }, 100);
                            }}
                            className="nav-link"
                            >
                            Acceso socios
                        </Link>
                    </li> 
                </ul> 
                <button className="btn btn-outline"> 
                    <a href={API} 
                    target="_blank" 
                    rel="noopener noreferrer">
                    Acceso administrativo
                    </a> 
                </button> 
            </div> 
        </div> 
    </nav> 
    <div id="inscrpcion" className='titulo' > 
        <h1 className="zeus" >Zeus Gym</h1> 
        <p className="zeus-desc">Un gimnasio hecho para vos</p> 
    </div> {/* Carrusel */} 
    <div  id="inicio"className="carousel slide carousel-fade" data-bs-ride="carousel" data-bs-interval="3000"> 
        <div className="carousel-inner"> 
            <div className="carousel-item active"> 
                <img src={p1Img}  className="d-block w-100 h-95" alt="First slide" style={{ height: '95vh', objectFit: 'fill' }}/> 
            </div> 
            <div className="carousel-item"> 
                <img src={p2Img} className="d-block w-100 h-95" alt = "Second slide" style={{ height: '95vh', objectFit: 'fill' }}></img> 
            </div> 
            <div className="carousel-item"> 
                <img src={p3Img} className="d-block w-100 h-95" alt = "Third slide" style={{ height: '95vh', objectFit: 'fill' }}></img> 
            </div> 
        </div> 
    </div> 
    </> ); };

export default Header;
