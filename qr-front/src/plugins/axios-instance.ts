import axios from "axios";

export const instance = axios.create({
    baseURL: 'https://back.easymenu.kz/api',
    timeout: 10000,
  });


  instance.interceptors.request.use(function (config) {
    config.headers['Authorization'] = "Bearer "+localStorage.getItem('token');
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });