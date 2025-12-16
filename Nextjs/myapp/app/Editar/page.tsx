import React from "react";
import Link from "next/link";

import BotonRegresar from "../components/BotonRegresar";

export default function SixButtonsPage() {
  return (
    <div>
              {/* Navbar */}
      <nav className="w-full bg-slate-700 text-white p-4 shadow-lg flex justify-between items-center">
              <BotonRegresar/>
        <Link href={"/"}>
          <h1 className="text-2xl font-bold">Biblioteca Digital</h1>
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

    <main className="min-h-screen bg-slate-500 text-white flex items-center justify-center p-6">
        
      <div className="w-full max-w-4xl">
        <header className="mb-8 text-center">
          <h1 className="text-3xl font-semibold mb-2">Que deseas Agregar</h1>
        </header>

        <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <Link href="Agregar/agregarCategoria" className="block text-center p-6 bg-slate-600 hover:bg-slate-500 rounded-2xl shadow transition">
             Categoría
          </Link>

          <Link href="Agregar/agregarEditorial" className="block text-center p-6 bg-slate-600 hover:bg-slate-500 rounded-2xl shadow transition">
             Editorial
          </Link>

          <Link href="Agregar/agregarLibro" className="block text-center p-6 bg-slate-600 hover:bg-slate-500 rounded-2xl shadow transition">
             Libro
          </Link>

          <Link href="Agregar/agregarPublico" className="block text-center p-6 bg-slate-600 hover:bg-slate-500 rounded-2xl shadow transition">
             Público
          </Link>

          <Link href="Agregar/agregarSerie" className="block text-center p-6 bg-slate-600 hover:bg-slate-500 rounded-2xl shadow transition">
             Serie
          </Link>

          <Link href="Agregar/agregarAutor" className="block text-center p-6 bg-slate-600 hover:bg-slate-500 rounded-2xl shadow transition">
             Autor
          </Link>
        </section>
      </div>
    </main>
    </div>
  );
}
