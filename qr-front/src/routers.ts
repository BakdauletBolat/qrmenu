import { createRouter, createWebHistory } from 'vue-router'
import DetailResto from './pages/detail-resto.vue';
import QR from './pages/home.vue';
import Login from './pages/login.vue';
import AssignTable from "./pages/assign-table.vue";
import Orders from "./pages/orders.vue";
import FoodDetail from '@/pages/detail-food.vue';

const routes = [
  {
    name: 'home',
    path: '/', component: Orders, meta: {
      isRequiredAuth: true
    }
  },
  {
    name: 'login',
    path: '/login',
    component: Login,
  },
  {
    name: 'food',
    path: '/food/:id',
    component: FoodDetail,
  },
  {
    path: '/qr',
    name: 'qr',
    component: QR,
    meta: {
      isRequiredAuth: true
    }
  },
  {
    path: '/assign-table/:id',
    component: AssignTable,
    name: 'assign'
  },
  { path: '/resto/:slug', component: DetailResto },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});



router.beforeEach((to, _) => {
  // instead of having to check every route record with
  if (to.meta.isRequiredAuth && !localStorage.getItem('token')) {
    return {
      path: '/login',
      query: { redirect: to.fullPath },
    }
  }
})

export default router;