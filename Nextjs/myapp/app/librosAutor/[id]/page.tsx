"use client";
import { useEffect, useState } from "react";
import BotonRegresar from "../../components/BotonRegresar";

import Link from "next/link";
import { useRouter } from "next/router";
import { useParams } from "next/navigation";

export default function LibrosPorAutor() {
  const { id } = useParams(); // <-- obtiene autor_id de la URL
  const [libros, setLibros] = useState([]);
  const [loading, setLoading] = useState(true);


  useEffect(() => {
    const fetchLibros = async () => {
      try {
        const resp = await fetch(
          `http://localhost:8000/BuscarLibros/LibrosPorAutor/${id}`
        );

        if (!resp.ok) {
          throw new Error("No se pudieron cargar los libros");
        }

        const data = await resp.json();
        setLibros(data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchLibros();
  }, [id]);

  if (loading) return <p className="text-white p-10">Cargando...</p>;

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
    <div className="bg-slate-900 min-h-screen text-white p-10">
          <BotonRegresar />
      <h1 className="text-3xl font-bold mb-6">
        Libros del Autor #{id}, 
      </h1>

      {libros.length === 0 ? (
        <p className="text-gray-300">No hay libros registrados para este autor.</p>
      ) : (
        <ul className="space-y-4">
          {libros.map((libro) => (
            <li
              key={libro.id}
              className="bg-slate-800 p-4 rounded-xl shadow"
            >
              <h2 className="text-xl font-bold">{libro.titulo}</h2>
              <p className="opacity-80">ISBN: {libro.isbn}</p>
              <p className="opacity-80">Año: {libro.ano_publicacion}</p>
              <p><strong>Autores:</strong> {libro.autores.map(a => a.nombre).join(", ")}</p>

            </li>
          ))}
        </ul>
      )}
    </div>
    </div>
  );
}
