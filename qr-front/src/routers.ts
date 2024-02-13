import { createRouter, createWebHistory } from 'vue-router'
import DetailResto from './pages/detail-resto.vue';
import Home from './pages/home.vue';


const routes = [
  { path: '/', component: Home },
  { path: '/resto/:slug', component: DetailResto },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;