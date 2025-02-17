import { createApp } from 'vue'
import { createWebHistory, createRouter } from 'vue-router'
import VueCookies from 'vue-cookies';
import App from './App.vue'
import axios from 'axios';


import ToDoList from './components/ToDoList.vue'

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';
axios.defaults.withCredentials = true;

// Интерцептор запросов для добавления токена в заголовки
axios.interceptors.request.use(config => {
  const token = VueCookies.get('access_token');
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});


const routes = [
    { path: '/', component: ToDoList, meta: { requiresAuth: true },  },
    { path: '/login', component: () => import('@/components/LogView.vue') },
    { path: '/register', component: () => import('@/components/RegisterPage.vue') },
  ]
  
const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const token = VueCookies.get('access_token');
    if (!token) {
      next('/login');
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;

const app = createApp(App);

// Регистрируем глобальную переменную $axios
app.config.globalProperties.$axios = axios;

// Используем роутер
app.use(router);

// Монтируем приложение
app.mount('#app');
