<template>
  <div class="md:flex md:items-center md:justify-between">
    <div class="min-w-0 flex-1">
      <h2 class="text-2xl/7 font-bold text-white sm:truncate sm:text-3xl sm:tracking-tight">Welcome back, Admin.</h2>
    </div>
  </div>

  <div class="bg-gray-800 mt-7">
    <div class="mx-auto max-w-7xl">
      <div class="grid grid-cols-1 gap-px bg-white/5 sm:grid-cols-2 lg:grid-cols-4">
        <div v-for="stat in stats" :key="stat.name" class="bg-gray-800 px-4 py-6 sm:px-6 lg:px-8">
          <p class="text-sm/6 font-medium text-gray-400">{{ stat.name }}</p>
          <p class="mt-2 flex items-baseline gap-x-2">
            <span class="text-4xl font-semibold tracking-tight text-white">{{ stat.value }}</span>
            <span v-if="stat.unit" class="text-sm text-gray-400">{{ stat.unit }}</span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const stats = [
  { name: 'Number of suites', value: '2' },
  { name: 'Average suite runtime', value: '3.65', unit: 'mins' },
  { name: 'Success rate', value: '98.5%' },
  { name: 'Currently running suites', value: '0' },
]
</script>
