
import Link from 'next/link'
export default function LoginPage() {

  return (
    <div className="bg-slate-900"> 

    <div className='flex flex-col align-center justify-center min-h-screen'>
      <h1 className='flex align-center justify-center'>Formulario para la busqueda de libros </h1>
      <form className='flex align-center justify-center space-y-4'> 

        <input type='text' placeholder='Busqueda de Libros'/> 
      </form>

    </div>
  
    </div>
  );
}
