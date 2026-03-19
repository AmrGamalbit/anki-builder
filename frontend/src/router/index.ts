import { createRouter, createWebHistory } from 'vue-router';
import HomeView from "@/views/HomeView.vue";
import GeneratorView from "@/views/GeneratorView.vue"
import SettingsView from '@/views/SettingsView.vue';

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
    },
    {
      path: '/settings',
      component: SettingsView,
    }
  ],
});

export default router;
