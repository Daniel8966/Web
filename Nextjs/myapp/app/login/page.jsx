
import Link from 'next/link'
export default function LoginPage() {

  return (
    <div className="bg-slate-900"> 
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold">Iniciar Sesión</h1>
      <span>Solo los bibliotecarios pueden ingresar libros</span>

      <form className="flex flex-col mt-6 space-y-4 w-80">
        <input
          className="border p-2 rounded"
          type="text"
          placeholder="Numero de Trabajador"
        />
        <input
          className="border p-2 rounded"
          type="password"
          placeholder="Contraseña"
        />
        <button className="bg-blue-600 text-white p-2 rounded hover:bg-blue-500">
          Entrar
        </button> 
        <Link className="flex items-center justify-center 
        bg-blue-600 text-white p-2 rounded hover:bg-blue-500" href={"/"}>
          <button   >
            Regresar
          </button>
        </Link>

      </form>
    </div>
    </div>
  );
}
