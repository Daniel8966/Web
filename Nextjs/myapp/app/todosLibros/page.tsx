
"use client";
import React, { useEffect, useState } from "react";
import Link from "next/link";
export default function ListaLibros() {
  const [libros, setLibros] = useState([]);

  // Cambia esta URL por la de tu API
  const API_URL = "http://localhost:8000/Libros/TodosLosLibros";

  useEffect(() => {
    const fetchLibros = async () => {
      try {
        const response = await fetch(API_URL);
        const data = await response.json();
        setLibros(data);
      } catch (error) {
        console.error("Error al cargar los libros:", error);
      }
    };

    fetchLibros();
  }, []);

  return (
    <div className="bg- slate-900">
      {/* Navbar */}
    <nav className="w-full bg-slate-700 text-white p-4 shadow-lg flex justify-between items-center">
    <Link href={"/"}><h1 className="text-2xl font-bold">Biblioteca Digital</h1></Link>
    <div className="space-x-4">
    <Link href={"/"}><button className="hover:underline">Inicio</button></Link>
    <Link href={"/todosLibros"}><button className="hover:underline">Libros</button></Link>
    <Link href={"/busqueda"}><button className="hover:underline">Busqueda</button></Link>
    </div>
    </nav>
    <div className="min-h-screen bg-slate-900 p-10">
      <h1 className="text-4xl font-bold text-center mb-10">Lista de Libros</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {libros.map((libro) => (
          <div
            key={libro.isbn}
            className="bg-slate-800 p-6 shadow rounded-xl flex flex-col gap-2"
          >
            <h2 className="text-xl font-bold">{libro.titulo}</h2>
            <p><strong>ISBN:</strong> {libro.isbn}</p>
            <p><strong>Año:</strong> {libro.ano_publicacion}</p>
            <p><strong>Páginas:</strong> {libro.paginas}</p>
            <p><strong>Precio:</strong> ${libro.precio}</p>
            <p><strong>Formato físico:</strong> {libro.formato ? "Sí" : "No"}</p>
            <p><strong>Editorial:</strong> {libro.editorial?.nombre} ({libro.editorial?.direccion})</p>
            <p><strong>Público objetivo:</strong> {libro.publico_objetivo?.descripcion}</p>
            <p><strong>Serie:</strong> {libro.serie?.numeroDeSerie} - {libro.serie?.descripcion_serie}</p>

            {/* Listas */}
            <p><strong>Autores:</strong> {libro.autores.map(a => a.nombre).join(", ")}</p>
            <p><strong>Categorías:</strong> {libro.categorias.map(c => c.descripcion).join(", ")}</p>
          </div>
        ))}
      </div>
    </div>
    </div>
  );
}
