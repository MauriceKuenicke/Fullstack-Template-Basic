<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8 pt-52">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <svg class="mx-auto w-auto" width="64" height="64" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient x1="0%" y1="100%" x2="50%" y2="0%" id="feature-1-a">
              <stop stop-color="#F9425F" stop-opacity=".8" offset="0%"/>
              <stop stop-color="#47A1F9" stop-opacity=".16" offset="100%"/>
            </linearGradient>
            <linearGradient x1="50%" y1="100%" x2="50%" y2="0%" id="feature-1-b">
              <stop stop-color="#FDFFDA" offset="0%"/>
              <stop stop-color="#F97059" stop-opacity=".798" offset="49.935%"/>
              <stop stop-color="#F9425F" stop-opacity="0" offset="100%"/>
            </linearGradient>
          </defs>
          <g fill="none" fill-rule="evenodd">
            <path d="M24 48H0V24C0 10.745 10.745 0 24 0h24v24c0 13.255-10.745 24-24 24" fill="url(#feature-1-a)"/>
            <path d="M40 64H16V40c0-13.255 10.745-24 24-24h24v24c0 13.255-10.745 24-24 24" fill="url(#feature-1-b)"/>
          </g>
        </svg>
      <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-white">EchoSphere</h2>
      <p class="mt-2 text-center text-sm/6 text-white">Sign in with your user</p>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" action="#" method="POST">
        <div>
          <label for="username" class="block text-sm/6 font-medium text-white">Username</label>
          <div class="mt-2">
            <input type="text" name="username" id="username"
                   v-model="username"
                   class="block w-full rounded-md bg-white/5 px-3 py-1.5 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-orange-500 sm:text-sm/6" />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm/6 font-medium text-white">Password</label>
          </div>
          <div class="mt-2">
            <input type="password" name="password" id="password" autocomplete="current-password"
                   v-model="password"
                   class="block w-full rounded-md bg-white/5 px-3 py-1.5 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-orange-500 sm:text-sm/6" />
          </div>
        </div>

        <div>
          <div v-if="!buttonIsSubmittable"
                  class="flex w-full justify-center rounded-md bg-gray-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-orange-500">Sign in
          </div>
          <button type="submit"
                  v-else
                  @click.prevent="handleSubmit"
                  class="flex w-full justify-center rounded-md bg-orange-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-orange-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-orange-500">Sign in
          </button>
        </div>
      </form>

      <div class="rounded-md bg-red-200 p-4 mt-5" v-if="showError">
        <div class="flex">
          <div class="shrink-0">
            <ExclamationCircleIcon class="size-5 text-red-400" aria-hidden="true" />
          </div>
          <div class="ml-3">
            <p class="text-sm font-medium text-red-800">{{errorMsg}}</p>
          </div>
          <div class="ml-auto pl-3">
            <div class="-mx-1.5 -my-1.5">
              <button type="button"
                      class="inline-flex rounded-md bg-red-200 p-1.5 text-red-500 hover:bg-red-300 focus:ring-2 focus:ring-red-600 focus:ring-offset-2 focus:ring-offset-red-200 focus:outline-hidden">
                <span class="sr-only">Dismiss</span>
                <XMarkIcon class="size-5" aria-hidden="true" @click="showError = false"/>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { XMarkIcon, ExclamationCircleIcon } from '@heroicons/vue/20/solid'
import { ref, computed } from "vue"
import {useAuthStore} from "@/stores/auth.js";
import { useRouter } from 'vue-router'

const username = ref("admin")
const password = ref("admin")

const authStore = useAuthStore()
const router = useRouter()

const buttonIsSubmittable = computed(() => {
  return username.value.length > 0 && password.value.length > 0
})

function handleSubmit(_) {
  if (!buttonIsSubmittable.value) {
    return
  }
  showError.value = false
  if (username.value === "admin" && password.value === "admin") {
    authStore.authenticateUser(router)
  } else {
    errorMsg.value = "Invalid username or password"
    showError.value = true
  }
}

const showError = ref(false)
const errorMsg = ref("")

</script>
