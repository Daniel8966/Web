"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";

export default function AgregarLibro() {
  // Campos del libro
  const [isbn, setIsbn] = useState("");
  const [titulo, setTitulo] = useState("");
  const [anoPublicacion, setAnoPublicacion] = useState("");
  const [paginas, setPaginas] = useState("");
  const [precio, setPrecio] = useState("");
  const [formato, setFormato] = useState(true); // true/false

  // Selects data
  const [autores, setAutores] = useState([]);
  const [editoriales, setEditoriales] = useState([]);
  const [publicos, setPublicos] = useState([]);
  const [series, setSeries] = useState([]);
  const [categorias, setCategorias] = useState([]);
  const [autorIds, setAutorIds] = useState([]);
  const [categoriaIds, setCategoriaIds] = useState([]);

  
  // Selected ids
  const [autorId, setAutorId] = useState("");
  const [editorialId, setEditorialId] = useState("");
  const [publicoId, setPublicoId] = useState("");
  const [serieId, setSerieId] = useState("");
  const [categoriaId, setCategoriaId] = useState("");

  const [mensaje, setMensaje] = useState(null);
  const [cargando, setCargando] = useState(false);


  useEffect(() => {
    const loadData = async () => {
      try {
        const endpoints = [
          { url: "/Autores/TodosLosAutores", setter: setAutores },
          { url: "/Editorial/TodosLoseditoriales", setter: setEditoriales },
          { url: "/PublicoObjetivo/TodosLosPublicoes", setter: setPublicos },
          { url: "/Serie/TodosLosSeriees", setter: setSeries },
          { url: "/Categoria/TodosLosCategoriaes", setter: setCategorias },
        ];

        for (const { url, setter } of endpoints) {
          const resp = await fetch(`http://localhost:8000${url}`);
          if (!resp.ok) {
            console.error("Error cargando", url);
            setter([]);
            continue;
          }
          const data = await resp.json();
          setter(Array.isArray(data) ? data : []);
        }
      } catch (err) {
        console.error(err);
      }
    };

    loadData();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validaciones simples
    if (!isbn || !titulo) {
      setMensaje("ISBN y Título son obligatorios");
      return;
    }

const payload = {
  isbn: String(isbn),
  titulo: String(titulo),
  ano_publicacion: String(anoPublicacion),
  paginas: Number(paginas),
  precio: Number(precio),
  formato: Boolean(formato),

  editorial_id: editorialId ? Number(editorialId) : null,
  publico_objetivo_id: publicoId ? Number(publicoId) : null,
  serie_id: serieId ? Number(serieId) : null,

  autores_ids: autorIds,          
  categorias_ids: categoriaIds  
};
    try {
      setCargando(true);
      const response = await fetch("http://localhost:8000/Libros/RegistrarLibro", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        const text = await response.text();
        throw new Error(text || "Error al registrar libro");
      }

      setMensaje("Libro registrado correctamente ✔");
      // limpiar formulario opcional
      setIsbn("");
      setTitulo("");
      setAnoPublicacion("");
      setPaginas("");
      setPrecio("");
      setFormato(true);
      setAutorId("");
      setEditorialId("");
      setPublicoId("");
      setSerieId("");
      setCategoriaId("");
    } catch (err) {
      console.error(err);
      setMensaje("Error al registrar libro: " + (err.message || ""));
    } finally {
      setCargando(false);
    }
  };

  return (
    <div>
      <nav className="w-full bg-slate-700 text-white p-4 shadow-lg flex justify-between items-center">
        <Link href={"/"}>
          <h1 className="text-2xl font-bold">Biblioteca Digital</h1>
        </Link>

        <div className="space-x-4">
          <Link href={"/"}><button className="hover:underline">Inicio</button></Link>
          <Link href={"/todosLibros"}><button className="hover:underline">Libros</button></Link>
        </div>
      </nav>

      <div className="min-h-screen bg-slate-700 text-white flex flex-col items-center justify-center p-6">
        <div className="bg-slate-800 p-8 rounded-2xl shadow-xl w-full max-w-lg">
          <h1 className="text-3xl font-bold text-center mb-6">Agregar Libro</h1>

          <form className="flex flex-col gap-4" onSubmit={handleSubmit}>
            {/* Campos básicos (agregados) */}
            <label className="font-semibold">ISBN</label>
            <input
              className="p-3 bg-slate-600 rounded"
              placeholder="ISBN"
              value={isbn}
              onChange={(e) => setIsbn(e.target.value)}
              required
            />

            <label className="font-semibold">Título</label>
            <input
              className="p-3 bg-slate-600 rounded"
              placeholder="Título"
              value={titulo}
              onChange={(e) => setTitulo(e.target.value)}
              required
            />

            <label className="font-semibold">Año de publicación</label>
            <input
              className="p-3 bg-slate-600 rounded"
              placeholder="2023"
              value={anoPublicacion}
              onChange={(e) => setAnoPublicacion(e.target.value)}
            />

            <label className="font-semibold">Páginas</label>
            <input
              type="number"
              min="0"
              className="p-3 bg-slate-600 rounded"
              placeholder="0"
              value={paginas}
              onChange={(e) => setPaginas(e.target.value)}
            />

            <label className="font-semibold">Precio</label>
            <input
              type="number"
              step="0.01"
              min="0"
              className="p-3 bg-slate-600 rounded"
              placeholder="0.00"
              value={precio}
              onChange={(e) => setPrecio(e.target.value)}
            />

            <label className="flex items-center gap-2">
              <input
                type="checkbox"
                checked={formato}
                onChange={(e) => setFormato(e.target.checked)}
              />
              <span className="font-semibold">Formato (true = físico, false = digital)</span>
            </label>

            <select
              
              className="p-3 bg-slate-600 rounded"
              value={autorIds}
              onChange={(e) =>
                setAutorIds(
                  Array.from(e.target.selectedOptions, o => Number(o.value))
                )
              }
            > <option value="">Seleccione Autor</option>

              {autores.map(a => (
                <option key={a.id} value={a.id}>{a.nombre}</option>
              ))}
            </select>

            <select className="p-3 bg-slate-600 rounded" value={editorialId} onChange={(e) => setEditorialId(e.target.value)}>
              <option value="">Seleccione Editorial</option>
              {editoriales.map((ed) => (
                <option key={ed.id} value={ed.id}>{ed.nombre}</option>
              ))}
            </select>

            <select className="p-3 bg-slate-600 rounded" value={publicoId} onChange={(e) => setPublicoId(e.target.value)}>
              <option value="">Seleccione Público Objetivo</option>
              {publicos.map((p) => (
                <option key={p.id} value={p.id}>{p.descripcion}</option>
              ))}
            </select>

            <select className="p-3 bg-slate-600 rounded" value={serieId} onChange={(e) => setSerieId(e.target.value)}>
              <option value="">Seleccione Serie</option>
              {series.map((s) => (
                <option key={s.id} value={s.id}>{s.descripcion_serie}</option>
              ))}
            </select>

              <select
            
                className="p-3 bg-slate-600 rounded"
                value={categoriaIds}
                onChange={(e) =>
                  setCategoriaIds(
                    Array.from(e.target.selectedOptions, o => Number(o.value))
                  )
                }
              ><option value="">Seleccione Categoria</option>

                {categorias.map(c => (
                  <option key={c.id} value={c.id}>{c.descripcion}</option>
                ))}
              </select>

            <button
              type="submit"
              className="w-full py-3 mt-4 bg-indigo-600 hover:bg-indigo-500 rounded-xl shadow-lg"
              disabled={cargando}
            >
              {cargando ? "Registrando..." : "Registrar Libro"}
            </button>
          </form>

          {mensaje && <p className="mt-4 text-center opacity-90">{mensaje}</p>}
        </div>
      </div>
    </div>
  );
}
