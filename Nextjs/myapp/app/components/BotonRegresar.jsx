"use client";
import { useRouter } from "next/navigation";

export default function BotonRegresar() {
  const router = useRouter();

  return (
    <button
      onClick={() => router.back()}
      className="bg-slate-700 px-4 py-2 rounded-lg hover:bg-slate-800 transition"
    >
      ← Regresar
    </button>
  );
}
