import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'
import LoginView from '../views/LoginView.vue'
import UserManagementOverview from "@/views/UserManagement/UserManagementOverview.vue";
import ProfileOverview from "@/views/ProfileOverview.vue";
import NotFound404 from "@/views/NotFound404.vue";
import {useAuthStore} from "@/stores/auth.js";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/signin',
      name: 'signin',
      component: LoginView,
    },
    {
      path: '/',
      name: 'dashboard',
      component: DashboardView,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/user-management',
      name: 'user-management',
      component: UserManagementOverview,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/profile',
      name: 'profile-overview',
      component: ProfileOverview,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: "/:catchAll(.*)",
      name: "404NotFound",
      component: NotFound404
    }
  ],
})

router.beforeEach(async (to, _, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const authStore = useAuthStore()
    if (!authStore.isAuthenticated) {
      next({name: 'signin'});
    }
    next()
  } else {
    next()
  }
})

export default router
