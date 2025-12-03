export async function GET() {
  // Aquí tu servidor Node (Next.js) llama a FastAPI
  const res = await fetch("http://localhost:8000/api/data");

  const data = await res.json();

  let json = {
    "waos" : 1  , 
    "data" : data
  }
  
  // Devuelve la respuesta al frontend de React
  return Response.json(json);
}