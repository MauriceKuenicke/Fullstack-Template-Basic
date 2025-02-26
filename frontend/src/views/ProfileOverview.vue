<template>
  <div>
    <div class="md:flex md:items-center md:justify-between">
      <div class="min-w-0 flex-1">
        <h2 class="text-2xl/7 font-bold text-white sm:truncate sm:text-3xl sm:tracking-tight">Profile</h2>
      </div>
    </div>
  <button type="button"
          @click="handleSignOut"
          class="rounded-md bg-orange-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-orange-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-orange-600">Sign Out</button>
  </div>
</template>
<script setup>
import {useAuthStore} from "@/stores/auth.js";
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

function handleSignOut() {
  authStore.signOut(router)
}

</script>
<style scoped>

</style>
