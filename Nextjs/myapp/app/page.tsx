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
          <button className="
            px-6 py-3 bg-slate-700  rounded-lg shadow transition-transform duration-200
            hover:scale-105 hover:bg-slate-500 hover:shadow-lg
          ">
            <img src="/images/lupa2.png" className="h-[350px] w-[350px]" />
          </button>
      </div>
      {/* LADO DERECHO */}
      <div className="flex-1 bg-slate-500 flex justify-center items-center h-[400px]">
          <button className="
            px-6 py-3 bg-slate-700  rounded-lg shadow transition-transform duration-200
            hover:scale-105 hover:bg-slate-500 hover:shadow-lg
          ">
            <img src="/images/agregar.jpg" className="h-[350px] w-[350px]" />
          </button>
      </div>
    </div>
    
    </div>
  );
}