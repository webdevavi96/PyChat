import axios from 'axios';

const SERVER_URL = 'http://127.0.0.1:8000/auth/';

export const register = async (data) => {
  try {
    const res = await axios.post(`${SERVER_URL}register`, data, {
      headers: {
        'Content-Type': 'application/json',
      },
    });

    return res.data;
  } catch (error) {
    throw error.response?.data || error;
  }
};

export const verify_otp = async (otp) => {
  const email = sessionStorage.getItem('pending_email');

  if (!email) {
    throw new Error('Email not found for OTP verification');
  }

  const payload = {
    email,
    otp,
  };

  const res = await axios.post(`${SERVER_URL}verify_otp`, payload);
  return res;
};
export const login = async (data) => {
  try {
    const res = await axios.post(`${SERVER_URL}login`, { params: { data } });
    return res;
  } catch (error) {
    return error;
  }
};

export const getProfile = async (userId) => {
  try {
    const res = await axios.get(`${SERVER_URL}profile`, { params: { userId: userId } });
    return res;
  } catch (error) {
    return error;
  }
};
