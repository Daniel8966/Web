import React from "react";
import Link from "next/link";

export default function Biblioteca() {
  return (
    <div className="min-h-screen bg-slate-700">
      {/* Navbar */}
    <nav className="w-full bg-slate-700 text-white p-4 shadow-lg flex justify-between items-center">
    <Link href={"/"}><h1 className="text-2xl font-bold">Biblioteca Digital</h1></Link>
        <div className="space-x-4">
        <Link href={"/"}><button className="hover:underline">Inicio</button></Link>
        <Link href={"/todosLibros"}><button className="hover:underline">Libros</button></Link>
        <Link href={"/busqueda"}><button className="hover:underline">Busqueda</button></Link>
        </div>
    </nav>

      {/* Contenido */}
      <div className="flex flex-col items-center justify-center py-20 px-4 text-center">
        <h2 className="text-4xl font-bold mb-10">
          Bienvenido a la Biblioteca Digital
        </h2>
        <Link href={"todosLibros"}>
            <button className="bg-slate-500 text-white py-3 rounded-xl hover:bg-slate-800 shadow">
                mostrar todos los libros
            </button>
        </Link>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-20 w-full max-w-xl">
        <div className="bg-slate-500 text-white py-3 rounded-xl hover:bg-slate-800 shadow hover:bg-slate-700" >
          <Link href={"/busqueda/autores"}  >
            <button >
              Mostrar Todos los autores 
            </button>
          </Link>
        </div>

        <div className="bg-slate-500 text-white py-3 rounded-xl hover:bg-slate-800 shadow hover:bg-slate-700" >
          <Link href={"/busqueda/categorias"}  >
            <button >
              Mostrar Todas Las categorias 
            </button>
          </Link>
        </div>
                <div className="bg-slate-500 text-white py-3 rounded-xl hover:bg-slate-800 shadow hover:bg-slate-700" >
          <Link href={"/busqueda/series"}  >
            <button >
              Mostrar Todas Las Series 
            </button>
          </Link>
        </div>

                <div className="bg-slate-500 text-white py-3 rounded-xl hover:bg-slate-800 shadow hover:bg-slate-700" >
          <Link href={"/busqueda/publicos"}  >
            <button >
              Mostrar Publico Objetivo
            </button>
          </Link>
        </div>
        

        </div>
      </div>
    </div>
  );
}
