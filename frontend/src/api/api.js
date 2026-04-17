import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

// ── HCP APIs ────────────────────────────────────────────────
export const getAllHCPs = async () => {
  const response = await axios.get(`${BASE_URL}/hcp/`);
  return response.data;
};

export const createHCP = async (data) => {
  const response = await axios.post(`${BASE_URL}/hcp/`, data);
  return response.data;
};

// ── Interaction APIs ────────────────────────────────────────
export const logInteraction = async (data) => {
  const response = await axios.post(`${BASE_URL}/interaction/log`, data);
  return response.data;
};

export const editInteraction = async (id, data) => {
  const response = await axios.put(`${BASE_URL}/interaction/edit/${id}`, data);
  return response.data;
};

export const getHCPHistory = async (hcp_id) => {
  const response = await axios.get(`${BASE_URL}/interaction/history/${hcp_id}`);
  return response.data;
};

export const suggestFollowup = async (data) => {
  const response = await axios.post(`${BASE_URL}/interaction/suggest-followup`, data);
  return response.data;
};

export const analyzeSentiment = async (data) => {
  const response = await axios.post(`${BASE_URL}/interaction/analyze-sentiment`, data);
  return response.data;
};

export const sendChatMessage = async (data) => {
  const response = await axios.post(`${BASE_URL}/interaction/chat`, data);
  return response.data;
};