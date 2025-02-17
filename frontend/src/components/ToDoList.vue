<template>
  <div>
    <div v-for="task in tasks" :key="task.id">
      {{  task.date_create }}
    </div>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>

import axios from 'axios';
import VueCookies from 'vue-cookies';

export default {

  data() {
    return {
      tasks: []
    };
  },
  created() {
    this.get_tasks();
  },
  methods: {
    async get_tasks() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/tasks/');
        this.tasks = response.data
      } catch (error) {
        console.error('Ошибка')
      }
    },
    async logout() {
      try {
        // Отправляем POST-запрос на сервер для завершения сессии
        await axios.post('http://127.0.0.1:8000/api/logout/', {}, {
          withCredentials: true // Необходимо для отправки кук
        });

        // Удаляем куки с клиента
        VueCookies.remove('access_token');  // Удаляем access token
        VueCookies.remove('refresh_token'); // Удаляем refresh token
        alert('Logout suc!');
        // Перенаправляем пользователя на страницу входа
        this.$router.push('/login');  // Замените 'login' на название вашей маршрутизации для страницы входа
      } catch (error) {
        console.error("Ошибка при выходе из системы:", error);
        alert('Logout failed!');
      }
    },

  },

};

</script>

