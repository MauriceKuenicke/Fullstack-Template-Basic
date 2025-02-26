<template>
  <div v-if="isAuthenticated">
    <TransitionRoot as="template" :show="sidebarOpen">
      <Dialog class="relative z-50 lg:hidden" @close="sidebarOpen = false">
        <TransitionChild as="template" enter="transition-opacity ease-linear duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="transition-opacity ease-linear duration-300" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-900/80" />
        </TransitionChild>

        <div class="fixed inset-0 flex">
          <TransitionChild as="template" enter="transition ease-in-out duration-300 transform" enter-from="-translate-x-full" enter-to="translate-x-0" leave="transition ease-in-out duration-300 transform" leave-from="translate-x-0" leave-to="-translate-x-full">
            <DialogPanel class="relative mr-16 flex w-full max-w-xs flex-1">
              <TransitionChild as="template" enter="ease-in-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in-out duration-300" leave-from="opacity-100" leave-to="opacity-0">
                <div class="absolute top-0 left-full flex w-16 justify-center pt-5">
                  <button type="button" class="-m-2.5 p-2.5" @click="sidebarOpen = false">
                    <span class="sr-only">Close sidebar</span>
                    <XMarkIcon class="size-6 text-white" aria-hidden="true" />
                  </button>
                </div>
              </TransitionChild>

              <div class="flex grow flex-col gap-y-5 overflow-y-auto bg-gray-900 px-6 pb-2 ring-1 ring-white/10">
                <IconLogo class="flex h-16 shrink-0 items-center mt-4"/>
                <nav class="flex flex-1 flex-col">
                  <ul role="list" class="flex flex-1 flex-col gap-y-7">
                    <li>
                      <ul role="list" class="-mx-2 space-y-1">
                        <li v-for="item in navigation" :key="item.name">
                          <router-link
                            :to="{ name: item.href }"
                            :class="[item.current ? 'bg-gray-800 text-white' : 'text-gray-400 hover:bg-gray-800 hover:text-white',
                            'group flex gap-x-3 rounded-md p-2 text-sm/6 font-semibold']">
                            <component :is="item.icon" class="size-6 shrink-0" aria-hidden="true" />
                            {{ item.name }}
                          </router-link>
                        </li>
                      </ul>
                    </li>

                    <li>
                      <div class="text-xs/6 font-semibold text-gray-400">Admin Panel</div>
                      <ul role="list" class="-mx-2 mt-2 space-y-1">
                        <li v-for="item in adminNav" :key="item.name">
                          <router-link
                            :to="{ name: item.href }"
                            :class="[item.current ? 'bg-gray-800 text-white' : 'text-gray-400 hover:bg-gray-800 hover:text-white',
                            'group flex gap-x-3 rounded-md p-2 text-sm/6 font-semibold']">
                            <component :is="item.icon" class="size-6 shrink-0" aria-hidden="true" />
                            {{ item.name }}
                          </router-link>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </nav>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- ######################## -->
    <!--  STATIC DESKTOP SIDEBAR  -->
    <!-- ######################## -->
    <div class="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-72 lg:flex-col">
      <div class="flex grow flex-col gap-y-5 overflow-y-auto bg-gray-900 px-6">
        <IconLogo class="flex h-16 shrink-0 items-center mt-4"/>
        <nav class="flex flex-1 flex-col">
          <ul role="list" class="flex flex-1 flex-col gap-y-7">
            <li>
              <ul role="list" class="-mx-2 space-y-1">
                <li v-for="item in navigation" :key="item.name">
                  <router-link
                    :to="{ name: item.href }"
                    :class="[item.current ? 'bg-gray-800 text-white' : 'text-gray-400 hover:bg-gray-800 hover:text-white',
                    'group flex gap-x-3 rounded-md p-2 text-sm/6 font-semibold']">
                    <component :is="item.icon" class="size-6 shrink-0" aria-hidden="true" />
                    {{ item.name }}
                  </router-link>
                </li>
              </ul>
            </li>

            <li>
              <div class="text-xs/6 font-semibold text-gray-400">Admin Panel</div>
              <ul role="list" class="-mx-2 mt-2 space-y-1">
                <li v-for="item in adminNav" :key="item.name">
                  <router-link
                    :to="{ name: item.href }"
                    :class="[item.current ? 'bg-gray-800 text-white' : 'text-gray-400 hover:bg-gray-800 hover:text-white',
                    'group flex gap-x-3 rounded-md p-2 text-sm/6 font-semibold']">
                    <component :is="item.icon" class="size-6 shrink-0" aria-hidden="true" />
                    {{ item.name }}
                  </router-link>
                </li>
              </ul>
            </li>


            <li class="-mx-6 mt-auto">
              <router-link
                :to="{name: 'profile-overview'}"
                class='text-xs font-medium text-gray-500 group-hover:text-gray-700'
              >
              <div class="flex items-center gap-x-4 px-6 py-3 text-sm/6 font-semibold text-white hover:bg-gray-800">
                  <div>
                    <span class="inline-flex size-9 items-center justify-center rounded-full bg-gray-500">
                      <span class="font-medium text-white">AA</span>
                    </span>
                  </div>
                  <div class="ml-3">
                    <p class="text-sm font-medium text-gray-100">Admin Admin</p>
                    <p class="text-xs font-normal text-gray-400">View Profile</p>
                  </div>
                </div>
              </router-link>
            </li>
          </ul>
        </nav>
      </div>
    </div>


    <!-- ######################## -->
    <!--      MOBILE HEADER       -->
    <!-- ######################## -->
    <div class="sticky top-0 z-40 flex items-center gap-x-6 bg-gray-900 px-4 py-4 shadow-xs sm:px-6 lg:hidden">
      <button type="button" class="-m-2.5 p-2.5 text-gray-400 lg:hidden" @click="sidebarOpen = true">
        <span class="sr-only">Open sidebar</span>
        <Bars3Icon class="size-6" aria-hidden="true" />
      </button>
      <div class="flex-1 text-sm/6 font-semibold text-white capitalize">{{currentRouteTitle}}</div>

      <router-link
        :to="{name: 'profile-overview'}"
      >
          <div>
            <span class="sr-only">Your Profile</span>
            <span class="inline-flex size-9 items-center justify-center rounded-full bg-gray-500">
              <span class="font-medium text-white">AA</span>
            </span>
          </div>
      </router-link>
    </div>

    <main class="py-10 lg:pl-72">
      <div class="px-4 sm:px-6 lg:px-8">
        <RouterView />
      </div>
    </main>
  </div>

  <!-- ###################### -->
  <!--  UNAUTHENTICATED VIEW  -->
  <!-- ###################### -->
  <div v-else>
    <RouterView />
  </div>
</template>

<script setup>
import { ref, watch, onMounted, computed } from 'vue'
import { RouterView } from 'vue-router'
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue'
import {
  Bars3Icon,
  KeyIcon,
  HomeIcon,
  XMarkIcon
} from '@heroicons/vue/24/outline'
import { useRoute } from 'vue-router'
import {useAuthStore} from "@/stores/auth.js";
import { storeToRefs } from 'pinia';
import IconLogo from "@/components/icons/IconLogo.vue";

const route = useRoute()
const authStore = useAuthStore()
const { isAuthenticated } = storeToRefs(authStore);
const navigation = ref([
  { name: 'Dashboard', href: 'dashboard', icon: HomeIcon, current: true },
])
const adminNav = ref([
  { name: 'User Management', href: 'user-management', icon: KeyIcon, current: false },
])

const sidebarOpen = ref(false)

const currentRouteTitle = computed(() => route.name)


// Derive current sidebar item based on route on mount
function updateCurrentRoute(currentRouteName) {
  navigation.value = navigation.value.map(item => ({
    ...item,
    current: item.href === currentRouteName
  }))

  adminNav.value = adminNav.value.map(item => ({
    ...item,
    current: item.href === currentRouteName
  }))
}

onMounted(() => {
  updateCurrentRoute(route.path)
})


// Watch route and update current sidebar item
watch(
  () => route.name,
  (newRouteName) => {
    updateCurrentRoute(newRouteName)
  }
)

</script>

