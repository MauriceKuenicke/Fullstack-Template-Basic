import axios from "axios"

const API = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_HOST,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json"
  },
  //withCredentials: true,
})

export default API
