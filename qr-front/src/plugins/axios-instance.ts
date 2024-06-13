import axios from "axios";

export const instance = axios.create({
    baseURL: 'http://localhost:8000/api',
    timeout: 10000,
  });


  instance.interceptors.request.use(function (config) {
    if (localStorage.getItem('token') != null) {
      config.headers['Authorization'] = "Bearer "+localStorage.getItem('token');
    }

    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });