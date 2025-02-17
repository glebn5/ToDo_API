<template>
    <div>
        <h1>Регистрация</h1>
        <form @submit.prevent="register">
            <input v-model="username" type="text" placeholder="Username" required />
            <input v-model="password" type="password" placeholder="Password" required />
            <button type="submit">Зарегистрироваться</button>
        </form>
        <p>{{ message }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            username: '',
            password: '',
            message: '',
        };
    },
    methods: {
        async register() {
            try {
                const response = axios.post('http://127.0.0.1:8000/api/register/', {
                    username: this.username,
                    password: this.password
                });
                console.log(response.data);
                this.message = 'Регистрация завершена'
                setTimeout(() => {
                    this.$router.push('/login');
                }, 2000);
                
            } catch (error) {
                console.error(error);
                this.message = 'Ошибка регистрации';
            }
        },
    },
}

</script>

