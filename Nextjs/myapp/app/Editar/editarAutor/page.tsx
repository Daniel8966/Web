"use client";
import Link from "next/link";
import React, { useState } from "react";


export default function AgregarAutor() {
  const [nombre, setNombre] = useState("");
  const [mensaje, setMensaje] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:8000/Autores/RegistrarAutor", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ nombre }),
      });

      if (!response.ok) {
        throw new Error("Error al registrar autor");
      }

      setMensaje("Autor registrado correctamente");
      setNombre("");
    } catch (error) {
      setMensaje("Ocurrió un error al registrar el autor");
    }
  };

  return (
    <div>
    <nav className="w-full bg-slate-700 text-white p-4 shadow-lg flex justify-between items-center">
    <Link href={"/"}><h1 className="text-2xl font-bold">Biblioteca Digital</h1></Link>
        <div className="space-x-4">
        <Link href={"/"}><button className="hover:underline">Inicio</button></Link>
        <Link href={"/todosLibros"}><button className="hover:underline">Libros</button></Link>
        <Link href={"/busqueda"}><button className="hover:underline">Busqueda</button></Link>
        </div>
    </nav>

    <div className="min-h-screen bg-slate-700 text-white flex flex-col items-center justify-center p-6">

      <div className="bg-slate-800 p-8 rounded-2xl shadow-xl w-full max-w-md">
        <h1 className="text-3xl font-bold text-center mb-6">Agregar Autor</h1>

        <form className="flex flex-col gap-4" onSubmit={handleSubmit}>
          <label className="text-lg font-semibold">Nombre del Autor</label>
          <input
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            placeholder="Ingresa el nombre"
            className="p-3 rounded bg-slate-600 text-white outline-none focus:ring-2 focus:ring-indigo-400"
            required
          />

          <button
            type="submit"
            className="w-full py-3 mt-4 bg-indigo-600 hover:bg-indigo-500 rounded-xl shadow-lg"
          >
            Agregar Autor
          </button>
        </form>

        {mensaje && (
          <p className="mt-4 text-center text-sm opacity-90">{mensaje}</p>
        )}
      </div>
    </div>
    </div>
  );
}