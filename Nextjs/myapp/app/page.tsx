"use client";
import Link from "next/link";
export default function Home() {
  return (
    <div className="bg-slate-500">
    <nav className="w-full bg-slate-700 text-white p-4 shadow-lg flex justify-between items-center">
    <Link href={"/"}><h1 className="text-2xl font-bold">Biblioteca Digital</h1></Link>
    <div className="space-x-4">
    <Link href={"/"}><button className="hover:underline">Inicio</button></Link>
    <Link href={"/todosLibros"}><button className="hover:underline">Libros</button></Link>
    <Link href={"/busqueda"}><button className="hover:underline">Busqueda</button></Link>
    </div>
    </nav>

    <div className="flex h-screen">
      {/* LADO IZQUIERDO */}
      <div className="flex-1 bg-slate-500 flex justify-center items-center h-[400px]">
          <Link href={"busqueda"}>
          <button className="
            px-6 py-3 bg-slate-700  rounded-lg shadow transition-transform duration-200
            hover:scale-105 hover:bg-slate-500 hover:shadow-lg
          ">
            <img src="/images/lupa2.png" className="h-[350px] w-[350px]" />
          </button>
          </Link> 
      </div>
      {/* LADO DERECHO */}
      <div className="flex-1 bg-slate-500 flex justify-center items-center h-[400px]">
          <Link href={"Agregar"}>
          <button className="
            px-6 py-3 bg-slate-700  rounded-lg shadow transition-transform duration-200
            hover:scale-105 hover:bg-slate-500 hover:shadow-lg
          ">
            <img src="/images/agregar.jpg" className="h-[350px] w-[350px]" />
          </button>
          </Link>
      </div>
    </div>
    
    </div>
  );
}