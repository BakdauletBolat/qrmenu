import { createRouter, createWebHistory } from 'vue-router'
import DetailResto from './pages/detail-resto.vue';
import FoodDetail from '@/pages/detail-food.vue';
import Foods from "@/pages/foods.vue";
import Landing from "@/pages/Landing.vue";

const routes = [
  {
    name: 'landing',
    path: '/',
    component: Landing
  },
  {
    name: 'foods',
    path: '/foods/:categoryId',
    component: Foods
  },
  {
    name: 'food',
    path: '/food/:id',
    component: FoodDetail,
  },
  { path: '/resto/:slug', component: DetailResto },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});



router.beforeEach((to, _) => {
  // instead of having to check every route record with
  if (to.meta.isRequiredAuth) {
    return {
      path: '/login',
      query: { redirect: to.fullPath },
    }
  }
})

export default router;