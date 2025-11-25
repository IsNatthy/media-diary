import api from './axios';

export const getCatalog = async () => {
  const response = await api.get('/api/catalog/');
  return response.data;
};

export const getCatalogItem = async (id) => {
  const response = await api.get(`/api/catalog/${id}`);
  return response.data;
};
