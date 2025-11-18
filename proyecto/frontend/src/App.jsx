import { useState, useEffect } from "react";
import "./App.css";
import { obtenerUsuarios, registrarUsuario } from "./servicios/usuarioServicios";

function App() {
  const [usuarios, setUsuarios] = useState([]);
  const [nombre, setNombre] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    obtenerUsuarios().then(res => {
      // Ajusta al formato que devuelve tu backend
      setUsuarios(res.data); 
    });
  }, []);

  const enviar = (e) => {
    e.preventDefault(); // ← Importante para evitar recargar la página

    registrarUsuario({ nombre, password }).then(res => {
      const nuevo = res.data.usuario; // ← el usuario que devolvió FastAPI
      
      setUsuarios((prev) => [...prev, nuevo]); // ← lo agregas a la lista

      setNombre("");
      setPassword("");
    });
  };

  return (
    <div className="container">
      <h2> Registrarse </h2>

      <form className="formulario" onSubmit={enviar}>
        
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

        <button type="submit" className="btn">
          Guardar usuario
        </button>
        ¿Ya estas registrado(a)? 
        <a href="/login">Iniciar Sesión</a>
      </form>

      <h3>Usuarios registrados:</h3>
      <ul className="lista">
        {usuarios.map((u, i) => (
          <li key={i} className="item">id: {u.id}, {u.nombre} Contraseña {u.password}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
