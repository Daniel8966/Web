import axios from "axios";

const API_URL = "http://localhost:8000";

export const obtenerUsuarios = () => {
  return axios.get(`${API_URL}/usuarios`);
};

export const  registrarUsuario = (usuario ) => {
  return axios.post(`${API_URL}/usuarios`, usuario);
};


export const  login = (usuario ) => {
  return axios.post(`${API_URL}/usuarios/login`, usuario);
};

