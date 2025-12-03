import Link from "next/link";
export default function Home() {


  return (
    <div className="bg-slate-500">
    <div className=" fs-90px flex-col flex bg-slate-800 justify-center items-center h-[100px] text-white">
        <span>Bienvenido (a) a la Biblioteca Digital  </span>
        <span>    </span>
    </div >
    <div className="flex h-screen">
      {/* LADO IZQUIERDO */}
      <div className="flex-1 bg-slate-500 flex justify-center items-center h-[400px]">
        <Link href="busqueda">
          <button
            className="
              relative group
              px-6 py-3 bg-slate-700 rounded-lg shadow overflow-hidden
              transition-transform duration-200
              hover:scale-105 hover:bg-slate-500 hover:shadow-lg
            "
          >
            {/* Imagen (visible por defecto) */}
            <img
              src="/images/lupa2.png"
              className="
                h-[350px] w-[350px]
                transition-opacity duration-300
                group-hover:opacity-500
              "
            />

            {/* Texto (oculto por defecto, aparece en hover) */}
            <span
              className="
                absolute inset-0 flex items-center justify-center
                text-white text-2xl font-bold
                opacity-0 group-hover:opacity-100
                transition-opacity duration-300
              "
            >
              Buscar Libro 
            </span>
          </button>
        </Link>
      </div>
      {/* LADO DERECHO */}
      <div className="flex-1 bg-slate-500 flex justify-center items-center h-[400px]">
        <Link href={"/login"}>
          <button 
            className="
              relative group
              px-6 py-3 bg-slate-700 rounded-lg shadow overflow-hidden
              transition-transform duration-200
              hover:scale-105 hover:bg-slate-500 hover:shadow-lg
            "
          >
            {/* Imagen (visible por defecto) */}
            <img
              src="/images/agregar.jpg"
              className="
                h-[350px] w-[350px]
                transition-opacity duration-300
                group-hover:opacity-500
              "
            />

            {/* Texto (oculto por defecto, aparece en hover) */}
            <span
              className="
                absolute inset-0 flex items-center justify-center
                text-white text-2xl font-bold
                opacity-0 group-hover:opacity-100
                transition-opacity duration-300
              "
            >
              Agregar Libro
            </span>
          </button>
        </Link>
      </div>
    </div>
    
    </div>
  );
}