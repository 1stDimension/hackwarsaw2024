import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/voters',
    name: 'voters',
    component: () => import('../views/VotersView.vue')
  },
  {
    path: '/resolution/add',
    name: 'resolutionAdd',
    component: () => import('../views/ResolutionAddView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
