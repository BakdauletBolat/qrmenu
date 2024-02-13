import axios from "axios";

export const instance = axios.create({
    baseURL: 'http://back.easymenu.kz/api',
    timeout: 10000,
  });