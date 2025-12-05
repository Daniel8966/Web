"use client";
import React, { useEffect, useState } from "react";
import Link from "next/link";

export default function ListaCategorias() {
  const [categorias, setCategorias] = useState([]);

  const API_URL = "http://localhost:8000/Categoria/TodosLosCategoriaes";

  useEffect(() => {
    const fetchCategorias = async () => {
      try {
        const response = await fetch(API_URL);
        const data = await response.json();
        
        console.log("DATA RECIBIDA:", data);
        setCategorias(data); // <-- data es un arreglo, está bien
      } catch (error) {
        console.error("Error al cargar las categorías:", error);
      }
    };

    fetchCategorias();
  }, []);

  return (
    <div className="bg-slate-900 min-h-screen text-white">

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

      <div className="p-10">
        <h1 className="text-4xl font-bold text-center mb-10">
          Lista de Categorías
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {categorias.map((categoria) => (
            <div
              key={categoria.id}
              className="bg-slate-800 p-6 shadow rounded-xl flex flex-col gap-2"
            >
              <h2 className="text-xl font-bold">{categoria.descripcion}</h2>

              <div className="flex gap-4 justify-between mt-4">
                <button className="bg-blue-600 px-3 py-1 rounded hover:bg-blue-700">
                  Editar
                </button>
                <button className="bg-green-800 px-3 py-1 rounded hover:bg-green-950">
                  Consultar Libros
                </button>
                <button className="bg-red-600 px-3 py-1 rounded hover:bg-red-700">
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
