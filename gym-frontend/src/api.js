import axios from 'axios';

// Configura la instancia de axios con la URL base de tu backend si no usas el proxy
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000'  // Ajusta la URL según tu backend
});

export const fetchData = async () => {
  try {
    const response = await api.get('/endpoint/');
    return response.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};
