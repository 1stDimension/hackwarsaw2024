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
    path: '/voter/create',
    name: 'voterCreate',
    component: () => import('../views/VoterCreateView.vue')
  },
  {
    path: '/bill/add',
    name: 'billAdd',
    component: () => import('../views/BillAddView.vue')
  },
  {
    path: '/bills',
    name: 'bills',
    component: () => import('../views/BillsView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
