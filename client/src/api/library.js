import api from './axios';

export const getLibrary = async () => {
  const response = await api.get('/api/library/');
  return response.data;
};

export const addContent = async (contentData) => {
  const response = await api.post('/api/library/', contentData);
  return response.data;
};

export const updateContent = async (id, contentData) => {
  const response = await api.put(`/api/library/${id}`, contentData);
  return response.data;
};

export const deleteContent = async (id) => {
  const response = await api.delete(`/api/library/${id}`);
  return response.data;
};
