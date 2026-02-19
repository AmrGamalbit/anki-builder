import { createRouter, createWebHistory } from 'vue-router';
import HomeView from "@/views/HomeView.vue";
import GeneratorView from "@/views/GeneratorView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: HomeView,
    },
    {
      path: '/generator',
      component: GeneratorView,
    }
  ],
});

export default router;
