"use client";
import React, { useEffect, useState } from "react";
import Link from "next/link";

export default function ListaAutores() {
  const [autores, setAutores] = useState([]);

  const API_URL = "http://localhost:8000/PublicoObjetivo/TodosLosPublicoes";

  const eliminarPublico = async (idPublico: number) => {
    try {
      const response = await fetch(
        `http://localhost:8000/PublicoObjetivo/BorrarPublico/${idPublico}`,
        { method: "DELETE" }


      );

      if (!response.ok) {
        throw new Error("Error al eliminar al publico ");
      }
      window.location.reload();

    } catch (error) {
      console.error(error);
      alert("No se pudo eliminar al publico");
    }
  };

  useEffect(() => {
    const fetchAutores = async () => {
      try {
        const response = await fetch(API_URL);
        const data = await response.json();
        setAutores(data);
      } catch (error) {
        console.error("Error al cargar los autores:", error);
      }
    };

    fetchAutores();
  }, []);

  return (
    <div className="bg-slate-900 min-h-screen text-white">
      {/* Navbar */}
      <nav className="w-full bg-slate-700 text-white p-4 shadow-lg flex justify-between items-center">
        <Link href={"/"}>
          <h1 className="text-2xl font-bold cursor-pointer">
            Biblioteca Digital
          </h1>
        </Link>

        <div className="space-x-4">
          <Link href={"/"}>
            <button className="hover:underline">Inicio</button>
          </Link>
          <Link href={"/todosLibros"}>
            <button className="hover:underline">Libros</button>
          </Link>
          <Link href={"/busqueda"}>
            <button className="hover:underline">Busqueda</button>
          </Link>
        </div>
      </nav>

      {/* Contenido */}
      <div className="p-10">
        <h1 className="text-4xl font-bold text-center mb-10">
          Lista de Publicos Objetivos
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {autores.map((autor) => (
            <div
              key={autor.id}
              className="bg-slate-800 p-6 shadow rounded-xl flex flex-col gap-2"
            >

            <p><strong>Descripcion:</strong> {autor.descripcion}</p>
              <div className="flex gap-4  justify-between mt-4">
                <button className="bg-blue-600 px-3 py-1 rounded hover:bg-blue-700">
                  Editar
                </button>
                <Link href={`/librosPublico/${autor.id}`}>
                  <button className="bg-green-800 px-3 py-1 rounded hover:bg-green-950">
                    Consultar Libros
                  </button>
                </Link>
                <button onClick={()=> eliminarPublico(autor.id)} className="bg-red-600 px-3 py-1 rounded hover:bg-red-700">
                  Eliminar
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
