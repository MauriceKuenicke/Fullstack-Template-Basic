import { ref } from 'vue'
import { defineStore } from 'pinia'


export const useAuthStore = defineStore('auth', () => {
  const authToken = ref(localStorage.getItem('authToken'))
  const isAuthenticated = ref(!!authToken.value)

  function authenticateUser(router) {
    const newToken = '<RANDOM_TOKEN>'
    authToken.value = newToken
    isAuthenticated.value = !!newToken

    if (newToken) {
      localStorage.setItem('authToken', newToken)
    } else {
      localStorage.removeItem('authToken')
    }

    router.push({
      name: 'dashboard'
    })
  }

  function signOut(router) {
    isAuthenticated.value = false
    authToken.value = null
    localStorage.removeItem('authToken')
    router.push({
      name: 'signin'
    })
  }

  return { isAuthenticated, authToken, authenticateUser, signOut }
})
