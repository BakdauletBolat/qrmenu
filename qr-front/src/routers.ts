import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/home.vue';
const About = { template: '<div>About</div>' }

const routes = [
  { path: '/', component: About },
  { path: '/:slug', component: Home },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;