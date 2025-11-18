import { useState } from "react";
import { login } from "./servicios/usuarioServicios";

function Login() {
  const [nombre, setNombre] = useState("");
  const [password, setPassword] = useState("");
  const [mensaje, setMensaje] = useState("");

  const iniciarSesion = (e) => {
    e.preventDefault();

    login({ nombre, password })
      .then(res => {
        window.location.href = "https://search.brave.com/images?q=gatitos";

      })
      .catch(err => {
        if (err.response && err.response.status === 404) {
          setMensaje("Credenciales incorrectas");
        } else {
          setMensaje("Error de servidor Usuario no encontrado");
        }
      });
  };

  return (
    <div className="container">
      <h2>Iniciar Sesión</h2>

      <form className="formulario" onSubmit={iniciarSesion}>
        <input
          type="text"
          placeholder="Nombre"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
          className="input"
        />

        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="input"
        />

        <button type="submit" className="btn">Entrar</button>
      </form>

      {mensaje && <p>{mensaje}</p>}

      <p>¿No tienes cuenta?</p>
      <a href="/">Registrarse</a>
    </div>
  );
}

export default Login;
