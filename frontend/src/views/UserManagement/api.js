import API from "@/api.js"

const UserAPI = {
  createNewUser(payload){
    return API.post(`user/create`, payload)
  },

  getAvailableUser(){
    return API.get(`user/list`)
  },

  getUserInfo(uuid){
    return API.get(`user/${uuid}/read`)
  }
}

export default UserAPI
